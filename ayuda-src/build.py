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
from pasos import PASOS, PDFS
from c_descargas import PAGINAS as P4
from c_primer_respondiente import PAGINAS as P5

SITIO = 'https://capturadocs.com'
FECHA = '2026-10-30'
PAGINAS = P1 + P2 + P3 + P4 + P5
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

def descarga(p):
    """Atajo a la descarga del formato en blanco (solo PDF) y a la sección de descargas."""
    if p['slug'] in PDFS:
        fpj = PDFS[p['slug']][1]
        return (f'<div class="descarga"><h3>Descarga el {fpj} en blanco</h3><p>PDF para imprimir y diligenciar. Copia para diligenciar: verifica que sea la versión vigente en tu institución.</p>'
                f'<div class="cta-botones"><a class="btn-p" href="pdf/formato-fpj{fpj[-1]}-en-blanco.pdf" download>{icono("file-text")} Descargar {fpj} en blanco (PDF)</a>'
                f'<a class="btn-o" href="descargas-formatos-fpj.html">Ver todos los formatos</a></div>'
                + ('' if p.get('suave') else '<p class="descarga-nota"><strong>¿Prefieres no llenarlo a mano?</strong> Con CapturaDocs Express llenas el caso una sola vez y este formato sale listo, más rápido y sin errores de transcripción. <a href="../index.html#descargas">Probar gratis con 5 casos</a>.</p>') + '</div>')
    return ''

def stepper(p):
    """Paso a paso interactivo: marca cada paso, ve el avance y compara hacerlo a mano con hacerlo con la app."""
    if p['slug'] not in PASOS: return ''
    tit, pasos = PASOS[p['slug']]
    n = len(pasos)
    lis = ''.join(
        f'<li class="sp"><div class="sp-cab"><b>{i}</b><h3>{e(t)}</h3><button type="button" class="sp-ok" aria-pressed="false">Hecho</button></div>'
        f'<div class="sp-cols"><div class="sp-mano"><span>A mano</span><p>{e(m)}</p></div>'
        f'<div class="sp-app"><span>Con CapturaDocs Express</span><p>{e(a)}</p></div></div></li>'
        for i, (t, m, a) in enumerate(pasos, 1))
    return (f'<div class="stepper" data-total="{n}"><div class="sp-prog"><div class="sp-bar"><i></i></div><span class="sp-txt" aria-live="polite">0 de {n} pasos</span></div>'
            f'<ol>{lis}</ol>'
            f'<div class="sp-fin" hidden><strong>Listo. A mano son {n} pasos repitiendo los mismos datos.</strong> '
            f'Con CapturaDocs Express los llenas <b>una sola vez</b>, la aplicación revisa antes de generar y sale todo con el formato oficial: más rápido y sin errores de transcripción. '
            f'<a class="btn-p" href="../index.html#descargas">{icono("zap")} Probar gratis con 5 casos</a></div></div>')

STEPPER_JS = ("<script>(function(){document.querySelectorAll('.stepper').forEach(function(st){var t=+st.dataset.total,bar=st.querySelector('.sp-bar i'),"
              "tx=st.querySelector('.sp-txt'),fin=st.querySelector('.sp-fin');function up(){var d=st.querySelectorAll('.sp.hecho').length;"
              "bar.style.width=(d*100/t)+'%';tx.textContent=d+' de '+t+' pasos';fin.hidden=d<t;}"
              "st.querySelectorAll('.sp-ok').forEach(function(b){b.addEventListener('click',function(){var li=b.closest('.sp'),on=li.classList.toggle('hecho');"
              "b.setAttribute('aria-pressed',on);b.textContent=on?'Hecho \\u2713':'Hecho';up();});});});})();</script>")

def comentarios(p):
    """Preguntas y comentarios con moderación previa. Se muestra solo si config.js trae COMENTARIOS_URL
    (o, en localhost, ?comentarios=http://localhost:8787 para pruebas). La página se ve completa sin esto."""
    if p['slug'] == 'index': return ''
    return (f'<section class="coment" id="comentarios" data-slug="{e(p["slug"])}" hidden>'
            '<h2>Preguntas y comentarios</h2>'
            '<div class="tip"><p><strong>Antes de escribir:</strong> lo que publiques es público. '
            'No escribas nombres, cédulas, teléfonos ni números de casos reales. Los comentarios se revisan antes de aparecer.</p></div>'
            '<div class="coment-lista" aria-live="polite"></div>'
            '<form class="coment-form" novalidate>'
            '<label for="c-nombre">Tu nombre o alias (opcional)</label>'
            '<input id="c-nombre" name="nombre" maxlength="40" autocomplete="off"/>'
            '<label for="c-texto">Tu pregunta o comentario</label>'
            '<textarea id="c-texto" name="texto" rows="4" maxlength="800" required></textarea>'
            '<input class="c-web" name="web" tabindex="-1" autocomplete="off" aria-hidden="true"/>'
            '<div class="c-ts"></div>'
            '<div class="coment-pie"><button type="submit" class="btn-p">Enviar para revisión</button><span class="coment-msg" role="status"></span></div>'
            '</form></section>')

