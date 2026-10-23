# Relación entre las actividades y el código

El caso de estudio común es Swag Labs. Los laboratorios manuales examinaron catálogo, carrito y checkout; la implementación académica desarrolla las reglas del carrito y la validación de datos del comprador de ese mismo escenario.

| Antecedente | Requisito del módulo | Pruebas |
|---|---|---|
| Agregar productos y comprobar importes | Una unidad por ID y subtotal exacto | C01-C04, C07-C10 |
| CP016: retirar el último artículo | El carrito queda vacío | C05, C06, C11, C12 |
| CP001-CP008: campos obligatorios | Presencia de nombre, apellido y postal; orden de validación | Q01, Q04-Q10 |
| CP009-CP014: fronteras de texto | Aceptar texto de un carácter | Q02; las variantes de dos caracteres siguen siendo casos manuales |
| CP017 y Lab 1: confirmación sin artículos | Cantidad positiva antes de validar comprador | Q17, Q18, Q23 |
| EXP02: conflicto entre nombre y apellido | Conservar los tres datos en Customer y exigir apellido | Q01, Q05; no simulan eventos del navegador |
| Revisión del diseño | Tipos, espacios, ceros iniciales y cantidad múltiple | Q03, Q11-Q16, Q19-Q22, Q24 |

CP015 (Cancel), CP018 (Finish), CP019 (Atrás), CP020 (sesión), imágenes y ordenamiento siguen fuera de estas unidades. La suite no automatiza el navegador ni demuestra que los defectos de la web estén corregidos.

## Plan y revisión

Objetivos: comprobar estado, subtotal, validación, errores y aislamiento. Entrada: dependencias instaladas y contrato disponible. Salida: 36 aprobados, cero errores u omisiones y cobertura de las 14 reglas. Cada test crea objetos nuevos. Si una dependencia impide ejecutar, se corrige y se repite la suite completa.

La revisión del diseño incorporó cuatro casos: retirar de un carrito vacío, agregar de nuevo después de retirar, priorizar cantidad cero y conservar ceros iniciales del postal. El checklist adaptado y las fichas completas figuran en `diseno_casos.json`. Las aprobaciones externas y las reproducciones manuales pendientes de los laboratorios conservan su estado; no se sustituyen por resultados unitarios.
