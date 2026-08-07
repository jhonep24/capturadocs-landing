# Contexto de la landing — CapturaDocs Express

Este archivo es el punto de partida para modificar o mejorar la landing
(`index.html`) desde una sesión nueva, sin tener que releer todo el HTML para
entender el sistema de diseño o las decisiones ya tomadas.

📌 **Los pendientes reales viven en Vikunja, no acá** (regla acordada
2026-08-05 en la sección `homelab`, coordinadora de todos los proyectos
— ver `../homelab/CONTEXTO.md`, "Rol de esta sección: coordinación
multi-proyecto"). Proyecto **"CapturaDocs Landing"** en
`http://192.168.0.100:3456`. La sección "Pendientes conocidos" más abajo
quedó congelada como estaba antes de esa fecha — no confiar en ella como
lista viva. Esta sección SÍ es dueña de sus propias tareas en Vikunja:
márcalas hechas ahí mismo al resolverlas. Para avisar algo a otra
sección (o dejar constancia persistente de un cambio compartido), hay
dos canales: `mcp__ccd_session_mgmt__send_message` (tiempo real) y la
bitácora de Vikunja (proyecto "Coordinación" id 9, tarea 63, comentarios
prefijados `[capturadocs-landing]`) — detalle en `../homelab/CONTEXTO.md`.

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
6.5. `.downloads#descargas` (agregada 2026-08-07) — 3 tarjetas: Android (.apk firmado), Windows (.msix), iPhone (enlace a la PWA por Safari). Los binarios de Android/Windows viven como assets de un GitHub Release (`v1.6-descargas`) en **este repo** (`capturadocs-landing`, público — no en `informes-ponal`, que es privado y da 404 en descarga pública), enlazados vía `releases/latest/download/...`. Ver "Cómo regenerar los instaladores" más abajo para el proceso completo.
7. `.testimonios` — 3 citas reales de policías que probaron la app
8. `.trust` — franja de 5 iconos de confianza
9. `.faq#preguntas` — acordeón `<details>` con 9 preguntas
10. `.cta` — llamado final a WhatsApp
11. `footer` — contacto + enlace a modal de términos
12. Modal de términos (`#modal`) — 3 pestañas: Términos de Uso, Privacidad, Licencias (contenido legal completo, sincronizado con lo que ofrece la app real: precios, período de gracia de 3 días, medios de pago Nequi/Llave, etc.). Los números de WhatsApp/Nequi (`.cfg-whatsapp`/`.cfg-nequi`) y los 3 precios pagos de `.pricing` (`#price-S`/`#price-M`/`#price-N`) se refrescan solos al cargar la página, consultando `POST https://capturadocs-licencias.capturadocs.workers.dev/config-publica` (agregado 2026-08-07) — mismo dato que edita el panel admin de `informes-ponal`, así no quedan desactualizados como pasó antes (Nequi viejo `321 2016275` vs. el real `350 3593635`). Si el fetch falla, se queda con el valor ya escrito en el HTML. Ver `informes-ponal/README_TECNICO.md` sección "Configuración pública en caliente" para el lado del Worker.
13. Widget de chat flotante (`#chatToggle` / `#chatPanel`, agregado 2026-08-04) — botón dorado fijo abajo a la derecha. Abre un panel con 5 acciones: ver precios, cotizar un plan, subir comprobante de pago (con deviceId + foto), consultar el estado de un pedido por deviceId + correo, y sugerencias/contacto. Habla directo con el bot de `capturadocs-bot-pagos` vía `https://chat.capturadocs.com/webhook/landing-chat` y `.../landing-status` (mismo túnel Cloudflare que ya exponía el webhook de WhatsApp). No depende de WhatsApp: la aprobación del pago la sigue haciendo el dueño por WhatsApp como siempre, pero el cliente compra y recibe la clave sin salir de la landing. Ver `capturadocs-bot-pagos/CONTEXTO.md` sección 50 para el diseño completo del lado del bot.
    La vista "Sugerencias o contacto" (`chatEnviarContacto`, acción `contacto`) ya tiene su rama en n8n (`mensajes_contacto`, avisa al dueño por WhatsApp) — resuelto 2026-08-04 por la sesión del homelab, confirmado en vivo con un `POST` de prueba.
    **Deep-link desde la app (`informes-ponal`, agregado 2026-08-07)**: al cargar, `chatDeepLink()` lee `?view=&deviceId=&plan=&mensaje=&tipo=` de la URL — si `view` es una de las 5 vistas válidas, abre el chat directo ahí con `deviceId`/`plan`/`tipo`/`mensaje` ya prellenados. Así los botones de compra, renovación, soporte y "pedir instalador" de la app llevan directo al self-service en vez de abrir WhatsApp. Ver `licencia.js:getLandingLink()` y `ActualizacionRequerida.jsx` en `informes-ponal`, y `README_TECNICO.md` sección 11 de ese repo (v1.6.5).

Todos los botones de CTA (`btn-p`, `wa`, `pbtn`, `nav-cta`) siguen apuntando a
`https://wa.me/573503593635` — **pendiente #14**: enlazar a la app real
(`informes-ponal`) en vez de solo WhatsApp, donde tenga sentido (ej. "Probar
gratis ahora" podría ir directo a la app). El deep-link de arriba resuelve el
sentido inverso (app → landing); #14 sigue siendo landing → app.

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

## Cómo regenerar los instaladores (Android/Windows)

Cuando cambie la app (`informes-ponal`) y haya que republicar los binarios de
la sección Descargas:

**Android** (`informes-ponal/android`):
1. `npm run build && npx cap sync android` en `informes-ponal`.
2. El keystore de firma vive en `informes-ponal/android/keystore/` —
   **gitignored, no está en el repo**. Si no existe en la máquina, hay que
   generarlo de nuevo con `keytool -genkeypair` (esto invalida las
   actualizaciones para quien ya instaló el APK anterior, porque Android exige
   la misma firma para reinstalar/actualizar — evitar si es posible, hacer
   backup del `.keystore` en vez de regenerarlo).
3. Requiere **JDK 21** (no 17/20) — `capacitor.build.gradle` lo exige. Si no
   está instalado, usar la versión `.zip` portátil de Temurin en vez del
   instalador `.msi` (el `.msi` requiere admin, que esta sesión no tenía).
4. `JAVA_HOME=<ruta-jdk21> ./gradlew.bat assembleRelease` dentro de
   `informes-ponal/android` → genera `app/build/outputs/apk/release/app-release.apk`.

**Windows** (`.msix`): no usar la interfaz web de pwabuilder.com — sus
componentes son Lit/shadow-DOM y el click automatizado no siempre dispara el
handler real (visto en esta sesión). Es más confiable llamar directo a su API
pública:
```
POST https://pwabuilder-windows-docker.azurewebsites.net/msix/generatezip
Content-Type: application/json

{"url":"https://capturadocs-app.capturadocs.workers.dev/","packageId":"CapturaDocs.CapturaDocsExpress","name":"CapturaDocs Express","version":"1.6.0.0","allowSigning":false,"generateModernPackage":true,"publisher":{"displayName":"CapturaDocs","commonName":"CN=3a54a224-05dd-42aa-85bd-3f3c1478fdca"}}
```
Devuelve un `.zip` con `*.sideload.msix` + `install.ps1` + `utils/pwainstaller.exe`
— ese `.zip` completo es el que se sube al release, no solo el `.msix` suelto
(el usuario final necesita `install.ps1` para que el certificado de prueba se
instale junto con el paquete).

**Publicar**: subir los dos archivos (`CapturaDocs-Express-Android.apk`,
`CapturaDocs-Express-Windows.zip`) como assets de un nuevo GitHub Release en
**`capturadocs-landing`** (repo público) — nunca en `informes-ponal` (privado,
los links públicos dan 404 aunque el asset se suba bien, ver Falla más abajo).
`gh release create <tag> archivo1 archivo2 --repo jhonep24/capturadocs-landing`.
Los links de la landing usan `releases/latest/download/<nombre-exacto>`, así
que basta con que el nuevo release quede marcado "Latest" (por defecto, el más
reciente) — no hace falta tocar `index.html` de nuevo si los nombres de
archivo no cambian.

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
