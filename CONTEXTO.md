# Contexto de la landing — CapturaDocs Express

Este archivo es el punto de partida para modificar o mejorar la landing
(`index.html`) desde una sesión nueva, sin tener que releer todo el HTML para
entender el sistema de diseño o las decisiones ya tomadas.

## Qué es este repo

Landing estática de una sola página (`index.html`, sin build, sin
frameworks) para **CapturaDocs Express**, la app de informes de captura de
`informes-ponal`. Se publica en GitHub Pages:
https://jhonep24.github.io/capturadocs-landing/

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

Todos los botones de CTA (`btn-p`, `wa`, `pbtn`, `nav-cta`) apuntan a
`https://wa.me/573503593635` — **pendiente #14**: enlazar a la app real
(`informes-ponal`) en vez de solo WhatsApp, donde tenga sentido (ej. "Probar
gratis ahora" podría ir directo a la app).

## Pendientes conocidos de la landing (backlog)

- **#14** — Enlazar botones a la app real, no solo a WhatsApp.
- **#15** — Reemplazar la maqueta falsa de `.preview` (sección Funciones) por una captura o GIF real de la app funcionando.
- **#17** — Mover el hosting de GitHub Pages a Vercel/Netlify para tener un link sin depender de un usuario de GitHub visible en la URL.
- **#18** — Analítica (Google Analytics/Plausible) para medir cuántas visitas llegan a WhatsApp vs. rebotan.
- **#19** — Centralizar el número de WhatsApp (hoy repetido "a mano" en ~9 lugares del HTML) en una constante de JS.

Ya resueltos (ver `LECCIONES_APRENDIDAS.md` para el detalle): `rel=noopener`
en enlaces externos, imagen OG a tamaño correcto, accesibilidad del modal
de términos y sus pestañas, `theme-color`, `canonical`, `preconnect` a
Google Fonts, JSON-LD y `robots.txt`/`sitemap.xml`.

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
