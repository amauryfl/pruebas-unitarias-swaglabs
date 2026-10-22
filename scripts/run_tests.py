"""Ejecuta pytest y conserva sus resultados originales y el entorno utilizado."""

import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
from datetime import datetime, timezone
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidencias"
EVIDENCE.mkdir(exist_ok=True)
command = [
    sys.executable, "-m", "pytest", "-v", "-p", "pytest_cov",
    "--color=no", "--cov=swaglab", "--cov-branch",
    "--cov-report=term-missing", "--cov-report=json:evidencias/coverage.json",
    "--cov-report=html:evidencias/coverage_html",
    "--junitxml=evidencias/junit.xml",
]
environment = dict(os.environ, PYTEST_DISABLE_PLUGIN_AUTOLOAD="1", PYTHONIOENCODING="utf-8")
started = datetime.now(timezone.utc).isoformat()
run = subprocess.run(command, cwd=ROOT, env=environment, text=True,
                     encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
(EVIDENCE / "pytest.txt").write_text(run.stdout, encoding="utf-8")
print(run.stdout, end="")
metadata = {
    "started_utc": started,
    "finished_utc": datetime.now(timezone.utc).isoformat(),
    "python": platform.python_version(),
    "platform": platform.platform(),
    "command": ["python", *command[1:]],
    "exit_code": run.returncode,
    "files_sha256": {},
}
for folder in ["swaglab", "tests"]:
    for path in sorted((ROOT / folder).glob("*.py")):
        metadata["files_sha256"][path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
if (EVIDENCE / "junit.xml").exists():
    suites = ET.parse(EVIDENCE / "junit.xml").getroot().findall("testsuite")
    metadata["tests"] = sum(int(s.attrib["tests"]) for s in suites)
    metadata["failures"] = sum(int(s.attrib["failures"]) for s in suites)
    metadata["errors"] = sum(int(s.attrib["errors"]) for s in suites)
    metadata["skipped"] = sum(int(s.attrib["skipped"]) for s in suites)
if (EVIDENCE / "coverage.json").exists():
    metadata["coverage"] = json.loads((EVIDENCE / "coverage.json").read_text())["totals"]
(EVIDENCE / "ejecucion.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
raise SystemExit(run.returncode)