COMENTARIOS_JS = ("<script>(function(){var s=document.getElementById('comentarios');if(!s)return;var C=window.CAPTURADOCS||{},u=C.COMENTARIOS_URL||'';"
 "if(/^(localhost|127\\.0\\.0\\.1)$/.test(location.hostname)){var q=new URLSearchParams(location.search).get('comentarios');if(q)u=q;}"
 "if(!u)return;u=u.replace(/\\/+$/,'');var slug=s.dataset.slug,lista=s.querySelector('.coment-lista'),f=s.querySelector('form'),msg=s.querySelector('.coment-msg'),"
 "btn=f.querySelector('button'),t0=0,tok='',wid=null,key=C.TURNSTILE_SITEKEY||'';"
 "function fecha(x){return new Date(x*1000).toLocaleDateString('es-CO',{day:'numeric',month:'long',year:'numeric'});}"
 "function pintar(cs){lista.textContent='';if(!cs.length){var p=document.createElement('p');p.className='coment-vacio';p.textContent='Aún no hay comentarios. Sé la primera persona en preguntar.';lista.appendChild(p);return;}"
 "cs.forEach(function(c){var d=document.createElement('div');d.className='coment-item';var m=document.createElement('div');m.className='coment-meta';"
 "m.textContent=(c.nombre||'Anónimo')+' · '+fecha(c.creado);var t=document.createElement('p');t.textContent=c.texto;d.appendChild(m);d.appendChild(t);"
 "if(c.respuesta){var r=document.createElement('div');r.className='coment-resp';var b=document.createElement('b');b.textContent='Respuesta de CapturaDocs: ';"
 "r.appendChild(b);r.appendChild(document.createTextNode(c.respuesta));d.appendChild(r);}lista.appendChild(d);});}"
 "fetch(u+'/api/comentarios?slug='+encodeURIComponent(slug)).then(function(r){return r.json();}).then(function(j){if(!j.ok)return;s.hidden=false;pintar(j.comentarios||[]);}).catch(function(){});"
 "function cargarTs(){if(!key||wid!==null||t0)return;t0=Date.now();var sc=document.createElement('script');sc.src='https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit';"
 "sc.async=true;sc.onload=function(){wid=window.turnstile.render(s.querySelector('.c-ts'),{sitekey:key,callback:function(t){tok=t;}});};document.head.appendChild(sc);}"
 "f.querySelector('textarea').addEventListener('focus',function(){if(!t0)t0=Date.now();cargarTs();});"
 "f.addEventListener('submit',function(ev){ev.preventDefault();msg.className='coment-msg';msg.textContent='';btn.disabled=true;"
 "var body={slug:slug,nombre:f.nombre.value,texto:f.texto.value,web:f.web.value,t:t0?Date.now()-t0:0,token:tok};"
 "fetch(u+'/api/comentarios',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}).then(function(r){return r.json();}).then(function(j){"
 "btn.disabled=false;if(j.ok){f.texto.value='';msg.className='coment-msg ok';msg.textContent=j.mensaje||'Enviado.';if(wid!==null&&window.turnstile){window.turnstile.reset(wid);tok='';}}"
 "else{msg.className='coment-msg mal';msg.textContent=j.error||'No se pudo enviar.';}}).catch(function(){btn.disabled=false;msg.className='coment-msg mal';msg.textContent='No se pudo enviar. Revisa tu conexión e inténtalo de nuevo.';});});"
 "})();</script>")

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
                      'inLanguage': 'es-CO', 'datePublished': p.get('publicado', FECHA), 'dateModified': p.get('modificado', '2026-11-22'), 'mainEntityOfPage': url,
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
    secs = list(p.get('secciones', []))
    st = stepper(p)
    if st and len(secs) > 1:
        secs.insert(1, ('paso-a-paso', 'Paso a paso: a mano y con la aplicación',
                        '<p>Marca cada paso a medida que avanzas. En cada uno ves cómo es hacerlo a mano y cómo se simplifica con CapturaDocs Express.</p>' + st))
    dl = descarga(p)
    dl = '<div class="container">' + dl + '</div>' if dl else ''
    toc = ''
    if len(secs) > 1:
        toc = '<div class="container toc"><div class="toc-box"><h2>En esta página</h2><ol>' + ''.join(
            f'<li><a href="#{i}">{e(t)}</a></li>' for i, t, _ in secs) + '</ol></div></div>'
    com = comentarios(p)
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
<p class="meta">Actualizado el {p.get('actualizado','22 de noviembre de 2026')} · Lectura de {p.get('min', 6)} minutos</p></div></header>
{toc}
{dl}
<main><article class="container">{cuerpo}</article>
{'' if p.get('suave') else producto(p)}
{'' if p.get('suave') else cta(p)}
<div class="container">{faq}{rel}{com}<p class="aviso">{e(AVISO)}</p>{fuente}</div></main>
{FOOT}
{STEPPER_JS if st else ''}
{COMENTARIOS_JS if com else ''}
<script>document.querySelectorAll('a.wa-link').forEach(function(el){{el.href='https://wa.me/'+window.CAPTURADOCS.WA_NUMBER;}});</script>
</body>
</html>
'''

def indice():
    p = POR_SLUG['index']
    p['secciones'] = [('guias', 'Los formatos, uno por uno', '<div class="cards">' + ''.join(
        f'<a class="card" href="{x["slug"]}.html">{icono(x["icono"])}<h3>{e(x["corto"])}</h3><p>{e(x["desc_card"])}</p></a>'
        for x in PAGINAS if x['grupo'] == 'formatos') + '</div>'),
        ('descargas', 'Descargas: formatos en blanco', '<div class="cards">' + ''.join(
        f'<a class="card" href="{x["slug"]}.html">{icono(x["icono"])}<h3>{e(x["corto"])}</h3><p>{e(x["desc_card"])}</p></a>'
        for x in PAGINAS if x['grupo'] == 'descargas') + '</div>'),
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
