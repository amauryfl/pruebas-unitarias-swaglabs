# Repositorio publicado y revisión

Repositorio público: https://github.com/amauryfl/pruebas-unitarias-swaglabs  
Rama de entrega: `main`.

## Revisar desde GitHub

1. Abrir el enlace del repositorio.
2. Revisar `swaglab/`, `tests/`, `docs/`, `evidencias/` y `README.md`.
3. Descargar el informe Word y el video de la carpeta `entrega/`.
4. Consultar el historial de commits para comprobar el contenido publicado.

## Clonar y ejecutar

```bash
git clone https://github.com/amauryfl/pruebas-unitarias-swaglabs.git
cd pruebas-unitarias-swaglabs
git rev-parse HEAD
```

Seguir los comandos de instalación y ejecución del README para Windows, Linux o macOS. La suite debe producir **32 pruebas aprobadas**. El script de fallos controlados debe detectar M01 y M02. La ejecución vuelve a generar los archivos de evidencia; el historial conserva los registros originales.

## Copia del historial incluida en el paquete

El ZIP incluye `Pruebas_Unitarias_SwagLabs_Amaury.bundle`. Puede recuperarse sin conexión al servidor:

```bash
git clone Pruebas_Unitarias_SwagLabs_Amaury.bundle swaglabs-unitarias
cd swaglabs-unitarias
git log --oneline
```

Esta copia permite revisar el historial correspondiente al paquete. El origen de esa copia apunta al bundle; el enlace público indicado arriba identifica la publicación en GitHub.

## Entrega en el aula virtual

Adjuntar el documento Word y el video, e incluir el enlace del repositorio. El repositorio permite revisar las pruebas y sus instrucciones sin solicitar acceso. La carga en el aula virtual es el acto de entrega del estudiante.
