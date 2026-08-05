# Contexto de la landing — CapturaDocs Express

Este archivo es el punto de partida para modificar o mejorar la landing
(`index.html`) desde una sesión nueva, sin tener que releer todo el HTML para
entender el sistema de diseño o las decisiones ya tomadas.

## Qué es este repo

Landing estática de una sola página (`index.html`, sin build, sin
frameworks) para **CapturaDocs Express**, la app de informes de captura de
`informes-ponal`. Se publica en GitHub Pages, con dominio propio:
https://capturadocs.com/ (el link de GitHub sigue funcionando como alias:
https://jhonep24.github.io/capturadocs-landing/). El dominio se compró en
Cloudflare Registrar y el DNS apunta a las IPs de GitHub Pages — ver
`CNAME` en la raíz del repo y `git log` del commit que lo configuró
(2026-08-04) si hace falta tocarlo de nuevo.

También vive aquí `api-config.json`, que le indica a la app (`licencia.js`
en `informes-ponal`) la URL vigente del Worker de licencias — ver la sección
"Ubicación del servidor" en `informes-ponal/README_TECNICO.md`. **No tocar
ese archivo al editar la landing** a menos que el Worker se haya mudado de
verdad.

Además: `robots.txt` y `sitemap.xml` (SEO básico), y `logo-og.jpg`
(1200×630, imagen de vista previa al compartir el link — regenerarla con
Pillow si cambia el logo o el copy principal, no solo redimensionar la
vieja). El `<head>` de `index.html` también trae un bloque JSON-LD
(`schema.org/SoftwareApplication`) con nombre, descripción y los 4 precios
— actualízalo si cambian los planes o precios en `.pricing`.

Ver [LECCIONES_APRENDIDAS.md](LECCIONES_APRENDIDAS.md) para el porqué de
las decisiones de SEO/accesibilidad tomadas y problemas ya resueltos.

## Sistema de diseño (todo vive en el `<style>` del `<head>`)

- **Paleta** (variables CSS en `:root`): `--navy` (fondo principal, casi
  negro azulado), `--navy2`/`--navy3` (fondos de tarjetas/secciones
  alternas, cada vez un poco más claro), `--gold`/`--gold2` (acento
  principal, CTAs y títulos destacados), `--accent` (azul, botón
  secundario), `--green` (WhatsApp/CTA de conversión), `--white` (texto
  principal), `--muted` (texto secundario/descripciones), `--border`
  (bordes sutiles en tarjetas y separadores).
- **Tipografías** (Google Fonts, ya cargadas):
  - `Barlow Condensed` (700/800) → títulos grandes (`h1`, `.stitle`, `.cta h2`).
  - `Rajdhani` (400/600/700) → todo lo "táctico"/UI: nav, badges, botones,
    nombres de planes, preguntas del FAQ.
  - `Barlow` (300/400/500) → cuerpo de texto normal.
- **Patrón de sección repetido**: cada `<section>` tiene un `<div
  class="container">` (max-width 1100px) con un encabezado
  `.stag` (etiqueta pequeña en mayúsculas, dorada) + `.stitle` (título
  grande) + `.ssub` (descripción en `--muted`). Copiar ese patrón para
  cualquier sección nueva mantiene la consistencia visual gratis.
- **Animación de entrada**: `@keyframes fadeUp` para el hero; `.fi`/`.fi.visible`
  + `IntersectionObserver` (al final del `<script>`) para que la lista de
  funcionalidades aparezca en cascada al hacer scroll. Reutilizable para
  cualquier lista nueva que deba animarse al entrar en viewport.
- **Botones**: `.btn-p` (dorado, CTA primario), `.btn-s` (azul, secundario),
  `.wa` (verde, específico de WhatsApp), `.pbtn.pp`/`.pbtn.po` (planes de
  precios, destacado vs. normal).

## Estructura actual de secciones (en orden)

