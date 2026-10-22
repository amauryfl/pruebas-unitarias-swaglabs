# Matriz de pruebas unitarias

Cada fila representa un escenario ejecutado. C01–C10 pertenecen a CU01; Q01–Q22 a CU02. Los IDs aparecen en los nombres de prueba o parámetros de pytest y en junit.xml. En checkout, los campos no indicados son válidos y la cantidad es 1, salvo indicación contraria.

## CU01

| ID | Reglas | Propósito | Datos / acción | Resultado esperado | Resultado real |
|---|---|---|---|---|---|
| C01 | R01 | Estado inicial | Carrito nuevo | Sin artículos; contador 0; subtotal 0.00. | APROBADA |
| C02 | R02, R07 | Agregar producto válido | Agregar backpack | True; mochila; contador 1; subtotal 29.99. | APROBADA |
| C03 | R02 | Evitar duplicados | Agregar backpack dos veces | Segunda alta False; una línea; subtotal 29.99. | APROBADA |
| C04 | R02, R07 | Sumar productos distintos | Agregar backpack y jacket | Dos identificadores; contador 2; subtotal 79.98. | APROBADA |
| C05 | R04, R05 | Retirar el último producto | Agregar y retirar backpack | True; carrito vacío; contador 0; subtotal 0.00. | APROBADA |
| C06 | R04, R07 | Conservar otros artículos | Agregar ambos; retirar backpack | Solo jacket; contador 1; subtotal 49.99. | APROBADA |
| C07 | R04 | Retirar un producto ausente | Carrito con mochila; retirar missing | False; contenido, contador y subtotal sin cambios. | APROBADA |
| C08 | R03 | Rechazar producto desconocido | Carrito con mochila; agregar missing | KeyError: Unknown product: missing; estado intacto. | APROBADA |
| C09 | R06 | Aislar compradores | Dos carritos; agregar al primero | El segundo permanece vacío, contador 0 y subtotal 0.00. | APROBADA |
| C10 | R07 | Conservar precisión monetaria | Precios Decimal 0.10 y 0.20 | Subtotal de tipo Decimal, exactamente 0.30. | APROBADA |

## CU02

| ID | Reglas | Propósito | Datos / acción | Resultado esperado | Resultado real |
|---|---|---|---|---|---|
| Q01 | R11, R14 | Aceptar datos completos | Amaury / Leonardo / 10000; cantidad 1 | Customer con los tres textos originales. | APROBADA |
| Q02 | R13 | Validar frontera de un carácter | A / L / 1; cantidad 1 | Customer("A", "L", "1"). | APROBADA |
| Q03 | R11 | Normalizar espacios laterales | "  Ana María  " / " Pérez " / " 10000 " | Customer("Ana María", "Pérez", "10000"). | APROBADA |
| Q04 | R11, R12 | Nombre obligatorio; patrón 011 | Nombre vacío; apellido y postal presentes | ValueError: First Name is required. | APROBADA |
| Q05 | R11, R12 | Apellido obligatorio; patrón 101 | Apellido vacío; nombre y postal presentes | ValueError: Last Name is required. | APROBADA |
| Q06 | R11, R12 | Postal obligatorio; patrón 110 | Postal vacío; nombre y apellido presentes | ValueError: Postal Code is required. | APROBADA |
| Q07 | R11, R12 | Priorizar nombre; patrón 001 | Nombre y apellido vacíos; postal presente | ValueError: First Name is required. | APROBADA |
| Q08 | R11, R12 | Priorizar nombre; patrón 010 | Nombre y postal vacíos; apellido presente | ValueError: First Name is required. | APROBADA |
| Q09 | R11, R12 | Priorizar apellido; patrón 100 | Apellido y postal vacíos; nombre presente | ValueError: Last Name is required. | APROBADA |
| Q10 | R11, R12 | Rechazar tres vacíos; patrón 000 | Nombre, apellido y postal vacíos | ValueError: First Name is required. | APROBADA |
| Q11 | R11 | Rechazar nombre de espacios | Nombre "  "; otros campos válidos | ValueError: First Name is required. | APROBADA |
| Q12 | R11 | Rechazar apellido de tabulación | Apellido "\t"; otros campos válidos | ValueError: Last Name is required. | APROBADA |
| Q13 | R11 | Rechazar postal de espacios | Postal "\n "; otros campos válidos | ValueError: Postal Code is required. | APROBADA |
| Q14 | R10 | Rechazar nombre no textual | Nombre None; otros campos válidos | TypeError: First Name must be text. | APROBADA |
| Q15 | R10 | Rechazar apellido no textual | Apellido []; otros campos válidos | TypeError: Last Name must be text. | APROBADA |
| Q16 | R10 | Rechazar postal numérico | Postal 10000 (int); otros campos válidos | TypeError: Postal Code must be text. | APROBADA |
| Q17 | R08 | Rechazar carrito vacío | Datos completos; cantidad 0 | ValueError: Cart must contain at least one product. | APROBADA |
| Q18 | R08 | Rechazar cantidad negativa | Datos completos; cantidad -1 | ValueError: Cart must contain at least one product. | APROBADA |
| Q19 | R09 | Rechazar booleano | Datos completos; cantidad True | TypeError: Item count must be an integer. | APROBADA |
| Q20 | R09 | Rechazar cantidad textual | Datos completos; cantidad "1" | TypeError: Item count must be an integer. | APROBADA |
| Q21 | R09 | Rechazar cantidad decimal | Datos completos; cantidad 1.0 | TypeError: Item count must be an integer. | APROBADA |
| Q22 | R08, R14 | Aceptar varios artículos | Amaury / Leonardo / 10000; cantidad 2 | Customer con los tres textos originales. | APROBADA |

## Trazabilidad de ejecución

La ejecución registrada en `evidencias/ejecucion.json` contiene 32 pruebas, cero fallos y cero errores. En las pruebas negativas, APROBADA significa que se produjo la excepción esperada, no que se aceptó una entrada inválida.
