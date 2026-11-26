# Diseño: acceso a la ayuda y carrusel paso a paso (2026-11-25)

Aprobado por el dueño en el chat el 2026-11-25 (enfoque A, piloto FPJ-6).

## Intención
Que la ayuda se encuentre desde la primera pantalla de la landing y que cada guía enseñe a llenar el formato
**casilla por casilla, como a un niño pequeño**: nada se da por sabido, sin dudas al final.

## Metas / no metas
- Meta: botón visible «Ayuda» en el menú y franja bajo la portada. Carrusel con la hoja oficial y la casilla resaltada.
- Meta: texto simple, ejemplo con datos inventados rotulado «ejemplo», aviso de error común.
- No meta: tocar colores de marca, quitar el «paso a paso» actual a mano vs. con la app, publicar sin «aprobado».
- Anti-meta: afirmar algo sin fuente. Lo no sustentable se omite; lo que sea consejo va rotulado «Sugerencia».

## Enfoques considerados
- **A (elegido):** una imagen por hoja + recuadro/zoom por CSS + coordenadas por casilla. Ligero, el texto sigue siendo HTML (SEO), editable.
- B: una imagen recortada por paso. Descartado: decenas de archivos, pesado en celular, hay que rehacer todo si cambia el formato.

## Decisiones del dueño
Enfoque A; piloto con el FPJ-6; vista previa privada antes de cualquier push.

## Decisiones mías (a revisar)
- Hoja renderizada desde el PDF oficial en blanco (`ayuda/pdf/formato-fpjN-en-blanco.pdf`) a JPG/WebP, ancho ~1200 px.
- Carrusel en `build.py` (JS propio, sin librerías): flechas, teclado, deslizar, barra de avance, `aria-live`.
- Los pasos viven en un archivo por formato (`ayuda-src/carrusel_fpj6.py`), con `hoja`, `caja` (x,y,w,h en %), `titulo`, `texto`, `ejemplo`, `ojo`, `fuente`.
- Menú de la landing: enlace «Ayuda» + franja bajo el hero; se verifica en móvil.

## Pendiente para el constructor
Mapear coordenadas de cada casilla; redactar los pasos contra el formato oficial y la Ley 906; sin JS el contenido debe seguir leyéndose como lista.
