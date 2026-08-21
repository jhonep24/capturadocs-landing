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

Landing estática (sin build, sin frameworks) para **CapturaDocs Express**,
la app de informes de captura de `informes-ponal`. Tres páginas HTML:
`index.html` (la landing principal, con toda la lógica de precios/chat/
config-publica), `seguridad.html` (agregada 2026-08-11, ver punto 14 más
abajo) y `guia.html` (agregada 2026-08-11, ver punto 15) — las dos últimas
son páginas estáticas simples, sin JS propio salvo el link de WhatsApp.
Se publica en GitHub Pages, con dominio propio:
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
3. `.how#como-funciona` — 4 pasos numerados + botón "📖 Ver la guía de uso completa →" (agregado 2026-08-11) enlazando a `guia.html`
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
14. `seguridad.html` (página nueva, 2026-08-11) — "Arquitectura de privacidad": reemplaza la promesa genérica "100% privado" por un diagrama HTML/CSS de dos columnas (`.dcol.local` / `.dcol.remote`, sin librerías externas) que muestra qué se queda 100% en el dispositivo (datos del procedimiento, generación de documentos, borradores) vs. qué sí llega a la infraestructura propia y por qué (ID de dispositivo + licencia, pedidos/comprobantes/contacto, texto anonimizado para la IA). 3 tarjetas de preguntas puntuales debajo (qué hace la IA, qué usa el sistema de licencias, quién más ve los datos de pedido). No tiene su propio `<script>` de negocio — copia solo el CSS necesario del sistema de diseño (no todo el `<style>` de `index.html`) más el snippet de `WA_NUMBER` para el link de WhatsApp del footer. Enlazada desde: nav de `index.html` no (para no saturarlo), sí desde la respuesta de la FAQ "¿Qué pasa con los datos de mis capturados?" y desde el footer ("Cómo protegemos tus datos"). El botón "Leer la Política de Privacidad →" de `seguridad.html` apunta a `index.html#privacidad`, que dispara un pequeño bloque de JS en `index.html` (justo después del listener de teclado del modal) que abre el modal directo en la pestaña Privacidad si `location.hash === '#privacidad'` — así el texto legal completo sigue viviendo en un solo lugar (el modal), sin duplicarlo en la página nueva. Agregada a `sitemap.xml`.
    - **Cuidado si se edita el diagrama**: debe reflejar EXACTAMENTE la distinción de "Categorías de datos" del punto 12 (2a datos del procedimiento vs. 2b datos de gestión de pedidos/contacto) — si se retoca uno, retocar el otro, para no volver a tener dos fuentes de verdad desalineadas (fue justo el problema que motivó el refuerzo de la política, ver "Transparencia legal" más abajo).
    - **Sección `.hashbox`** (agregada 2026-08-11), debajo de las 3 tarjetas de preguntas: aquí vive el hash SHA-256 del instalador de Windows (`#hash-win`), movido desde `#descargas` — ver nota del punto anterior de "Transparencia legal" sobre por qué se movió aquí en vez de quitarlo del todo.
