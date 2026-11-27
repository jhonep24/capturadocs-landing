# ayuda-src — generador del Centro de ayuda

Fuente de las páginas de `ayuda/` (HTML estático, autocontenido, sin build en el despliegue).
Regenerar: `python ayuda-src/build.py` desde `capturadocs-landing`. **No se edita `ayuda/*.html` a mano**: se edita aquí y se regenera.

- `estilos.css` — estilo común (tokens de la landing: azul noche, dorado, Rajdhani/Barlow).
- `build.py` — plantilla, JSON-LD (Article, BreadcrumbList, FAQPage), tabla de contenidos, enlaces y llamado a la acción.
- `c_flagrancia.py`, `c_formatos.py`, `c_practica.py` — el contenido, una página por diccionario (`PAGINAS`).
- **Carrusel casilla por casilla** (guías FPJ-4 a FPJ-8): `carrusel.py` tiene el registro `FORMATOS` (slug → módulo, imágenes,
  nº de hojas), el HTML de respaldo (lista numerada, se lee sin JavaScript) y `CARRUSEL_JS`; los pasos de cada formato viven en
  `carrusel_fpjN.py` (`PAGINA` = tamaño de la hoja en puntos; cada paso: `h` hoja, `caja` (x0,y0,x1,y1) en puntos del PDF o `None`,
  `t`, `texto` (HTML), `ej`, `sug`). Imágenes: `python ayuda-src/render_hojas.py fpjN` → `img/carrusel-fpjN-hK.jpg` (1500 px, JPG q70).
  Estilos `.carr*` en `estilos.css` (mismo lenguaje que la sección «Documentos oficiales» de la landing). Una guía sin módulo no lleva carrusel.
  Para revisar cajas nuevas: dibujarlas sobre la imagen de la hoja antes de publicar (las coordenadas salen de `page.get_text('dict')`).
- Imágenes de apoyo: `img/doc-fpj7.jpg` y `doc-fpj8.jpg` (las usa la portada). Las `img/ayuda-fpj5-*.jpg` y `ayuda-fpj6-derechos.jpg`
  ya no se usan desde el 2026-11-27 (el carrusel reemplazó tablas e imágenes estáticas).
- Texto legal: sale de la Ley 906 de 2004 publicada por la Secretaría del Senado (`http://www.secretariasenado.gov.co/senado/basedoc/ley_0906_2004_pr006.html` y `pr007`; el `https` rechaza la conexión desde este PC). Si cambia una norma, revisar arts. 254-259 y 301-304.
- Al agregar una página: sumarla a `PAGINAS`, regenerar, agregarla a `sitemap.xml` y a `llms.txt`.

Fuentes y verificación de cada afirmación: `FUENTES.md`.
