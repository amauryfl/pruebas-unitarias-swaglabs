# Guion del video de demostración

El video muestra archivos de código y extractos de salidas reales guardadas. Se presentan con pausas para explicar su significado; no se representa una sesión de navegador ni una ejecución en vivo. La narración es sintética y el contenido técnico se conserva en los archivos de evidencia.

## 1. Diseño e implementación de pruebas unitarias

Esta demostración presenta el diseño y la implementación de treinta y dos pruebas unitarias para dos casos de uso: administrar el carrito y validar el checkout. El código probado es un módulo académico independiente en Python, inspirado en el caso de estudio de Swag Labs.

Fuente en pantalla: CASO DE ESTUDIO · SWAG LABS.

## 2. CU01 · Administrar el carrito

La clase Cart administra una unidad por producto. Agregar un identificador desconocido produce un error; agregar uno repetido conserva una sola línea. Retirar un producto actualiza el contenido, mientras que retirar uno ausente devuelve falso. El subtotal utiliza Decimal para mantener la precisión monetaria.

Fuente en pantalla: CÓDIGO ORIGINAL · swaglab/cart.py.

## 3. CU02 · Validar datos del checkout

La validación exige una cantidad entera positiva y tres campos de texto: nombre, apellido y código postal. Se eliminan espacios laterales y se rechazan entradas vacías. La función devuelve un objeto Customer con los datos válidos. Las excepciones distinguen entre un tipo incorrecto y un valor que incumple las reglas.

Fuente en pantalla: CÓDIGO ORIGINAL · swaglab/checkout.py.

## 4. Ejemplo de CU01 · Retirar el último producto

La prueba C cero cinco tiene tres partes. Primero prepara un carrito con una mochila. Después ejecuta la eliminación. Finalmente comprueba el resultado verdadero, la lista vacía, el contador en cero y el subtotal en cero. Verificar todo el estado evita aprobar una función que solo devuelve un indicador de éxito.

Fuente en pantalla: PRUEBA ORIGINAL · tests/test_cart.py · C05.

## 5. Ejemplo de CU02 · Tabla de decisión

La parametrización ejecuta siete combinaciones con campos vacíos. Junto al caso válido Q cero uno, cubre los ocho patrones de presencia de nombre, apellido y postal. La prueba exige ValueError y verifica el mensaje exacto. Q cero cinco comprueba específicamente que un apellido vacío impida continuar.

Fuente en pantalla: PRUEBA ORIGINAL · tests/test_checkout.py · Q04–Q10.

## 6. Ejecución real · 10 pruebas del carrito

El comando de ejecución es python scripts barra run guion bajo tests punto py. Esta salida corresponde a la ejecución real registrada, presentada con una pausa para su lectura. Las diez pruebas del carrito aprobaron: estado inicial, altas, duplicados, subtotal, bajas, productos desconocidos, aislamiento y precisión monetaria.

Fuente en pantalla: EXTRACTO SIN ALTERAR · evidencias/pytest.txt.

## 7. Ejecución real · Checkout: campos obligatorios

En el checkout aprobaron los datos completos, el límite mínimo de un carácter, la normalización y todas las combinaciones de obligatoriedad. Una prueba negativa aprobada significa que el código rechazó correctamente la entrada y produjo la excepción prevista. No significa que haya aceptado datos inválidos.

Fuente en pantalla: EXTRACTO SIN ALTERAR · evidencias/pytest.txt.

## 8. Ejecución real · Checkout: tipos y cantidades

También se verificaron tabulaciones y espacios, valores que no son texto, carrito vacío, cantidad negativa, booleanos, texto y números decimales como cantidad. El caso de dos artículos también aprueba. En total son veintidós escenarios del checkout y treinta y dos escenarios en la suite completa.

Fuente en pantalla: EXTRACTO SIN ALTERAR · evidencias/pytest.txt.

## 9. Resultado · 32 pruebas aprobadas

La suite terminó con treinta y dos pruebas aprobadas, cero fallos y código de salida cero. La medición cubrió cincuenta y seis sentencias y catorce ramas, el cien por ciento de estas dos unidades pequeñas. Esa cifra describe el código incluido; no garantiza ausencia de defectos ni representa cobertura del sitio público.

Fuente en pantalla: EXTRACTO SIN ALTERAR · evidencias/pytest.txt.

## 10. Comprobación de errores · M01

Para comprobar la utilidad de las pruebas se introdujeron fallos en copias temporales. En M cero uno, retirar el producto dejó de eliminarlo. C cero cinco falló porque el carrito seguía conteniendo la mochila. Ese fallo es el resultado esperado del experimento y demuestra que la prueba detecta la alteración.

Fuente en pantalla: EXTRACTO REAL · evidencias/M01_fallo_detectado.txt.

## 11. Comprobación de errores · M02

En M cero dos se omitió la validación del apellido. Q cero cinco falló porque no se lanzó ValueError. Las dos alteraciones fueron detectadas. Se realizaron en carpetas temporales, de modo que el código original conserva su comportamiento correcto. Son dos comprobaciones dirigidas, no una campaña exhaustiva de mutaciones.

Fuente en pantalla: EXTRACTO REAL · evidencias/M02_fallo_detectado.txt.

## 12. Cómo revisar el repositorio publicado

El proyecto está publicado en GitHub. Se descargó una copia independiente y las treinta y dos pruebas volvieron a aprobar, con cobertura completa del módulo y los dos fallos controlados detectados. Para revisarlo, se instalan las versiones fijadas y se ejecutan los dos scripts. La carpeta entrega contiene el informe y este video. La matriz documenta el propósito de cada prueba y su caso de uso.

Fuente en pantalla: REPRODUCCIÓN · DOCUMENTACIÓN · GIT.

