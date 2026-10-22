# Casos de uso y reglas de la implementación

Se conserva el caso de estudio de compras de Swag Labs y se implementan dos unidades de negocio en Python. Los nombres de productos y precios de referencia provienen de los escenarios documentados en el laboratorio anterior. Las reglas que siguen constituyen el contrato explícito de este módulo académico.

## CU01 Administrar el carrito

**Actor:** comprador.  
**Objetivo:** seleccionar o retirar productos y conocer el número de artículos y el subtotal.  
**Unidad:** clase `Cart`, en `swaglab/cart.py`.  
**Precondición:** existe un catálogo de productos con identificador, nombre y precio `Decimal`.

Flujo principal:

1. Crear un carrito vacío.
2. Agregar un identificador presente en el catálogo.
3. Consultar productos, contador y subtotal.
4. Retirar un producto y comprobar el estado resultante.

Reglas y alternativas:

- R01: el carrito comienza vacío, con contador 0 y subtotal 0.00.
- R02: cada identificador aparece como máximo una vez; agregarlo de nuevo devuelve `False` y conserva el estado.
- R03: un producto desconocido produce `KeyError` sin modificar el carrito.
- R04: retirar un producto presente devuelve `True`; si no está, devuelve `False` sin modificar otros artículos.
- R05: retirar el último producto deja el carrito vacío.
- R06: cada instancia de carrito mantiene su propio estado.
- R07: el subtotal suma precios con `Decimal`; no incluye impuestos, descuentos ni envío.

**Postcondición:** el contenido, el contador y el subtotal son coherentes con las operaciones válidas.

## CU02 Validar el checkout

**Actor:** comprador.  
**Objetivo:** validar los datos requeridos antes de continuar una compra.  
**Unidad:** función `validate_checkout`, en `swaglab/checkout.py`.  
**Entradas:** nombre, apellido, código postal y cantidad de artículos.

Flujo principal:

1. Recibir las cuatro entradas.
2. Comprobar que la cantidad sea un entero positivo.
3. Validar nombre, apellido y código postal, en ese orden.
4. Devolver un objeto `Customer` con los textos normalizados.

Reglas y alternativas:

- R08: el carrito debe contener al menos un artículo; cero o cantidades negativas producen `ValueError`.
- R09: la cantidad debe ser de tipo `int`; se rechazan booleanos, cadenas y números decimales con `TypeError`.
- R10: nombre, apellido y código postal deben ser cadenas; un tipo distinto produce `TypeError`.
- R11: se eliminan espacios laterales y cada campo debe conservar al menos un carácter; una entrada vacía o formada solo por espacios produce `ValueError`.
- R12: el primer error interrumpe la validación; se comprueba cantidad, nombre, apellido y postal en ese orden.
- R13: se admite texto ordinario de un carácter. El código postal se valida por presencia, sin afirmar validez geográfica ni longitud máxima.
- R14: la validación devuelve datos del comprador; no cobra, no envía productos y no persiste una orden.

**Postcondición exitosa:** se obtiene `Customer` con los tres campos presentes.  
**Postcondición alternativa:** se informa una excepción y no se devuelve un comprador válido.

## Estrategia de pruebas

Cada prueba sigue preparación, ejecución y comprobación. El carrito se crea de nuevo mediante una fixture, y la validación de checkout recibe datos directamente. Los valores esperados se fijan en las pruebas; no se calculan llamando de nuevo a la implementación que se quiere comprobar.

La tabla de decisión contiene las ocho combinaciones de presencia de los tres campos: Q01 comprueba 111; Q04-Q10 comprueban las otras siete. Se añaden fronteras de cero y un carácter, normalización, tipos inválidos y cantidades 0, -1, 1 y 2. El alcance unitario se limita a estas dos unidades en memoria.
