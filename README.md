# Pruebas unitarias del carrito y checkout

**Amaury Francisco Leonardo · 25-1128**  
TI3-312 Aseguramiento de la Calidad del Software · UNIBE

Este proyecto implementa un módulo académico en Python inspirado en los casos de uso del carrito y checkout de Swag Labs. Incluye dos unidades de lógica de negocio y 32 pruebas con pytest. Se comprueban estados, resultados, errores esperados y aislamiento entre ejecuciones.

La implementación probada es la que se encuentra en `swaglab/`. Es una aplicación académica independiente; los resultados no se atribuyen al código interno del sitio público saucedemo.com. Las reglas completas están en `docs/casos_de_uso.md`.

## Requisitos y ejecución

Repositorio: https://github.com/amauryfl/pruebas-unitarias-swaglabs

```bash
git clone https://github.com/amauryfl/pruebas-unitarias-swaglabs.git
cd pruebas-unitarias-swaglabs
```

Utilizar Python 3.12 y Git. Desde la carpeta del proyecto, en PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe scripts/run_tests.py
```

En Linux o macOS:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python scripts/run_tests.py
```

No es necesario activar el entorno virtual. La instalación inicial requiere acceso a Internet; las pruebas se ejecutan localmente sin navegador, credenciales, servidor ni base de datos.

Para seleccionar un caso de uso en PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pytest -v -m cu01
.\.venv\Scripts\python.exe -m pytest -v -m cu02
```

Para verificar que las pruebas detectan los dos fallos controlados:

```powershell
.\.venv\Scripts\python.exe scripts/check_fault_detection.py
```

Este último comando crea copias temporales. En ellas se espera que una prueba falle por cada alteración; el script termina correctamente cuando detecta ambos fallos. La suite principal conserva su código correcto.

## Casos de uso y documentación

| Caso | Unidad | Archivo de pruebas | Escenarios |
|---|---|---|---:|
| CU01 Administrar el carrito | `Cart` | `tests/test_cart.py` | 10 |
| CU02 Validar el checkout | `validate_checkout` | `tests/test_checkout.py` | 22 |

- `docs/casos_de_uso.md`: precondiciones, flujos, reglas y resultados.
- `docs/matriz_pruebas.md`: propósito, datos y resultado esperado de cada prueba.
- `docs/resultados.md`: resultados reales, cobertura y detección de fallos.
- `docs/publicar_en_git.md`: instrucciones de publicación y revisión.
- `docs/guion_video.md`: recorrido de la demostración y explicación del código.

## Evidencias que se generan

| Archivo | Contenido |
|---|---|
| `evidencias/pytest.txt` | Salida completa de pytest |
| `evidencias/junit.xml` | Resultado de cada escenario en formato JUnit |
| `evidencias/coverage.json` | Cobertura de sentencias y ramas |
| `evidencias/coverage_html/index.html` | Informe navegable de cobertura |
| `evidencias/ejecucion.json` | Entorno, comando, marcas de tiempo y huellas del código |
| `evidencias/mutaciones.json` | Resultado de las dos alteraciones controladas |
| `evidencias/M01_fallo_detectado.txt` | Fallo real al impedir que Remove elimine el artículo |
| `evidencias/M02_fallo_detectado.txt` | Fallo real al omitir la validación del apellido |
| `evidencias/publicacion_github.json` | Commit descargado de GitHub, entorno y verificación independiente |
| `evidencias/pytest_desde_github.txt` | Salida original de las 32 pruebas ejecutadas desde esa descarga |

El umbral de cobertura es 100 % para las dos unidades pequeñas definidas en este proyecto. La cobertura se calcula sobre `swaglab/`; no representa cobertura del sitio público, de la interfaz ni de todos los posibles datos de entrada.

## Revisión de la entrega

1. Leer `docs/casos_de_uso.md` y `docs/matriz_pruebas.md`.
2. Ejecutar `scripts/run_tests.py` y comprobar el código de salida 0.
3. Abrir `evidencias/coverage_html/index.html`.
4. Ejecutar `scripts/check_fault_detection.py` y comprobar M01 y M02 detectados.
5. Revisar el informe Word y el video incluidos en el paquete de entrega.

## Archivos de entrega

- [Informe Word](entrega/TI3312_Pruebas_Unitarias_LeonardoAmaury.docx)
- [Video explicativo en español](entrega/Demostracion_Pruebas_Unitarias_Amaury.mp4)
- [Instrucciones para revisar el repositorio](docs/publicar_en_git.md)

El código y las pruebas se publican en la rama `main`. El informe y el video se encuentran en `entrega/`. Para entregar la tarea en el aula virtual, adjuntar el informe y el video e incluir el enlace de este repositorio.
