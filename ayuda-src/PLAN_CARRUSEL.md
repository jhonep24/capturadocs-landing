# Plan: carrusel paso a paso (piloto FPJ-6) y acceso a la ayuda

Spec: `ayuda-src/DISENO_CARRUSEL.md`. Ejecución: nativa, en esta sesión; vista previa privada; no se hace push sin «aprobado» del dueño.

## Restricciones globales
- Colores de marca y estilos existentes intactos; sin librerías; sin cifras de tiempo; sin datos reales (ejemplos inventados y rotulados «ejemplo»).
- Cada instrucción se apoya en el formato oficial FPJ-6 v03 (PDF en `ayuda/pdf/`) o en la Ley 906 art. 303; consejos propios van rotulados «Sugerencia».
- Sin JavaScript la sección debe leerse como una lista numerada con todos los pasos.
- El Windows del dueño tiene animaciones apagadas: nada puede depender de una animación para entenderse.

## Revisión (casos que el spec no prueba)
- Celular vertical (360 px): la hoja y el texto deben caber sin scroll horizontal; recuadro visible tras el zoom.
- Paso sin recuadro (ej. «qué es este formato»): no debe fallar.
- Teclado (← →) y deslizar con el dedo sin quitar el scroll vertical de la página.

## Tareas
1. **Imágenes de las hojas** — Crear `ayuda-src/render_hojas.py` (PDF → `img/carrusel-fpj6-h1.jpg`, `-h2.jpg`, ancho 1100 px, JPG calidad ~80). Verificación: archivos existen y pesan < 250 KB cada uno.
2. **Datos de pasos y cajas** — Crear `ayuda-src/carrusel_fpj6.py` con `PASOS_FPJ6 = [dict(hoja, caja=(x,y,w,h en %) | None, titulo, texto, ejemplo, ojo, fuente)]` y las cajas calculadas desde el PDF (PyMuPDF `search_for`). Verificación: render con recuadros dibujado sobre cada paso y revisión visual.
3. **Componente** — En `ayuda-src/build.py` agregar `carrusel(slug) -> str` (HTML con lista de respaldo sin JS), `CARRUSEL_JS` (flechas, teclado, deslizar, barra de avance, `aria-live`) y su CSS `.carr*` en `estilos.css`; insertarlo en `pagina()` como sección «Paso a paso, casilla por casilla» (id `casilla-por-casilla`) tras «¿Qué es?». Verificación: `python build.py` sin errores; página FPJ-6 contiene la sección y `sitemap` sigue en 15 URLs.
4. **Acceso desde la landing** — En `index.html`: enlace «Ayuda» visible en `<nav>` (junto a «Obtener acceso») y franja bajo el hero «¿Primera vez? Aprende a llenar cada formato paso a paso → Centro de ayuda»; mismo enlace «Ayuda» en la `NAV` de `build.py` ya existe (`Centro de ayuda`). Verificación: captura en 360 px y en escritorio.
5. **Vista previa y aprobación** — Servir en local, capturar pantallas (escritorio + móvil), enviarlas al dueño; documentar en `CONTEXTO.md`/`LECCIONES_APRENDIDAS.md` solo tras el «aprobado» y el push.
