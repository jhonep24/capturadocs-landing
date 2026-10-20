# Guía paso a paso en PDF

`CapturaDocs-Express-Guia-Paso-a-Paso.pdf` es la guía descargable: el recorrido de
la app de Windows con capturas reales, numeradas y señaladas, todas con datos
**inventados**. Las capturas **no se toman a mano**: las genera un script que
abre la app (la versión de `origin/main`) en un navegador con la red simulada.

## Regenerarla (cuando cambie la app)

```sh
sh guia-pdf/regenerar.sh      # Git Bash; ~1 minuto
```

Hace todo en una carpeta temporal: extrae `origin/main` de `informes-ponal`,
la construye, recorre el primer ingreso y un caso de ejemplo capturando cada
pantalla, recorta las imágenes y exporta el PDF aquí mismo. No toca el directorio
de trabajo de `informes-ponal` ni los cambios sin commitear de otra sesión, y no
se conecta al Worker de licencias real.

## Qué hay en `generador/`

| Archivo | Para qué |
|---|---|
| `e2e-guia/capturas.spec.js` | El recorrido: qué se llena, qué se señala, qué se captura |
| `e2e-guia/util-guia.js` | Datos inventados, resaltes numerados, primer ingreso |
| `e2e-guia/preparar-imagenes.py` | Recorta cada captura a su zona útil (así el texto sale legible impreso) |
| `e2e-guia/hacer-pdf.mjs` | Arma la maqueta y exporta el PDF |
| `guia-print.tpl.html` | **El texto de la guía** (todo lo que dice cada paso) |
| `playwright.guia.config.js` | Build de producción en el puerto 5179, tamaño de pantalla |
| `img-usuario/` | Las 3 imágenes que NO salen de la app (ver abajo) |

## Las 3 imágenes de Windows/Word/impresión (ilustraciones)

El Explorador de Windows, Word y el cuadro de impresión no existen en la versión web
que se captura. Se dibujan como **ilustraciones** (HTML en `generador/ilustraciones/`,
datos inventados, estilo claro) y se guardan ya generadas en `generador/img-usuario/`
(`explorador.png`, `word-pdf.png`, `imprimir-escala.png`; la guía las incluye sola).
Una captura real de la pantalla del dueño salía ilegible (4K a 300 %) y mostraba
carpetas personales. Para cambiarlas: editar el HTML y correr
`node generador/e2e-guia/ilustraciones.mjs <ilustraciones> <img-usuario>` (con
`@playwright/test` disponible, p. ej. desde `informes-ponal`), y recortar el blanco sobrante.

## Cuidados

- **Cambió una pantalla, un botón o un paso de la app** → volver a correr el script
  y revisar el PDF; si cambió un *texto* de la guía, se edita `guia-print.tpl.html`.
- **El script falla en un selector** (`getByRole`, etiquetas…) → casi siempre es
  que cambió el nombre de un botón o una etiqueta en la app; ajustar `capturas.spec.js`.
- **Nada real en las capturas.** Los valores de fábrica de "Configuración inicial"
  se reemplazan por inventados antes de capturar (la app trae precargados un NUNC
  y una URI que parecen reales, ver `CONTEXTO.md`). En el modal de licencia se
  tapan los botones de plan para no fijar precios en un archivo que circula meses.
- La guía en línea (`guia.html`) y este PDF dicen lo mismo con distinto formato;
  si se corrige uno, revisar el otro.