15. `guia.html` (página nueva, 2026-08-11) — "Guía de uso", pedida por el usuario.
    Recibió feedback de una auditoría externa de IA sugiriendo reordenar todo en 9
    secciones tipo recorrido real; se probó esa versión pero **al usuario no le
    gustó — pidió volver a la estructura original de 6 secciones + Problemas
    comunes, complementada con el contenido bueno de la versión de 9** (no un
    revert puro). Estructura final, **6 secciones numeradas** (`.gsec`, índice
    `.toc` arriba) + Problemas comunes:
    - **1 Instalar** — Windows / Android-iPhone (deshabilitados) + tarjeta nueva
      "¿Necesito internet?" (no para diligenciar/generar; sí para
      verificar/activar licencia, actualizaciones, y usar la IA).
    - **2 Primer uso y prueba gratis** — correo, código de referido, 5 casos
      gratis + línea nueva explicando qué es el ID de dispositivo + aviso nuevo
      sobre la IA (nunca decide sola, solo sugiere; anonimización local).
    - **3 Activar tu licencia** — sin cambios.
    - **4 Diligenciar un caso y generar los documentos** — lista de pasos
      corregida a los 8 reales (`informes-ponal/src/modelos.js:STEPS`: Encabezado,
      Policías, Capturados, Víctimas, Testigos, Vehículos, Elementos Incautados,
      Hechos — antes decía mal "Encabezado, Capturados... Elementos
      incautados/Vehículos" como si fuera un solo paso), + frase nueva sobre que el
      clic en un valor del Resumen navega directo al paso a corregir
      (`onNavegar`/`onIrAlPaso` en `PasoResumen.jsx`), + tarjeta nueva "Checklist
      antes de generar" (`.gcheck`, 7 puntos).
    - **5 Dónde quedan tus documentos descargados** — sin cambios (Windows
      instalado → `Documentos\CapturaDocs`; web → Descargas del navegador;
      Android → hoja de compartir).
    - **6 Truco: imprimir el rótulo en tamaño reducido** — paso 2 corregido de
      "Archivo → Exportar → Crear PDF/XPS" a **"Archivo → Guardar como" → Tipo:
      PDF**, para que coincida con la captura real que mandó el usuario.
    - **Problemas comunes** — de 6 a **9 preguntas**: se sumaron "¿dónde encuentro
      mi ID de dispositivo?", "no puedo activar mi licencia" y "la IA no aparece o
      no funciona".
    Mismo patrón que `seguridad.html`: CSS propio recortado, sin `<script>` de
    negocio. Enlazada desde el footer de `index.html`, la FAQ "¿Cómo empiezo...?", y
    entre `guia.html`/`seguridad.html`. Agregada a `sitemap.xml`.
    - **Lección de esta ronda**: el usuario prefiere iteraciones incrementales
      sobre una estructura ya aprobada, no una reescritura completa aunque el
      contenido nuevo sea bueno — la próxima vez que se sugiera una reestructuración
      grande (por auditoría externa o no), ofrecer agregar el contenido de valor
      *dentro* de la estructura existente como primera opción, no reemplazarla.
    - **Si se agrega Android/iPhone a descargas**: actualizar la sección 1.
    - **Si cambia algo del formulario** (pasos, nombres, navegación de corrección) o
      del rótulo/carpeta de descargas: releer `modelos.js`, `PasoResumen.jsx`,
      `fpj7.js`, `descargar.js` y `electron/main.cjs` antes de tocar el texto — no
      redactar de memoria, ya pasó dos veces en esta página (rótulo y carpeta).
    - **Pendiente: capturas de pantalla reales**. El usuario mandó 5 de las 6 que se
      habían pedido (pegadas directo en el chat, no como archivos en disco — hay que
      pedirle que las guarde como archivo en la carpeta del repo para poder
      insertarlas): `guia-licencia.png` (modal "Licencia activa" con ID de
      dispositivo, código de referido y renovación — mejor que el plan original de
      solo el ícono 🎁, va en sección 8), `guia-resumen.png` (paso Resumen con los 5
      botones + "Abrir carpeta CapturaDocs" — sección 5), `guia-explorador.png`
      (Explorador en `Documentos\CapturaDocs` — sección 5), `guia-word-pdf.png`
      (Word, "Guardar como" con Tipo: PDF — sección 5, truco del rótulo),
      `guia-imprimir-escala.png` (diálogo de impresión con escala 60% — sección 5,
      truco del rótulo). **Sigue faltando**: `guia-registro.png` (pantalla de
      registro de correo, primer uso — sección 2). Todas sin datos reales de casos.

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
- ~~**#21** — Cambiar "🔒 100% privado".~~ **Resuelto 2026-08-11** — el usuario prefirió mantener el "100%" pero acotado a un hecho verificable: "100% seguros los datos de tu procedimiento" / "Se procesan en tu dispositivo. Ningún dato del caso sale de tu navegador o celular." (sección Funciones). No se tocó la franja de confianza ("Datos 100% en tu dispositivo") ni la FAQ porque ya usaban una frase igual de acotada, no la absoluta que preocupaba a la auditoría.
- ~~**#22** — Página `/seguridad` con diagrama de arquitectura de privacidad.~~ **Resuelto 2026-08-11** — ver punto 14 de la estructura de secciones más arriba.

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

{"url":"https://capturadocs-app.capturadocs.workers.dev/?origen=win-instalado","packageId":"CapturaDocs.CapturaDocsExpress","name":"CapturaDocs Express","version":"1.6.0.0","allowSigning":false,"generateModernPackage":true,"publisher":{"displayName":"CapturaDocs","commonName":"CN=3a54a224-05dd-42aa-85bd-3f3c1478fdca"}}
```
Devuelve un `.zip` con `*.sideload.msix` + `install.ps1` + `utils/pwainstaller.exe`
— ese `.zip` completo es el que se sube al release, no solo el `.msix` suelto
(el usuario final necesita `install.ps1` para que el certificado de prueba se
instale junto con el paquete).

**El `?origen=win-instalado` en la URL es obligatorio si el gate de
`informes-ponal/worker-gate.js` está activo** (`GATE_ACTIVO=true`): esa marca
es lo único que distingue al instalador oficial de alguien abriendo la URL
directo en el navegador de una PC — sin ella, el `.msix` recién instalado
mostraría la página de bloqueo en vez de la app real. Los instaladores viejos
que ya se hayan usado con éxito siguen funcionando aunque no la tengan
(el service worker ya cacheó todo localmente y no vuelve a pasar por este
Worker para lo que ya tiene en caché), pero cualquier instalación nueva o
reinstalación necesita la URL con la marca. Ver el comentario de
`worker-gate.js` para el detalle completo (cookie que siembra en la primera
petición para que el resto del bundle también pase el gate).

**Si al llamar a la API de PWABuilder falla con `500` al generar los íconos
(2026-08-13)**: no es un problema de PWABuilder — es el gate bloqueando sus
peticiones. PWABuilder lee `manifest.webmanifest` y los íconos que declara
(`pwa-192.png`, `pwa-512.png`, `pwa-maskable-512.png`) con peticiones sueltas
del lado del servidor, sin cookie ni el marcador `?origen=...`, así que el
gate se las bloquea igual que a cualquier visitante sin marca. Esas rutas ya
están en `RUTAS_SIEMPRE_PERMITIDAS` de `worker-gate.js` (junto a `/logo.png`,
`/favicon.ico`, `/apple-touch-icon.png`) — si se agregan íconos nuevos al
manifest, hay que sumarlos ahí también o la regeneración del instalador
vuelve a fallar en silencio.

**Windows — `.exe` de Electron (desde 2026-08-14, vía principal ahora)**: el
`.msix` de arriba necesita el sistema de paquetes AppX de Windows, ausente en
versiones "Lite" recortadas — ahí la instalación fallaba con un crash de
`pwainstaller.exe` sin importar el certificado. La alternativa es empaquetar
la app con Electron (código en `informes-ponal/electron/main.cjs` +
`package.json` sección `"build"`): un instalador NSIS normal, autocontenido
con su propio Chromium, que no depende de AppX en absoluto.
```bash
cd informes-ponal
npm run electron:build   # vite build && electron-builder --win
```
Genera `dist-electron/CapturaDocs Express Setup <version>.exe` (~111 MB, sin
firmar — no hay certificado de código pagado, así que Windows muestra el
aviso estándar de SmartScreen, pero a diferencia del `.msix` la instalación
en sí siempre funciona). El ID de dispositivo depende de que Electron sirva
la app siempre en el mismo puerto local (`PORT = 47821` en `main.cjs`) — si
alguna vez se cambia ese puerto, todos los usuarios pierden su deviceId al
actualizar (ver `informes-ponal/README_TECNICO.md`, Error 36).

**Publicar**: subir el `.apk` y el instalador de Windows (hoy el `.exe`, antes
el `.zip` del `.msix`) como assets de un nuevo GitHub Release en
**`capturadocs-landing`** (repo público) — nunca en `informes-ponal` (privado,
los links públicos dan 404 aunque el asset se suba bien, ver Falla más abajo).
`gh release create <tag> archivo1 archivo2 --repo jhonep24/capturadocs-landing`.
Los links de la landing usan `releases/latest/download/<nombre-exacto>`, así
que basta con que el nuevo release quede marcado "Latest" (por defecto, el más
reciente) — pero si el nombre del archivo cambia (ej. de `.zip` a `.exe`, como
pasó el 2026-08-14 con la release `v1.6.10-windows-exe`), sí hay que actualizar
el `href` en `index.html` (sección `#descargas`) al nombre nuevo. GitHub
reemplaza espacios del nombre de archivo por puntos en la URL de descarga
real (`CapturaDocs Express Setup 1.6.10.exe` → `CapturaDocs.Express.Setup.1.6.10.exe`).

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
  el usuario pidió quitarlo de ahí (2026-08-11, "no es necesario" verlo en la página
  principal), y **finalmente quedó en `seguridad.html`** (mismo día, ver `.hashbox` —
  sección "Verificación de integridad del instalador (Windows)"), no al lado del botón
  de descarga pero sí visible públicamente, con instrucciones de cómo calcularlo
  (`certutil -hashfile ... SHA256`). Hay que recalcularlo a mano cada vez que se
  publique un instalador nuevo (no hay automatización todavía).
  **El valor vive en UN solo lugar: `#hash-win` en `seguridad.html`** — que es la
  página que lo publica, así que es la única copia que puede estar equivocada de
  cara al usuario. Antes también se repetía aquí, y el 2026-08-18 se descubrió que
  las dos copias llevaban rato distintas (`6df2d48b…` aquí vs. `c92261ff…` en la
  página) — ninguna de las dos correspondía ya al `.exe` publicado. Duplicar el hash
  no daba respaldo, solo una segunda cosa que se desactualiza en silencio; para
  saber el vigente, mirar `seguridad.html` o recalcularlo del release.
- **Frase de privacidad reescrita** ("los datos de los procedimientos nunca salen del
  dispositivo...") en la FAQ, con la salvedad correcta de que la mejora de redacción con
  IA sí envía el texto de la narración (ya anonimizado) a un proveedor externo — para no
  contradecir lo que hace `anonimizar.js` en el repo `informes-ponal`.
  **Cuidado si se retoca esta frase**: no prometer "cero datos salen nunca" sin esa
  salvedad, o queda desactualizada en cuanto alguien use esa función.

### Refuerzo de la Política de Privacidad (2026-08-11)

Segunda ronda de feedback de la misma auditoría externa. Se reescribió por completo
la pestaña "Privacidad" del modal (`#content-pp`), que pasó de 9 a 12 secciones:

- **Se corrigió una imprecisión real**: la versión anterior decía "no recopila ni
  transmite datos personales a servidores externos" de forma absoluta, pero eso es
  falso para los datos de **gestión de pedidos y contacto** — nombre, correo/WhatsApp,
  ID de dispositivo y la imagen del comprobante de pago sí viajan a la infraestructura
  propia (n8n en `capturadocs-bot-pagos`, vía Cloudflare Tunnel) cuando el usuario usa
  el chat para cotizar, pagar o escribir. Ahora el punto 2 distingue explícitamente
  **(a) datos del procedimiento** (100% local, nunca sale) de **(b) datos de gestión
  de pedidos/contacto** (sí se envían y almacenan, solo para eso). Esta distinción es
  la más importante de todo el refuerzo — si se vuelve a simplificar el texto, no
  perder esta separación.
- Secciones nuevas: **"Encargados del tratamiento"** (Cloudflare como infraestructura
  técnica, proveedor de IA solo para texto ya anonimizado) y **"Dónde y cuánto tiempo
  se almacena"**.
- Sección de derechos ahora incluye **procedimiento explícito** para ejercerlos
  (contacto@capturadocs.com o WhatsApp, respuesta en máx. 15 días hábiles) en vez de
  solo enunciarlos.
- Se dejó **fuera de esta ronda**, a pedido del usuario, cambiar el texto absoluto
  "🔒 100% privado" de la sección Funciones/franja de confianza/FAQ por algo tipo
  "Procesamiento local" — sigue pendiente, ver backlog. También queda pendiente la
  página `/seguridad` con diagrama de arquitectura que sugirió la misma auditoría —
  es la pieza más grande de las 3 recomendadas, no se abordó todavía.
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

## Corrección: dónde se anonimiza el texto para la IA (2026-08-11)

El usuario detectó una contradicción real (no de tono) en el refuerzo de
privacidad recién hecho: varios textos decían que **"nuestro propio
servidor anonimiza"** el texto de la narración antes de mandarlo al
proveedor de IA — eso sugiere que el servidor llega a ver el dato real
antes de borrarlo, lo cual es falso.

**Cómo es en realidad, verificado leyendo el código (no de memoria):**
`informes-ponal/src/anonimizar.js` (función `anonimizar()`, llamada desde
`src/ia.js:promptMejorarNarracion()`) corre **en el frontend — en el
navegador o la app, o sea en el dispositivo del usuario** — reemplaza
nombres/cédulas/NUNC por marcadores (`[CAPTURADO_1]`, etc.) **antes** de
que el prompt salga del dispositivo. El Worker (`handleIA` en
`informes-ponal/worker/index.js`) solo reenvía ese prompt ya anonimizado a
Groq — nunca ve el dato real tampoco. La política de privacidad de la app
(`informes-ponal/src/politica_privacidad.md`) ya lo decía bien ("texto ya
anonimizado **localmente**"); el error estaba solo en los 4 lugares de
`capturadocs-landing` que se habían escrito la ronda anterior.

**Se corrigió** en `index.html` (política de privacidad puntos 5/7/8 y la
FAQ de "datos de mis capturados") y en `seguridad.html` (diagrama y
tarjeta "¿Qué hace la IA exactamente?") para decir explícitamente que la
anonimización ocurre **en el dispositivo del usuario**, y que ni nuestro
servidor ni el proveedor de IA llegan a ver el dato real en ningún punto
de la cadena.

**Si se vuelve a tocar este tema**: la cadena correcta es
`dispositivo del usuario (anonimiza) → nuestro Worker (solo reenvía) →
proveedor de IA (solo ve texto anonimizado)`. Ningún punto de esa cadena
excepto el primero ve el dato real.

## Corrección: contradicción legal sobre cambio de dispositivo (2026-08-11)

El usuario pidió una auditoría de consistencia entre `capturadocs-landing` e
`informes-ponal` (app), específicamente en Términos/Privacidad/Licencias.
Se encontró una **contradicción legal real, no de tono**: el modal de esta
landing (pestaña Términos §7 y pestaña Licencias §6) decía que cambiar de
dispositivo **exige comprar una licencia nueva**, mientras que la propia
FAQ pública de esta misma landing (línea "¿Puedo cambiar de celular...?")
y los documentos oficiales de la app (`terminos_condiciones.md` §7,
`politica_licencias.md` §10) decían lo contrario: **reasignación gratis
por WhatsApp, sin licencia nueva**. El modal de la landing era el que
estaba desactualizado/equivocado — se corrigió para que coincida con la
FAQ y con la app (ver también LECCIONES_APRENDIDAS.md).

De paso se verificó contra el código del Worker (`TRIAL_GIFT = 5` en
`informes-ponal/worker/index.js`) que el código de regalo da **+5**
generaciones — la landing ya lo decía bien (pestaña Licencias §1), pero
`informes-ponal/src/politica_licencias.md` §3.1 decía "hasta 10" —
corregido ahí también.

**Si se vuelve a tocar el tema de cambio de dispositivo o generaciones de
regalo**: la fuente de verdad es siempre el código (`worker/index.js` para
las constantes numéricas, `handleReasignar`/similar para el flujo de
reasignación), no lo que ya esté escrito en ningún documento — verificar
ahí antes de copiar texto de un documento a otro.

### Segunda pasada de verificación (mismo día, sin hallazgos nuevos)

El usuario pidió una revisión adicional para no dejar nada por fuera. Se
comparó cada dato numérico/legal citado en ambos repos contra su constante
real en `worker/index.js` — todo consistente, sin cambios adicionales:

| Dato | Landing | App | Constante en `worker/index.js` |
|---|---|---|---|
| Casos/generaciones gratis | 5 | 5 | `TRIAL_LIMIT=5` |
| Generaciones por código regalo | +5 | +5 | `TRIAL_GIFT=5` |
| Días de gracia | 3 | 3 | `GRACE_DAYS=3` |
| Aviso previo al vencimiento | 1 día | 1 día | `WARN_DAYS=1` |
| Bono referido (quien refiere) | +7 días | no lo menciona (sin conflicto) | `REFERIDO_DIAS_BONUS=7` |
| Precios S/M/N | $12k/$35k/$100k | $12k/$35k/$100k | `PLANES` |
| Negocio/Estación solo PC | sí | sí | `soloPc:true`, bloqueado en Android en el Worker |
| Reasignación de dispositivo | gratis | gratis | — (ya corregido arriba) |
| Versión | v1.6.10 | v1.6.10 | `package.json` de `informes-ponal` |

## Corrección: botón de chat "aparecía solo al final" en móvil (2026-08-11)

El usuario reportó que en vista de celular el widget de chat (`#chatToggle`)
no se comportaba como fijo — solo se veía al llegar al final de la página,
en vez de acompañar el scroll desde el inicio. Causa: `overflow-x:hidden`
estaba puesto en `<body>`. Es un bug conocido de Safari/iOS — cuando el
`<body>` (no el `<html>`) tiene cualquier `overflow` distinto de `visible`,
los descendientes `position:fixed` (el botón del chat, y también `nav`)
pueden dejar de fijarse al viewport y renderizarse en su posición normal
del flujo del documento — que para `#chatToggle`/`#chatPanel` es justo al
final del `<body>` en el HTML fuente, coincidiendo exactamente con el
síntoma reportado.

**Arreglo**: mover `overflow-x:hidden` de `body` a `html` en ambos
archivos (`index.html` y `seguridad.html`) — sigue sin haber scroll
horizontal, pero ya no rompe `position:fixed` en el body. **Si se agrega
overflow (de cualquier tipo) a `body` en el futuro, revisar primero que no
rompa el chat ni el `nav`** (ambos son `position:fixed`, hijos directos de
`body`) — el fix correcto casi siempre es ponerlo en `html`, no en `body`.
No se pudo reproducir visualmente en el navegador de pruebas (Chromium no
tiene este bug de WebKit), así que quedó pendiente que el usuario confirme
en su celular real tras el deploy.

**Segundo hallazgo, este sí visible y reproducido con capturas**: la fila
de links del footer (`<div style="display:flex;gap:20px">`, el bloque con
correo/WhatsApp/"Cómo protegemos tus datos"/Términos) no tenía
`flex-wrap`. Con 4 links ahí (creció a 4 cuando se agregó "Cómo protegemos
tus datos" el 2026-08-11), en pantallas angostas el texto se salía del
viewport por la derecha y quedaba cortado — eso era lo que se veía "mal al
final". Arreglado agregando `flex-wrap:wrap;justify-content:center` a ese
div (mismo fix en `index.html` y `seguridad.html`), verificado con
`getBoundingClientRect()` en 375px de ancho: el link más largo ahora
termina en 310px, dentro del viewport.

## Corrección: dónde guarda los documentos la app de Windows (2026-08-11)

La primera versión de `guia.html` (sección 5, "Dónde quedan tus documentos")
decía que en Windows los documentos caían en la carpeta **Descargas** del
navegador. El usuario lo corrigió: **desde que la app de Windows es
Electron (no una PWA en el navegador), todo se guarda automáticamente en
`Documentos\CapturaDocs`** — carpeta que la propia app crea la primera vez.
Verificado leyendo `informes-ponal/electron/main.cjs`:

- `ventana.webContents.session.on("will-download", ...)` intercepta toda
  descarga del renderer y la redirige con `item.setSavePath(...)` a
  `carpetaCapturaDocs()` = `path.join(app.getPath("documents"), "CapturaDocs")`.
  Nunca se pregunta "guardar como".
- Si el nombre ya existe, `nombreDisponible()` agrega `(1)`, `(2)`... —
  nunca sobrescribe.
- Hay un botón dedicado **"Abrir carpeta CapturaDocs"** en el paso Resumen
  (`PasoResumen.jsx`, visible solo si `window.electronAPI` existe) que abre
  esa carpeta en el Explorador vía `ipcMain.handle("abrir-descargas", ...)`.

**Esto NO aplica si alguien usa la app dentro de un navegador sin instalar
el programa** (la opción "web, cualquier navegador" que también existe,
ver `politica_licencias.md` — Negocio/Estación, por ejemplo, se activa solo
en esa modalidad web) — ahí sí se comporta como una descarga normal, a la
carpeta Descargas del navegador. El propio código de `PasoResumen.jsx`
distingue los dos casos con `window.electronAPI ? <botón> : <texto que dice
"tu carpeta de Descargas de Windows">`.

**Si se vuelve a describir dónde se guardan los documentos, en cualquier
doc**: la respuesta depende de si es la app instalada (Electron →
`Documentos\CapturaDocs`) o la versión web en navegador (→ Descargas del
navegador) — no asumir que ambas se comportan igual. Verificar contra
`electron/main.cjs` y `PasoResumen.jsx`, no redactar de memoria.

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
