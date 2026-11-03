#!/usr/bin/env python3
"""Genera las páginas del Centro de ayuda (carpeta ayuda/) a partir de ayuda-src/.
Uso (desde capturadocs-landing):  python ayuda-src/build.py
Cada página sale autocontenida (CSS en línea, igual que guia.html). El contenido vive en
c_*.py; la plantilla y los datos estructurados (Article, BreadcrumbList, FAQPage) viven aquí."""
import html, json, os, re, sys
sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
from c_flagrancia import PAGINAS as P1
from c_formatos import PAGINAS as P2
from c_practica import PAGINAS as P3
from ventajas import GENERAL, POR_PAGINA

SITIO = 'https://capturadocs.com'
FECHA = '2026-10-30'
PAGINAS = P1 + P2 + P3
POR_SLUG = {p['slug']: p for p in PAGINAS}
CSS = open(os.path.join(AQUI, 'estilos.css'), encoding='utf-8').read()
FUENTES = ('<link rel="preconnect" href="https://fonts.googleapis.com"/><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>'
           '<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;600;700&family=Barlow+Condensed:wght@700;800&family=Barlow:wght@300;400;500;600&display=swap" rel="stylesheet"/>')
LEY = 'http://www.secretariasenado.gov.co/senado/basedoc/ley_0906_2004_pr007.html'

def e(s): return html.escape(s, quote=True)
def icono(n): return f'<svg class="ic" aria-hidden="true"><use href="../icons.svg#i-{n}"/></svg>'

NAV = '''<nav>
  <a href="../index.html" class="nav-logo"><img class="nav-icon" src="../logo.png" alt="CapturaDocs Express" width="36" height="36"/><div class="nav-text">Captura<span>Docs</span> Express</div></a>
  <div class="nav-links"><a href="./" class="nav-link">Centro de ayuda</a><a href="../index.html#descargas" class="nav-cta">Probar gratis</a></div>
</nav>'''
FOOT = '''<footer>
  <div style="display:flex;flex-direction:column;gap:4px">
    <div style="font-family:'Rajdhani',sans-serif;font-weight:700;font-size:.95rem;color:var(--white)">CapturaDocs<span style="color:var(--gold)"> Express</span></div>
    <div>Herramienta privada de apoyo — No oficial</div>
    <div>© 2026 CapturaDocs Express. Todos los derechos reservados.</div>
  </div>
  <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:12px 20px">
    <a href="../index.html">Inicio</a><a href="../guia.html">Guía de uso</a><a href="./">Centro de ayuda</a>
    <a href="mailto:contacto@capturadocs.com">contacto@capturadocs.com</a><a class="wa-link" href="#" target="_blank" rel="noopener">WhatsApp</a>
    <a href="../seguridad.html">Cómo protegemos tus datos</a>
  </div>
</footer>'''
AVISO = ('CapturaDocs Express es una herramienta privada e independiente, no afiliada ni avalada por la Policía Nacional de Colombia ni por la Fiscalía General de la Nación. '
         'Esta página es una ayuda general de lectura: no reemplaza el instructivo oficial vigente ni la orientación de tu fiscal o tu superior.')

def producto(p):
    """Bloque comercial antes del llamado a la acción: qué hace CapturaDocs Express con este formato."""
    if p['slug'] == 'index':
        tit, items = GENERAL
    else:
        tit, items = POR_PAGINA.get(p['slug'], GENERAL)
    lis = ''.join(f'<li>{i}</li>' for i in items)
    return (f'<section class="producto"><div class="container wide"><div class="prod-grid"><div class="prod-txt">'
            f'<div class="kicker">{icono("zap")} Con CapturaDocs Express</div><h2>{e(tit)}</h2><ul>{lis}</ul>'
            f'<div class="cta-botones"><a class="btn-p" href="../index.html#descargas">{icono("zap")} Probar gratis con 5 casos</a>'
            f'<a class="btn-o" href="../guia.html">{icono("book-open")} Ver cómo funciona</a></div></div>'
            f'<figure class="prod-img"><img src="../img/app-validacion.jpg" alt="Pantalla de CapturaDocs Express que avisa los campos que faltan antes de generar los documentos" width="1000" height="698" loading="lazy"/>'
            f'<figcaption>La aplicación revisa el caso antes de generar los documentos.</figcaption></figure></div></div></section>')

