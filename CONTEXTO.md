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

1. `nav` — logo + botón "Obtener acceso" → `#descargas` (ya NO abre WhatsApp directo, ver nota de CTAs más abajo)
2. `.hero` — titular, subtítulo, 2 CTAs (Probar gratis → `#descargas`; Ver cómo funciona → `#como-funciona`), franja de stats (5 casos gratis, ~30min, 5 documentos, app instalable)
3. `.how#como-funciona` — 4 pasos numerados
4. `.features#funciones` — lista de funcionalidades + maqueta visual de "5 archivos generados" (**pendiente #15: reemplazar por captura/GIF real**)
5. `.compare` — antes (a mano) vs. después (con la app)
6. `.pricing#precios` — 4 planes: prueba gratis (→ app), semanal/mensual/Negocio (→ chat en "Cotizar" con el plan preseleccionado, `abrirChatEnVista('cotizar', plan)`). Los 3 precios pagos (`#price-S`/`#price-M`/`#price-N`) se sincronizan solos, ver punto 12.
6.5. `.downloads#descargas` (agregada 2026-08-07) — 3 tarjetas con íconos SVG (no emoji) de Android/Windows/Apple. **Android e iPhone deshabilitados temporalmente** (2026-08-08, pedido del usuario, motivo no técnico) — quedan visibles con `<span class="pbtn po dlbtn-disabled">Próximamente</span>` en vez del link real; **solo Windows sigue activo**. El binario de Windows vive como asset de un GitHub Release (`v1.6-descargas`) en **este repo** (`capturadocs-landing`, público — no en `informes-ponal`, que es privado y da 404 en descarga pública), enlazado vía `releases/latest/download/...`. Ver "Cómo regenerar los instaladores" más abajo para el proceso completo (sigue vigente para cuando se reactiven Android/iPhone).
7. `.testimonios` — 3 citas reales de policías que probaron la app
8. `.trust` — franja de 5 iconos de confianza
8.5. `#referidos` (rediseñada 2026-08-10) — programa de referidos: título "Tú recomiendas, los dos ganan." + 3 pasos numerados en tarjetas (`.refgrid`/`.refcard`, con `.refarrow` conectando, se ocultan en móvil) — compartir código → el referido activa y gana 7 días → el que refiere gana 7 días (tarjeta destacada `.refcard-reward`). Antes era 3 `.tcard` genéricas con el eslogan "Comparte tu código, ganen los dos" (informal, no gustó). CTA "Preguntar cómo funciona" abre el chat en "libre". Sigue sin precio/reglas nuevas — solo texto y diseño, la mecánica (código `REF-XXXXXXXX`, +7 días c/u) vive en `informes-ponal` sin cambios.
9. `.faq#preguntas` — acordeón `<details>` con 9 preguntas. El botón "¿Tienes otra pregunta?" abre el chat en "Contacto" (`abrirChatEnVista('contacto')`), ya no WhatsApp directo.
10. `.cta` — llamado final → `#descargas` (antes abría WhatsApp)
10.5. `.ads-promo` (agregada 2026-08-08) — sección "Anúnciate con nosotros", entre el CTA principal y el footer. Promociona el espacio publicitario que ya existe dentro de `informes-ponal` (`BannerPublicidad.jsx`, banners imagen+link gestionados a mano desde el panel admin, visibles solo a usuarios sin licencia paga — motor ya existía, faltaba cómo conseguir anunciantes). Sin precio fijo todavía (a definir); el CTA "Quiero anunciarme →" abre el chat en "Contacto" con el tipo `publicidad` preseleccionado (nueva opción en el `<select id="chat-contacto-tipo">`, junto a sugerencia/problema/otro). Diseño con ícono en badge dorado + gradiente + chips de beneficios, para no verse "simple" al lado del resto de la página.
11. `footer` — logo/tagline/copyright agrupados en una columna (agosto 2026, antes eran 4 elementos sueltos en `space-between` que se veían desordenados) + columna de links de contacto (correo, WhatsApp — este sí sigue siendo un link directo a WhatsApp, es información de contacto, no un CTA de conversión) + enlace a modal de términos.
12. Modal de términos (`#modal`) — 3 pestañas: Términos de Uso, Privacidad, Licencias. Los números de WhatsApp/Nequi (`.cfg-whatsapp`/`.cfg-nequi`) y los 3 precios pagos de `.pricing` se refrescan solos al cargar la página, consultando `POST https://capturadocs-licencias.capturadocs.workers.dev/config-publica` (agregado 2026-08-07) — mismo dato que edita el panel admin de `informes-ponal`, así no quedan desactualizados como pasó antes (Nequi viejo `321 2016275` vs. el real `350 3593635`). Si el fetch falla, se queda con el valor ya escrito en el HTML. Ver `informes-ponal/README_TECNICO.md` sección "Configuración pública en caliente" para el lado del Worker.
13. Widget de chat flotante (`#chatToggle` / `#chatPanel`, agregado 2026-08-04, ampliado varias veces) — botón dorado fijo abajo a la derecha. Menú con **6 acciones**: ver precios, cotizar un plan, subir comprobante de pago, consultar el estado de un pedido, **escríbenos (chat libre, agregada 2026-08-08)**, y sugerencias/contacto (con la nueva opción "Quiero anunciarme en la app"). "Contáctanos por WhatsApp" (renombrado desde "Prefiero WhatsApp") queda como último ítem, último recurso — no incentivado. Habla directo con `capturadocs-bot-pagos` vía `https://chat.capturadocs.com/webhook/landing-chat`, `.../landing-status` y `.../landing-mensajes`.
    - **Comprobante de pago**: exige `sessionId` (UUID generado por `getSessionId()`, persistido en `localStorage` como `cd_session_id`) y `plan` (S/M/N, selector agregado 2026-08-08) además de `deviceId`+`imagenBase64` — cambio de contrato del backend que rompió este flujo en producción brevemente el 2026-08-08, ver `LECCIONES_APRENDIDAS.md`.
    - **Chat libre** (`chat-view-libre`, `chatLibreEnviar()`): asistente de FAQ con respaldo de IA, workflow propio separado del de pagos (desde 2026-08-08, antes vivía dentro de `landing-chat`). `POST https://chat.capturadocs.com/webhook/landing-faq {sessionId, texto}` responde **síncrono** con `{ok:true, respuesta:"..."}` en la misma llamada (normalmente 2-3s; hasta ~40-70s en el caso raro de fallback — hay un aviso a los 6s de espera). La ruta vieja (`landing-chat {accion:"mensaje"}`) ya no funciona, responde `410`. No usa polling (`landing-mensajes` sigue existiendo pero no hace falta para esto).
    - La vista "Sugerencias o contacto" (`chatEnviarContacto`, acción `contacto`) llega a una Data Table en el bot (`mensajes_contacto`) y avisa al dueño por WhatsApp — ver `capturadocs-bot-pagos/CONTEXTO.md` sección 52.
    - **Deep-link desde la app** (`informes-ponal`, agregado 2026-08-07): al cargar, `chatDeepLink()` lee `?view=&deviceId=&plan=&mensaje=&tipo=` de la URL y abre el chat directo ahí. Ver `licencia.js:getLandingLink()` en `informes-ponal`.
    - **Seguridad**: toda respuesta del backend que se inserta en el DOM pasa por `escapeHtml()` antes de ir a `innerHTML` (agregado 2026-08-08 tras una revisión de seguridad — antes 4 puntos insertaban `data.mensaje`/`data.pedido.estado`/`data.pedidoId`/`data.plan` sin escapar).

**CTAs ya NO apuntan a WhatsApp por defecto** (cambiado 2026-08-08, pedido
explícito: *"wsp va a ser el último lugar... no quiero incentivar el uso de
wsp"*). Nav/hero/CTA final → `#descargas`; planes pagos → chat en "Cotizar";
FAQ → chat en "Contacto". El único `wa.me` con esa etiqueta que sobrevive es
el ítem del propio menú del chat ("Contáctanos por WhatsApp", último ítem) y
el link de contacto del footer (información, no CTA). El pendiente histórico
**#14 (enlazar botones a la app real, no solo WhatsApp) quedó resuelto** con
esto — se deja la entrada en el backlog de abajo tachada por trazabilidad.

## Pendientes conocidos de la landing (backlog)

- ~~**#14** — Enlazar botones a la app real, no solo a WhatsApp.~~ **Resuelto 2026-08-08** — ver nota de CTAs arriba.
- **#15** — Reemplazar la maqueta falsa de `.preview` (sección Funciones) por una captura o GIF real de la app funcionando.
- ~~**#19** — Centralizar el número de WhatsApp en una constante de JS.~~ **Resuelto 2026-08-11** — quedan solo 2 enlaces reales (footer y menú del chat, `class="wa-link"`), ambos sin `href` fijo: se completan en runtime desde `const WA_NUMBER` (ver `<script>` principal). `check_wa_number.py` se actualizó para validar esa constante en vez de buscar `wa.me/<numero>` hardcodeado en el HTML.
- **Reactivar descargas de Android e iPhone** cuando corresponda (hoy deshabilitadas a propósito, ver punto 6.5) — el código/binarios siguen listos, solo hay que quitar el estado `dlbtn-disabled`.
- **Definir precio del espacio publicitario** (punto 10.5): la sección ya está, pero cotiza por chat en vez de mostrar un precio fijo. (La sección de referidos, punto 8.5, ya no está pendiente — se rediseñó el 2026-08-10; la mecánica del programa en sí, `REF-XXXXXXXX`/+7 días, vive en `informes-ponal` sin cambios de este lado.)
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

## Chat de la landing — cotizador (2026-08-10)

La vista `chat-view-cotizar` del panel de chat (`chatToggle` /
`chatPanel`) ahora pide **ID de dispositivo** (obligatorio) y
**código de referido** (opcional) además del plan. `chatCotizar()`
llama a `POST {CHAT_API}/landing-chat` con `{accion:'cotizar', plan,
deviceId, codigoReferido}` — el backend (workflow `Bot de pagos` en
`capturadocs-bot-pagos`, acción `cotizar`) responde `diasActivos`
(licencia actual, si tiene), `diasPlan`, `bonoReferido` (7 si el
código es válido) y `diasTotal`, más `referidoError` si el código no
se pudo aplicar. El resultado se muestra como texto y agrega un
botón "✅ Ya pagué, subir comprobante" que salta a `chat-view-
comprobante` con `chat-comp-deviceid`/`chat-comp-plan` ya rellenos
con lo que el visitante acaba de cotizar — no hace falta que vuelva a
escribir el ID. Lógica de negocio (cálculo de días, validación del
código contra el Worker) vive del lado de n8n, no en el HTML — ver
`capturadocs-bot-pagos/CONTEXTO.md` (sección "Cotizador de la landing").

## Transparencia legal y validación del resumen (2026-08-10)

A raíz de feedback de una auditoría externa de IA sobre la landing, se agregó:
- **Responsable identificado**: Johnn Eduardo Pacanchique Martínez, persona natural,
  en las pestañas Términos y Privacidad del modal (`#modal`) — sin NIT, no tiene
  negocio registrado.
- **Cláusula "9. Soporte técnico"** y **"10. Versión e historial de actualizaciones"**
  (v1.6.10) en la pestaña Términos.
- **Hash SHA-256 del instalador de Windows**, calculado descargando el `.zip` real del
  último release. Se publicó junto al botón de descarga en `#descargas` el 2026-08-10,
  pero el usuario pidió quitarlo de ahí (2026-08-11, "no es necesario" verlo en la
  página principal) — queda solo documentado aquí. Hay que recalcularlo a mano cada
  vez que se publique un instalador nuevo (no hay automatización todavía):
  - v1.6.10: `6df2d48bf78e5c8b6b7db48672d40b3c18a7d4c9b4a394e755789f58d3914f98`
- **Frase de privacidad reescrita** ("los datos de los procedimientos nunca salen del
  dispositivo...") en la FAQ, con la salvedad correcta de que la mejora de redacción con
  IA sí envía el texto de la narración (ya anonimizado) a un proveedor externo — para no
  contradecir lo que hace `anonimizar.js` en el repo `informes-ponal`.
  **Cuidado si se retoca esta frase**: no prometer "cero datos salen nunca" sin esa
  salvedad, o queda desactualizada en cuanto alguien use esa función.
- **Aclaración de que la IA de redacción nunca aplica un cambio por su cuenta**: solo
  sugiere, y el usuario decide con el botón "Usar" — verificado leyendo
  `informes-ponal/src/components/pasos/PasoHechos.jsx` antes de escribirlo, no de
  memoria.
- **Nueva tarjeta de función + maqueta del panel "preview"** (sección `#funciones`).
  **Ojo, esto se corrigió el mismo día**: la primera versión inventaba un detector
  automático de inconsistencias entre documentos (🟢/🔴 comparando edad vs. fecha de
  nacimiento, hora vs. otro documento) que **no existe** en el código real — el usuario
  lo notó y lo señaló. `PasoResumen.jsx` solo marca en rojo los campos obligatorios que
  faltan (componente `Campo` con `req`) y dos campos con recordatorio permanente de
  revisar dos veces (prop `alerta`: `fecha_captura` y `fecha_fiscal`), sin comparar
  valores entre sí. La tarjeta y la maqueta quedaron corregidas para describir
  exactamente eso — validación de completitud + recordatorio de fechas, no un motor de
  consistencia automática. Si se vuelve a tocar esta sección, verificar primero contra
  `PasoResumen.jsx` (buscar `alerta` y `req`), no redactar de memoria.

El mismo bloque de cambios se replicó en los documentos legales de la app
(`informes-ponal/src/terminos_condiciones.md`, `politica_privacidad.md`,
`politica_licencias.md`) y en el modal "Acerca de" (`ModalAcercaDe.jsx`) — ver
`informes-ponal/README_TECNICO.md` sección 11 (#12). De paso se corrigió ahí un Nequi
desactualizado que había quedado en `politica_licencias.md`.

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
