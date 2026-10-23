# Resultados de la versión consolidada

Ejecución real iniciada el 2026-10-23T18:31:45.631368+00:00 (UTC), Python 3.12.14, Linux-6.18.55-x86_64-with-glibc2.39; pytest 9.1.1, pytest-cov 7.1.0 y coverage 7.16.2.

| Indicador | Resultado |
|---|---:|
| Pruebas ejecutadas y aprobadas | 36 |
| CU01 / CU02 | 12 / 24 |
| Fallos / errores / omitidos | 0 / 0 / 0 |
| Sentencias cubiertas | 56 de 56 |
| Ramas cubiertas | 14 de 14 |
| Cobertura del módulo | 100 % |
| Duración informada por pytest | 0.15 s |
| Código de salida | 0 |

La salida original se conserva en `evidencias/pytest.txt`; JUnit identifica cada escenario; `coverage.json` registra la cobertura y `ejecucion.json` incluye entorno, marcas de tiempo y SHA-256 del código y de las pruebas. El tiempo puede variar en otro equipo.

## Comprobación de detección de fallos

M01 reemplaza la eliminación de un producto por una consulta sin efectos: C05 falla. M02 elimina la validación del apellido: Q05 falla. Ambos cambios se aplicaron en copias temporales; el script detectó los dos y terminó con éxito. El código entregado conserva la implementación correcta. Los registros están en `mutaciones.json` y `M01_fallo_detectado.txt` / `M02_fallo_detectado.txt`.

Estas son dos comprobaciones dirigidas, no una campaña exhaustiva de mutaciones. El 100 % se refiere a las 56 sentencias y 14 ramas del módulo académico `swaglab/`; no mide el sitio público ni demuestra ausencia de otros defectos.

## Evolución

La entrega inicial tuvo 32 casos. La revisión de diseño añadió C11, C12, Q23 y Q24. Esta publicación incorpora los 36 casos de la actividad de diseño, sin cambios en las funciones de producción. Los registros `publicacion_github.json` y `pytest_desde_github.txt` se conservan como evidencia histórica de la descarga inicial de 32 casos; no son los resultados actuales.
