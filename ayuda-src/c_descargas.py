# Centro de ayuda: sección de descargas (solo los formatos en blanco, en PDF, para imprimir).
DOCS = [
    ('fpj5', 'FPJ-5', 'Informe de Captura en Flagrancia', '3 hojas · Versión 04', 'informe-captura-flagrancia-fpj5'),
    ('fpj6', 'FPJ-6', 'Acta de Derechos del Capturado', '2 hojas · Versión 03', 'acta-derechos-capturado-fpj6'),
    ('fpj7', 'FPJ-7', 'Rótulo de Elementos Materiales Probatorios y Evidencia Física', '1 hoja · Versión 04', 'rotulo-elementos-fpj7'),
    ('fpj8', 'FPJ-8', 'Registro de Cadena de Custodia', '2 hojas · Versión 04', 'cadena-de-custodia-fpj8'),
]
def _tarjetas():
    out = '<div class="dl-grid">'
    for n, fpj, nom, det, slug in DOCS:
        out += (f'<div class="dl-card"><div class="dl-fpj">{fpj}</div><h3>{nom}</h3><p class="dl-det">{det}</p>'
                f'<a class="btn-p" href="pdf/formato-{n}-en-blanco.pdf" download>Descargar PDF en blanco</a>'
                f'<a class="dl-guia" href="{slug}.html">Cómo se diligencia →</a></div>')
    return out + '</div>'

DESCARGAS = dict(
    slug='descargas-formatos-fpj', grupo='descargas', corto='Descargar formatos FPJ en blanco', icono='file-text',
    titulo='Descargar formatos FPJ-5, FPJ-6, FPJ-7 y FPJ-8 en blanco (PDF para imprimir)',
    desc='Descarga gratis en PDF y en blanco los formatos FPJ 5, FPJ 6, FPJ 7 y FPJ 8 de la captura en flagrancia, listos para imprimir y diligenciar.',
    desc_card='Los cuatro formatos en PDF, en blanco, para imprimir.',
    kicker='Descargas', min=2,
    h1='Descargar los formatos FPJ-5, 6, 7 y 8 <em>en blanco</em>',
    h1_plano='Descargar los formatos FPJ-5, 6, 7 y 8 en blanco',
    lead='Los cuatro formatos de la captura en flagrancia en PDF, sin datos, para imprimirlos y diligenciarlos. Cada uno tiene su guía casilla por casilla.',
    secciones=[
        ('formatos', 'Los formatos en blanco (PDF)', _tarjetas() + '''
<div class="tip"><p><strong>Antes de imprimir:</strong> son copias para diligenciar. Verifica que sea la versión vigente en tu institución. CapturaDocs Express es una herramienta independiente y no oficial.</p></div>'''),
        ('app', '¿Prefieres no llenarlos a mano?', '''
<p>Llenar cuatro formatos a mano significa escribir varias veces el mismo nombre, el mismo NUNC y la misma hora, y ahí aparecen los errores que hacen devolver un informe.</p>
<p>Con <strong>CapturaDocs Express</strong> llenas el caso <strong>una sola vez</strong> y salen el FPJ-5, el FPJ-6, el FPJ-7 y el FPJ-8 con los mismos datos: más rápido y sin errores de transcripción. La aplicación te avisa lo que falta antes de generar y funciona sin conexión.</p>
<p><a href="../index.html#descargas">Probar gratis con 5 casos</a> · <a href="informe-captura-flagrancia-fpj5.html">Ver la guía del FPJ-5</a></p>'''),
    ],
    faq=[
        ('¿Dónde descargo el formato FPJ 5 en blanco?', 'En esta página: el botón «Descargar PDF en blanco» del FPJ-5, el Informe de Captura en Flagrancia, de tres hojas.'),
        ('¿Dónde descargo el formato FPJ 6 en blanco?', 'En esta página, en la tarjeta del FPJ-6, el Acta de Derechos del Capturado, de dos hojas.'),
        ('¿Puedo imprimir los formatos FPJ?', 'Sí. Los PDF están pensados para imprimirse en tamaño carta y diligenciarse a mano o con la aplicación.'),
        ('¿Son los formatos oficiales?', 'Son copias de los formatos para diligenciar. Verifica siempre que sea la versión vigente en tu institución. CapturaDocs Express es independiente y no está afiliada a la Policía Nacional ni a la Fiscalía.'),
    ],
    rel=['informe-captura-flagrancia-fpj5', 'acta-derechos-capturado-fpj6', 'errores-comunes-informes-captura'],
    fuentes=[],
)
PAGINAS = [DESCARGAS]
