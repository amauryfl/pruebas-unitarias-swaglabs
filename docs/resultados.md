# Resultados de la ejecución

La suite se ejecutó realmente el 2026-10-22T14:14:02.611747+00:00 (UTC) con Python 3.12.14 sobre Linux-6.18.55-x86_64-with-glibc2.39. Se usaron pytest 9.1.1, pytest-cov 7.1.0 y coverage 7.16.2.

| Indicador | Resultado |
|---|---:|
| Escenarios ejecutados | 32 |
| CU01 / CU02 | 10 / 22 |
| Aprobados | 32 |
| Fallos / errores / omitidos | 0 / 0 / 0 |
| Código de salida | 0 |
| Sentencias cubiertas | 56 de 56 (100 %) |
| Ramas cubiertas | 14 de 14 (100 %) |
| Sentencias excluidas | 0 |

La salida original está en `evidencias/pytest.txt`; el detalle por escenario, en `evidencias/junit.xml`; la medición, en `evidencias/coverage.json` y `evidencias/coverage_html/index.html`. `evidencias/ejecucion.json` registra el comando, el entorno, las marcas de tiempo y SHA-256 de los archivos probados. El tiempo de ejecución varía con el equipo.

## Detección de errores

En copias temporales independientes se introdujeron dos fallos. M01 sustituyó la eliminación del producto por una consulta que deja el carrito sin cambios: C05 falló al esperar un carrito vacío. M02 omitió validar el apellido: Q05 falló porque no se produjo ValueError. Las dos alteraciones fueron detectadas; sus procesos pytest devolvieron 1, como se esperaba. El script de comprobación terminó con éxito y el código original no se modificó.

No se trata de una campaña exhaustiva de mutaciones: son dos comprobaciones dirigidas. La cobertura del 100 % se limita a las 56 sentencias y 14 ramas del módulo `swaglab`; no demuestra ausencia de defectos ni cobertura del sitio público, de la interfaz o de todos los valores posibles.

## Estado de entrega

Código, pruebas, documentación, evidencias, informe Word y video publicados en https://github.com/amauryfl/pruebas-unitarias-swaglabs (rama main). Los archivos de entrega se encuentran en entrega/.

La descarga independiente del commit 377b71bf36f30ed1daac148707bbff38a7e33811 desde GitHub aprobó las 32 pruebas, mantuvo 100 % de cobertura de las 56 sentencias y 14 ramas y detectó M01 y M02. Esta verificación se conserva en evidencias/publicacion_github.json y evidencias/pytest_desde_github.txt. El documento y el video se añadieron posteriormente sin modificar el código probado.
