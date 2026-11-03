# ayuda-src — generador del Centro de ayuda

Fuente de las páginas de `ayuda/` (HTML estático, autocontenido, sin build en el despliegue).
Regenerar: `python ayuda-src/build.py` desde `capturadocs-landing`. **No se edita `ayuda/*.html` a mano**: se edita aquí y se regenera.

- `estilos.css` — estilo común (tokens de la landing: azul noche, dorado, Rajdhani/Barlow).
- `build.py` — plantilla, JSON-LD (Article, BreadcrumbList, FAQPage), tabla de contenidos, enlaces y llamado a la acción.
- `c_flagrancia.py`, `c_formatos.py`, `c_practica.py` — el contenido, una página por diccionario (`PAGINAS`).
- Imágenes de apoyo: `img/ayuda-*.jpg` (recortes de las muestras) y `img/doc-fpj7.jpg`, `doc-fpj8.jpg`.
- Texto legal: sale de la Ley 906 de 2004 publicada por la Secretaría del Senado (`http://www.secretariasenado.gov.co/senado/basedoc/ley_0906_2004_pr006.html` y `pr007`; el `https` rechaza la conexión desde este PC). Si cambia una norma, revisar arts. 254-259 y 301-304.
- Al agregar una página: sumarla a `PAGINAS`, regenerar, agregarla a `sitemap.xml` y a `llms.txt`.