def cta(p):
    return f'''<div class="cta"><div class="container"><h2>{e(p.get('cta_t','Llena este formato una sola vez y deja que se generen todos'))}</h2>
<p>{e(p.get('cta_p','CapturaDocs Express diligencia el Informe de Captura, el Acta de Derechos, el Rótulo y la Cadena de Custodia con un solo formulario. Pruébalo gratis con 5 casos completos, sin tarjeta.'))}</p>
<div class="cta-botones"><a class="btn-p" href="../index.html#descargas">{icono('zap')} Probar gratis con 5 casos</a><a class="btn-o" href="../index.html#documentos">{icono('file-text')} Ver los documentos generados</a></div></div></div>'''

def json_ld(p):
    url = f"{SITIO}/ayuda/{p['slug']}.html" if p['slug'] != 'index' else f'{SITIO}/ayuda/'
    miga = [{'@type': 'ListItem', 'position': 1, 'name': 'Inicio', 'item': SITIO + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Centro de ayuda', 'item': SITIO + '/ayuda/'}]
    if p['slug'] != 'index':
        miga.append({'@type': 'ListItem', 'position': 3, 'name': p['corto'], 'item': url})
    grafo = [{'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': miga}]
    if p['slug'] != 'index':
        grafo.append({'@context': 'https://schema.org', '@type': 'Article', 'headline': p['h1_plano'], 'description': p['desc'],
                      'inLanguage': 'es-CO', 'datePublished': FECHA, 'dateModified': FECHA, 'mainEntityOfPage': url,
                      'author': {'@type': 'Organization', 'name': 'CapturaDocs Express', 'url': SITIO + '/'},
                      'publisher': {'@type': 'Organization', 'name': 'CapturaDocs Express', 'url': SITIO + '/',
                                    'logo': {'@type': 'ImageObject', 'url': SITIO + '/logo.png'}}})
    if p.get('faq'):
        grafo.append({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
            {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in p['faq']]})
    return '\n'.join('<script type="application/ld+json">' + json.dumps(g, ensure_ascii=False) + '</script>' for g in grafo)

def h1fmt(t):
    return re.sub(r'FPJ-(\d)', lambda m: '<span style="white-space:nowrap">' + m.group(0) + '</span>', t)

def ampliable(t):
    """Cada imagen de un formato se abre en grande al tocarla (en el celular un FPJ horizontal se lee muy pequeño)."""
    def una(m):
        src = re.search(r'src="([^"]+)"', m.group(1)).group(1)
        return ('<figure class="doc"><a href="' + src + '" target="_blank" rel="noopener" aria-label="Abrir la imagen en grande">' + m.group(1) + '</a>'
                '<figcaption>' + m.group(2) + ' · Toca la imagen para verla en grande.</figcaption></figure>')
    return re.sub(r'<figure class="doc">(<img [^>]+/>)<figcaption>(.*?)</figcaption></figure>', una, t)

def pagina(p):
    slug = p['slug']; url = f'{SITIO}/ayuda/' if slug == 'index' else f'{SITIO}/ayuda/{slug}.html'
    secs = p.get('secciones', [])
    toc = ''
    if len(secs) > 1:
        toc = '<div class="container toc"><div class="toc-box"><h2>En esta página</h2><ol>' + ''.join(
            f'<li><a href="#{i}">{e(t)}</a></li>' for i, t, _ in secs) + '</ol></div></div>'
    cuerpo = ampliable(''.join(f'<section id="{i}"><h2>{t_html}</h2>{c}</section>' for i, t_html, c in
                     [(i, e(t), c) for i, t, c in secs]))
    faq = ''
    if p.get('faq'):
        faq = '<div class="faq"><h2 style="font-family:\'Barlow Condensed\',sans-serif;font-weight:800;font-size:1.9rem;margin-bottom:14px">Preguntas frecuentes</h2>' + ''.join(
            f'<details><summary>{e(q)}</summary><p>{a_html}</p></details>' for q, a_html in [(q, e(a)) for q, a in p['faq']]) + '</div>'
    rel = ''
    if p.get('rel'):
        rel = '<div class="rel"><h2>Sigue leyendo</h2><div class="cards">' + ''.join(
            f'<a class="card" href="{r}.html">{icono(POR_SLUG[r]["icono"])}<h3>{e(POR_SLUG[r]["corto"])}</h3><p>{e(POR_SLUG[r]["desc_card"])}</p></a>'
            for r in p['rel']) + '</div></div>'
    fuente = ''
    if p.get('fuentes'):
        fuente = '<div class="fuente"><p><strong>Fuentes consultadas:</strong></p>' + ''.join(f'<p>{f}</p>' for f in p['fuentes']) + '</div>'
    crumbs = f'<div class="crumbs"><a href="../index.html">Inicio</a> / <a href="./">Centro de ayuda</a>' + (f' / <span>{e(p["corto"])}</span>' if slug != 'index' else '') + '</div>'
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{e(p['titulo'])}</title>
<meta name="description" content="{e(p['desc'])}"/>
<link rel="icon" type="image/png" href="../logo.png"/><link rel="apple-touch-icon" href="../logo.png"/>
<link rel="canonical" href="{url}"/><meta name="theme-color" content="#070f1f"/><meta name="robots" content="index,follow"/>
<meta property="og:type" content="article"/><meta property="og:title" content="{e(p['titulo'])}"/><meta property="og:description" content="{e(p['desc'])}"/>
<meta property="og:url" content="{url}"/><meta property="og:image" content="{SITIO}/logo-og.jpg"/><meta property="og:locale" content="es_CO"/>
{FUENTES}
<style>
{CSS}
{p.get('extra_css','')}
</style>
{json_ld(p)}
<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "b1c89c7467ba41fbb947cce3577347db"}}'></script>
<script src="../config.js"></script>
</head>
<body>
{NAV}
<header class="hero"><div class="container">{crumbs}<div class="kicker">{icono(p['icono'])} {e(p['kicker'])}</div><h1>{h1fmt(p['h1'])}</h1><p class="lead">{p['lead']}</p>
<p class="meta">Actualizado el 30 de octubre de 2026 · Lectura de {p.get('min', 6)} minutos</p></div></header>
{toc}
<main><article class="container">{cuerpo}</article>
{producto(p)}
{cta(p)}
<div class="container">{faq}{rel}<p class="aviso">{e(AVISO)}</p>{fuente}</div></main>
{FOOT}
<script>document.querySelectorAll('a.wa-link').forEach(function(el){{el.href='https://wa.me/'+window.CAPTURADOCS.WA_NUMBER;}});</script>
</body>
</html>
'''

def indice():
    p = POR_SLUG['index']
    p['secciones'] = [('guias', 'Los formatos, uno por uno', '<div class="cards">' + ''.join(
        f'<a class="card" href="{x["slug"]}.html">{icono(x["icono"])}<h3>{e(x["corto"])}</h3><p>{e(x["desc_card"])}</p></a>'
        for x in PAGINAS if x['grupo'] == 'formatos') + '</div>'),
        ('procedimiento', 'El procedimiento y la práctica', '<div class="cards">' + ''.join(
        f'<a class="card" href="{x["slug"]}.html">{icono(x["icono"])}<h3>{e(x["corto"])}</h3><p>{e(x["desc_card"])}</p></a>'
        for x in PAGINAS if x['grupo'] == 'practica') + '</div>')]
    return p

if __name__ == '__main__':
    salida = os.path.join(RAIZ, 'ayuda'); os.makedirs(salida, exist_ok=True)
    indice()
    for p in PAGINAS:
        nombre = 'index.html' if p['slug'] == 'index' else p['slug'] + '.html'
        open(os.path.join(salida, nombre), 'w', encoding='utf-8', newline='\n').write(pagina(p))
        print('ok', nombre)