1. `nav` — logo + botón "Obtener acceso" (WhatsApp)
2. `.hero` — titular, subtítulo, 2 CTAs, franja de stats (5 casos gratis, ~30min, 5 documentos, app Android)
3. `.how#como-funciona` — 4 pasos numerados
4. `.features#funciones` — lista de funcionalidades + maqueta visual de "5 archivos generados" (**pendiente #15: reemplazar por captura/GIF real**)
5. `.compare` — antes (a mano) vs. después (con la app)
6. `.pricing#precios` — 4 planes: prueba gratis, semanal $12.000, mensual $35.000 (destacado), Negocio/Estación $100.000
7. `.testimonios` — 3 citas reales de policías que probaron la app
8. `.trust` — franja de 5 iconos de confianza
9. `.faq#preguntas` — acordeón `<details>` con 9 preguntas
10. `.cta` — llamado final a WhatsApp
11. `footer` — contacto + enlace a modal de términos
12. Modal de términos (`#modal`) — 3 pestañas: Términos de Uso, Privacidad, Licencias (contenido legal completo, sincronizado con lo que ofrece la app real: precios, período de gracia de 3 días, medios de pago Nequi/Llave, etc.)
13. Widget de chat flotante (`#chatToggle` / `#chatPanel`, agregado 2026-08-04) — botón dorado fijo abajo a la derecha. Abre un panel con 5 acciones: ver precios, cotizar un plan, subir comprobante de pago (con deviceId + foto), consultar el estado de un pedido por deviceId + correo, y sugerencias/contacto. Habla directo con el bot de `capturadocs-bot-pagos` vía `https://chat.capturadocs.com/webhook/landing-chat` y `.../landing-status` (mismo túnel Cloudflare que ya exponía el webhook de WhatsApp). No depende de WhatsApp: la aprobación del pago la sigue haciendo el dueño por WhatsApp como siempre, pero el cliente compra y recibe la clave sin salir de la landing. Ver `capturadocs-bot-pagos/CONTEXTO.md` sección 50 para el diseño completo del lado del bot.
    La vista "Sugerencias o contacto" (`chatEnviarContacto`, acción `contacto`) ya tiene su rama en n8n (`mensajes_contacto`, avisa al dueño por WhatsApp) — resuelto 2026-08-04 por la sesión del homelab, confirmado en vivo con un `POST` de prueba.

Todos los botones de CTA (`btn-p`, `wa`, `pbtn`, `nav-cta`) apuntan a
`https://wa.me/573503593635` — **pendiente #14**: enlazar a la app real
(`informes-ponal`) en vez de solo WhatsApp, donde tenga sentido (ej. "Probar
gratis ahora" podría ir directo a la app).

## Pendientes conocidos de la landing (backlog)

- **#14** — Enlazar botones a la app real, no solo a WhatsApp. (El widget de chat del punto 13 ya cubre la compra directa; los botones de WhatsApp existentes se dejaron intactos como canal alterno, no se tocaron.)
- **#15** — Reemplazar la maqueta falsa de `.preview` (sección Funciones) por una captura o GIF real de la app funcionando.
- **#19** — Centralizar el número de WhatsApp (hoy repetido "a mano" en ~9 lugares del HTML) en una constante de JS.
- **#20.1** — Rate limit en Cloudflare (WAF → Rate limiting rules, `chat.capturadocs.com` + `/webhook/landing-status`) — sigue sin confirmarse si se activó, requiere el dashboard. (El punto 2 de este pendiente, exigir correo, ya quedó resuelto — ver abajo.)

Resuelto: **#17** — no se migró el hosting a Vercel/Netlify, pero se
compró dominio propio (`capturadocs.com`) y se configuró como custom
domain de GitHub Pages, que resuelve el mismo problema (link sin usuario
de GitHub visible) sin cambiar de proveedor.

Resuelto: **#18 (analítica)** — se activó Cloudflare Web Analytics
(cuenta ya existente, sin crear nada nuevo) para `capturadocs.com`. El
dominio usa DNS-only (sin proxy naranja, necesario para el certificado
de GitHub Pages), así que el modo "automático" de Cloudflare no sirve —
se usó el modo manual ("Enable with JS Snippet installation"), que
inyecta un `<script type="module">` con un `data-cf-beacon` propio del
sitio. El snippet vive en el `<head>` de `index.html`, justo antes de
`</head>`.

Resuelto: **#20.2 (exigir correo, no solo deviceId, en landing-status)**
— el widget ya mandaba `email` desde que se agregó (ver abajo); el lado
de n8n (`capturadocs-bot-pagos`) se completó en la sesión del homelab,
sección 51 de su `CONTEXTO.md` — confirmado en vivo por las dos
sesiones en paralelo, sin conflicto.

Ya resueltos (ver `LECCIONES_APRENDIDAS.md` para el detalle): `rel=noopener`
en enlaces externos, imagen OG a tamaño correcto, accesibilidad del modal
de términos y sus pestañas, `theme-color`, `canonical`, `preconnect` a
Google Fonts, JSON-LD y `robots.txt`/`sitemap.xml`.

- **#18 (analítica)** — sigue pendiente, sin decidir: requiere que el
  usuario cree la cuenta (GA4/Plausible/etc.) primero.
- **#19 (número de WhatsApp)** — resuelto de forma distinta a lo previsto:
  ver `check_wa_number.py` más abajo, en vez de centralizar en JS runtime.

## Verificación del número de WhatsApp (`check_wa_number.py`)

El número `573503593635` está repetido a mano en ~9 enlaces `wa.me/` de
`index.html` (se descartó centralizarlo vía JS en tiempo de carga porque
eso vuelve el CTA principal del sitio dependiente de que JS cargue bien —
demasiado riesgo para el único camino de conversión de la landing).

En su lugar, `check_wa_number.py` (raíz del repo) escanea `index.html` y
falla si encuentra más de un número distinto en los enlaces `wa.me/`. Está
enganchado como git hook en `.githooks/pre-commit`, pero **el hook no se
activa solo** — hay que correr una vez, en cada clon del repo:

```bash
git config core.hooksPath .githooks
```

Si cambia el número de WhatsApp: reemplázalo en todo `index.html` (buscar
`573503593635`) y el hook (o `python check_wa_number.py` a mano) avisa si
quedó alguno desincronizado.

## Cómo desplegar cambios

Es GitHub Pages sirviendo directo desde la rama del repo — no hay build ni
CI. `git add` + `commit` + `push` a `main` es suficiente; el cambio queda
visible en unos minutos en la URL pública de arriba.

## Cómo usar este archivo

Al empezar una sesión nueva para tocar la landing, basta con decir "lee
`CONTEXTO.md` en `capturadocs-landing`" (o pegar este archivo) para tener
todo el sistema de diseño, la estructura y los pendientes sin releer las
~570 líneas del `index.html`. Actualiza este archivo cuando cambie algo
estructural (nueva sección, nuevo pendiente resuelto, cambio de paleta).
