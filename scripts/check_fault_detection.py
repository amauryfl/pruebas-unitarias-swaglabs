"""Prueba dos alteraciones aisladas en copias temporales; no modifica swaglab/."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidencias"
EVIDENCE.mkdir(exist_ok=True)
mutations = [
    {
        "id": "M01", "description": "Remove deja el producto en el carrito",
        "file": "swaglab/cart.py",
        "original": "del self._items[product_id]",
        "replacement": "self._items.get(product_id)",
        "test": "tests/test_cart.py::test_C05_remove_last_product",
    },
    {
        "id": "M02", "description": "Checkout omite validar el apellido",
        "file": "swaglab/checkout.py",
        "original": 'last = _required_text(last_name, "Last Name")',
        "replacement": "last = str(last_name)",
        "test": "tests/test_checkout.py::test_required_fields_decision_table[Q05_101]",
    },
]
results = []
for mutation in mutations:
    with tempfile.TemporaryDirectory(prefix="swaglab_mutation_") as temporary:
        target = Path(temporary)
        for name in ["swaglab", "tests"]:
            shutil.copytree(ROOT / name, target / name, ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copy2(ROOT / "pyproject.toml", target / "pyproject.toml")
        source = target / mutation["file"]
        text = source.read_text(encoding="utf-8")
        if text.count(mutation["original"]) != 1:
            raise RuntimeError("El código cambió: no se puede aplicar la mutación de forma inequívoca")
        source.write_text(text.replace(mutation["original"], mutation["replacement"]), encoding="utf-8")
        command = [sys.executable, "-m", "pytest", "-v", "--color=no", mutation["test"]]
        run = subprocess.run(command, cwd=target, text=True, encoding="utf-8",
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             env=dict(os.environ, PYTEST_DISABLE_PLUGIN_AUTOLOAD="1"))
        (EVIDENCE / f'{mutation["id"]}_fallo_detectado.txt').write_text(run.stdout, encoding="utf-8")
        detected = run.returncode == 1 and "1 failed" in run.stdout and "ERROR " not in run.stdout
        results.append({**mutation, "exit_code": run.returncode, "detected": detected})
        print(f'{mutation["id"]}: {mutation["description"]} -> ' + ("DETECTADO" if detected else "NO DETECTADO"))
(EVIDENCE / "mutaciones.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
raise SystemExit(0 if all(r["detected"] for r in results) else 1)
