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

🗺️ **Índice de detalle (movido a `ref/` el 2026-10-27 sin perder contenido)**

| Necesitas... | Ve a |
|---|---|
| Regenerar instaladores, publicar un `.exe` nuevo (hash), verificar el WhatsApp | [`ref/OPERACION.md`](ref/OPERACION.md) |
| Chat cotizador, transparencia legal, privacidad y correcciones de agosto | [`ref/BITACORA_AGO.md`](ref/BITACORA_AGO.md) |
| Ventas solo escritorio (provisional), APK/iPhone, versiones 1.10–1.13.4 publicadas, íconos, videos, guía PDF | [`ref/BITACORA_SEP_OCT.md`](ref/BITACORA_SEP_OCT.md) |
| Por qué se hizo cada cosa y qué salió mal | `LECCIONES_APRENDIDAS.md` (empieza con índice por fecha) |

> Nota de estructura (2026-10-27): la lista de secciones de abajo no menciona `.dispositivos#dispositivos` (laptop + 2 teléfonos con capturas reales, va entre `.features` y `.compare`); está descrita en «Rediseño … dirección B».

## Qué es este repo

Landing estática (sin build, sin frameworks) para **CapturaDocs Express**,
la app de documentación policial de `informes-ponal`.

⚠️ **La landing describe un producto más chico del que existe hoy**, y la
distancia creció entre el 11 y el 28 de septiembre de 2026. Desde la v1.8.0 la
app sirve **dos procesos** —captura en flagrancia y primer respondiente
(FPJ-4)— y además incorporó bicicletas incautadas, atribución de elementos a
cualquier persona del caso y reutilización de direcciones y personas. La
landing sigue hablando solo de flagrancia, nombrando 4 documentos y anunciando
la v1.6.10. El detalle de todo eso vive en `../informes-ponal/README.md`
(novedades) y `../informes-ponal/PLAN-FPJ4.md` (el proceso nuevo) — son los
dueños de ese hecho, no copiarlo acá. El trabajo de actualizar `index.html`,
`guia.html` y la versión está en Vikunja, **CapturaDocs Landing #126**, y
depende de que se publique el instalador de la 1.8.0.

⚠️ **El hash de `seguridad.html` se recalcula del archivo que se suba.** El
instalador de la 1.8.0 se ha recompilado varias veces, así que cualquier hash
anotado en otra parte puede estar vencido. Publicar uno viejo hace que el
cliente que siga los pasos de verificación concluya que el instalador fue
alterado — ya pasó una vez (ver punto 14). Tres páginas HTML:
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
6. `.pricing#precios` — 4 planes (restaurados 2026-10-17): prueba gratis (→ `#descargas`), semanal/mensual/Negocio (→ chat en "Cotizar" con el plan preseleccionado, `abrirChatEnVista('cotizar', plan)`). Los 3 precios pagos (`#price-S`/`#price-M`/`#price-N`) se sincronizan solos, ver punto 12.
6.5. `.downloads#descargas` (agregada 2026-08-07) — 3 tarjetas con íconos SVG (no emoji) de Android/Windows/Apple. **Las tres descargas (Windows, Android, iPhone) están activas** desde 2026-10-17 (estuvieron deshabilitadas con "Próximamente" desde 2026-08-08; ver "Vuelven las ventas normales"). La clase `.dlbtn-disabled` queda en el CSS por si hay que deshabilitar otra vez. El binario de Windows vive como asset de un GitHub Release (`v1.6-descargas`) en **este repo** (`capturadocs-landing`, público — no en `informes-ponal`, que es privado y da 404 en descarga pública), enlazado vía `releases/latest/download/...`. Ver "Cómo regenerar los instaladores" más abajo para el proceso completo (sigue vigente).
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
15. `guia.html` (página nueva, 2026-08-11) — "Guía de uso", pedida por el usuario. *(Desde 2026-10-16 admite un video por sección clave — ver "Videos tutoriales en `guia.html`" más abajo.)*
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

## Pendientes y decisiones vigentes

La lista viva está en **Vikunja, proyecto «CapturaDocs Landing» (id 5)**; abiertos al 2026-10-27: #10 confirmar rate limit de Cloudflare en `landing-status`, #12 reemplazar la maqueta de «Funciones» (`.preview`) por captura/GIF real, #39-#41 prueba social / urgencia / ROI en el copy, #126 landing y guía para el primer respondiente (FPJ-4), #163 grabar los 4 videos de la guía. La guía en PDF está hecha pero **sin publicar** (ver «Guía paso a paso en PDF» en `ref/BITACORA_SEP_OCT.md`). El texto antiguo de pendientes quedó congelado en `ref/BITACORA_AGO.md`.

**Decisión vigente (2026-08-11): el precio del espacio publicitario ($150.000 COP/mes, precio de arranque) NO debe aparecer escrito en la landing.** Solo se da cuando alguien pide cotizar por el chat: el botón «Quiero anunciarme →» abre el chat en «Contacto». No hay automatización que lo aplique (a diferencia de los precios de licencias, que viven en `PLANES` del Worker); si algún día se automatiza, usar ese valor salvo que el usuario indique otro. La mecánica de referidos (`REF-XXXXXXXX`, +7 días) vive en `informes-ponal`.

## Vuelven las ventas normales (2026-10-17)

Pedido del dueño: *"ajusta ya las ventas normales, ya la apk está funcionando
full"*. Las dos restricciones provisionales ("Venta solo para escritorio" y "solo
se vende Estación", ver arriba) existían porque el celular no generaba documentos;
con el APK completo (y la PWA de iPhone completa) dejaron de tener razón de ser.

**Eran DOS mitades y hubo que mover las dos, en este orden:**

1. **Worker** (`informes-ponal/worker/index.js`): `PLANES_EN_VENTA` volvió de
   `["N"]` a `["S","M","N"]` (commit `fad5856` de `informes-ponal`). Esa constante
   filtra lo que publica `/config-publica` y lo que recibe el **bot** de cotización
   por `/admin/config-consultar`. **Un push a `main` que toque `worker/**` lo
   despliega solo** (GitHub Actions `deploy-worker.yml`); no hace falta `wrangler`.
   Verificado en vivo: `/config-publica` devuelve `{"S":12000,"M":35000,"N":100000}`.
   La prueba `test:worker` dejó de fijar *cuáles* planes están en venta: verifica
   que el bot reciba exactamente los de `PLANES_EN_VENTA`.
2. **Landing** (este repo): se restauraron las tarjetas **Semanal** y **Mensual**
   (rejilla otra vez de 4 columnas), las dos listas del chat (cotizar y comprobante),
   las ofertas de `schema.org` (4: gratis, semanal, mensual, Negocio/Estación), y se
   **eliminó** el filtro `CHAT_PLANES_EN_VENTA` de "Ver precios". Los textos que
   comparaban con un plan que "ya no se ofrecía" volvieron: la IA es **exclusiva de
   Mensual y Negocio/Estación** (tarjeta de funciones, FAQ y `guia.html`), y la FAQ de
   Estación otra vez dice que "cuesta más que la mensual normal".

**Decisiones que conviene no perder:**

- **"Empezar gratis" ahora va a `#descargas`**, no directo al `.exe`. Con tres
  plataformas, mandar a todos al instalador de Windows no tiene sentido; la sección
  de descargas deja escoger. Los textos de plataforma de las tarjetas dicen **"Windows,
  Android e iPhone"** (antes "Para computador con Windows").
- **Negocio/Estación sigue siendo solo para computador.** No lo cambió esta reversión:
  es una regla del Worker (`soloPc: true` en `PLANES`; no se emite ni se reasigna a un
  dispositivo Android) y la tarjeta lo sigue diciendo ("Solo para computador").
- **Los precios de las tarjetas son el respaldo estático** ($12.000 / $35.000 /
  $100.000); `sincronizarConfigPublica()` los reemplaza por lo que devuelva el
  Worker. Mientras el Worker solo publicaba N, S y M se quedaban con el valor del HTML
  (la función ignora un plan que no venga en la respuesta).
- **Los términos y la política de licencias nunca se tocaron** durante el retiro (a
  propósito, por los clientes que ya habían pagado), así que no hubo que restaurar
  nada legal.
- **La palanca queda armada.** Para retirar otro plan sin borrarlo: quitarlo de
  `PLANES_EN_VENTA` en el Worker (y, si se quiere, de la landing). No borra nada:
  quien ya lo compró conserva su licencia.

> ⚠️ **REVERTIDO el 2026-10-22 (pedido del dueño, "mientras definimos todo"):** la landing
> volvió al estado del commit `02bec43` (emojis originales, sin `icons.svg`, sin escena de
> scroll). Todo lo descrito en las dos secciones siguientes **ya no está publicado**, pero
> sigue en el historial de git (`95d7cef`, `dbfc2b3`, `b8519e1`) para recuperarlo. El dueño
> está investigando skills de diseño y quiere un **rediseño respetando los colores** (azul
> marino + dorado, representan la app). Rechazó la propuesta "papel/azul". Pendiente: definir
> la dirección con él antes de tocar nada.

## Rediseño de la landing, dirección "B" (2026-10-24 a 26) — PUBLICADO por pasos

El dueño eligió la dirección B (cinematográfica) de Superdesign, **manteniendo colores y
tipografías** (son la marca de la app). Se hace por pasos, con vista previa privada en un
Artifact de claude.ai y aprobación antes de cada `git push`. Ya publicado:
1. **Base** (`41730de`): portada alineada a la izquierda con **hojas de documento flotando en
   un `<canvas>`** (fondo "documentos en vuelo", tenue; se pausa fuera de pantalla y en
   movimiento reducido), emojis → íconos Lucide (`icons.svg`, `<svg class="ic"><use href="icons.svg#i-…">`),
   cortes diagonales (`clip-path`) en `.features` y `.trust`.
2. **Mockups** (`e412a46`): sección `#dispositivos` con laptop + 2 teléfonos CSS y capturas
   reales de la app (`img/app-pc.jpg`, `app-movil-1/2.jpg`).
3. **Validación real + testimonios + confianza** (`ba12d3e`): captura real del Resumen
   (`img/app-validacion.jpg`), testimonios en franjas anchas, `.trust` en banda de 5 columnas.
- Las capturas salen de `guia-pdf/` (mismo generador de la guía, con `resaltar()` neutralizado
  para quitar los círculos rojos); datos **inventados**. Si cambia la app, regenerarlas.
- Superdesign: CLI `npx @superdesign/cli`, cuenta "Personal" ya con login; proyecto y borradores
  en su lienzo. Generar imágenes gasta créditos (saldo figuraba negativo): **no se usó**; el fondo
  se hizo en código. `.superdesign/` está en `.gitignore`.
- Plugins instalados por el dueño: `frontend-design`, `superdesign`.
- **Guía de uso con capturas reales** (2026-10-26): 11 capturas de la app de Windows en `img/guia-*.jpg`
  (términos, correo, configuración inicial, licencia, inicio, encabezado, capturados, elementos, hechos,
  resumen, generar), con ampliación al tocar (`.lightbox`). Fondos variados por sección en la landing y
  mismo estilo (íconos + portada con hojas) en `guia.html` y `seguridad.html`.
- **Checklist "antes de generar"** reescrito para reflejar lo que la app SÍ hace (Resumen con "Falta N",
  campos en rojo que llevan al paso, fechas "Revisar dos veces") y lo que solo confirma la persona (cédula,
  narración, elementos). Está igual en `guia.html` y en el PDF (`guia-print.tpl.html`); si se toca uno, tocar el otro.
- **Reglas de estilo que quedaron (2026-10-26/27), para no romperlas al tocar la landing:**
  - Paleta fija: azul marino + dorado (+ azul `#2e7fff` en botones secundarios). El verde solo
    para WhatsApp (botón del chat). Rojo solo en "Antes, a mano" de la comparación.
  - Botón principal = dorado sólido; secundario = **contorno dorado** (`.pbtn.po`, `.nav-cta`);
    el botón de la barra superior ya NO es verde. Palomitas de listas en dorado.
  - Íconos: siempre Lucide en medallón dorado con brillo (`.step-i .fi-icon .ti-ic .refico .ads-promo-icon .dlicon`); nada de emojis.
  - Cada sección con fondo propio (azul rey / ámbar / navy con resplandor) y **cortes diagonales**
    (`clip-path` alternando) en features, comparación, descargas, testimonios, trust y cierre. Los
    cortes solo se ven si la sección vecina tiene un tono distinto: no igualar fondos contiguos.
  - Descargas en celular: tarjeta apilada (ícono grande arriba, botón abajo). Se probó una versión
    compacta y el dueño prefirió la apilada. Botones de Android/iPhone en dorado.
  - Revisión en celular (375 px) hecha el 2026-10-26: sin desbordes; barra superior en una fila,
    enlaces del pie ≥ 44 px.
- **Método reutilizable para otras páginas:** `Documents\claude\guia-web\GUIA_PAGINAS_WEB.md` (flujo, herramientas, plantillas, checklist). El porqué de cada cambio del rediseño está en `LECCIONES_APRENDIDAS.md` (entradas de oct-2026).
- **Chat con mascota (2026-10-27):** el botón flotante es un **agente 3D saludando** (`img/agente-chat.jpg`,
  generado con Superdesign/Seedream, 6 créditos, con bigote por decisión del dueño), mano fija en la gorra;
  solo flota suave y se acerca al pasar el mouse. Globito "¡A la orden!" una vez por visita (`sessionStorage cd-saludo`).
  Menú del chat con íconos dorados en medallón y texto blanco; **cada sección tiene su título + "← Menú"**
  (`.chat-vhdr`). La imagen es un render de IA sin insignias reales (la web dice que NO es oficial de la Policía).
  Antes se probaron robots y agentes en SVG propio y no gustaron ("muy básicos"): para personajes, usar generación de imagen.
- **Sección "Documentos oficiales" (2026-10-28, `#documentos`):** visor con pestañas FPJ-5/6/7/8, hoja en
  perspectiva con otras detrás, 3 puntos numerados por documento (leyenda que los resalta) y ampliación al tocar.
  Imágenes `img/doc-fpj*.jpg` = documentos REALES que genera la app con un caso inventado. No afirma que la
  Fiscalía los acepte (la FAQ dice que depende de la autoridad). Cómo regenerarlas: `guia-pdf/generador/e2e-guia/documentos.spec.js`
  (ver `LECCIONES_APRENDIDAS.md`, entrada 2026-10-28). Los datos de las 4 hojas deben coincidir (mismo capturado y policía).
- **Recorte para celular (2026-10-28):** la página bajó de ~17.800 a ~15.500 px en 375 px. Se quitó la función duplicada
  "En el computador y en la calle" (ya la cuenta `#dispositivos`) y se compactó con un bloque `@media (max-width:700px)` al
  final del CSS ("Celular: la misma información, menos alto"): pasos y referidos con ícono a la izquierda, pestañas de
  documentos en 2 columnas, menos relleno. Enlaces de texto con zona táctil de 44 px (`.fa a`, `.docs-nota a`).
  Candidatos a recortar más (decisión del dueño, no hechos): anuncios (`.ads-promo`), banda `.trust`, mockups `#dispositivos`,
  funciones desplegables en celular.
- Pendiente de B (opcional): más cortes diagonales, ilustraciones por función.
- La vista previa se arma inlineando CSS/imágenes/icons en un solo HTML y publicándolo como
  Artifact; el chat/precios en vivo no funcionan ahí (solo en el sitio real).

## 1.13.7 publicada (2026-10-29)

Lote de ajustes a documentos y captura (todo en `informes-ponal`):

- **NUNC en Times New Roman negrilla 12** en los 5 documentos: FPJ-4, FPJ-5,
  FPJ-6 (derechos), rótulo (FPJ-7) y acta de incautación.
- **Cédulas con puntos de miles** en los documentos; además la **cédula del
  policía** (bloque de firma del FPJ-5 y rótulo) y la **cédula del rótulo**
  quedaron parejas (misma fuente que el nombre).
- **Captura:** la IA ahora *corrige* el delito escrito en las 3 casillas (no
  propone otro); listas de incautación con nombre y apellidos completos; alerta
  si se escribe un vehículo en Elementos Incautados; en primer respondiente,
  casilla **Tipo** en vehículos y **sin tope de 2** personas que entregan.

- **`v1.13.7-windows-exe`** (*Latest*), SHA `0f089759…`.
- **`v1.13.7-android`** (`--latest=false`), SHA `1d546045…`, versionCode 16.
- Links de `index.html` y hashes de `seguridad.html` actualizados a 1.13.7.
- PWA redesplegada sola desde `main` (el Worker no cambió en este lote). El APK
  exige **JDK 21** (`JAVA_HOME` al JBR de Android Studio), igual que la vez pasada.

## 1.13.6 publicada (2026-10-28)

Lote de mejoras de UI pedidas por el dueño (todas en `informes-ponal`):

- **Captura — ¿a quién notificar?**: los campos (nombre/ID/teléfono/hora) solo
  salen tras elegir Papá/Mamá/Otro, no antes.
- **Elementos incautados:** el aviso rojo solo aparece con 1+ elementos (antes
  salía con el contador en 0).
- **Inicio:** la tarjeta de proceso no seleccionada va en gris apagado y la
  seleccionada en dorado pleno (se nota la diferencia).
- **Licencia/prueba terminada:** banner rojo permanente arriba con botón Activar,
  desde el arranque (antes solo salía al intentar generar).
- Por dentro (cierra Vikunja Informes PONAL #172): de-versión del userAgent en la
  huella (actualizar la app ya no la cambia) y ciudad/URI también en `/estado`.

- **`v1.13.6-windows-exe`** (*Latest*), SHA `7836813f…`.
- **`v1.13.6-android`** (`--latest=false`), SHA `45776f16…`, versionCode 15.
- Links de `index.html` y hashes de `seguridad.html` actualizados a 1.13.6.
- PWA y **Worker** redesplegados solos desde `main`. Compilar el APK/AAB exige
  **JDK 21** (`JAVA_HOME` al JBR de Android Studio); con el JDK 20 del PATH falla.
- Se generó además el **`.aab`** para Google Play (tarea aparte, aún sin subir).

## 1.13.5 publicada (2026-10-27)

Lote de ajustes pedidos por el dueño:

- **Fechas con teclado numérico:** en el APK, `<input type="date">` solo abría el
  calendario nativo. Ahora todos los campos de fecha usan un componente propio
  (`FechaInput`) de texto DD/MM/AAAA con teclado numérico (valida día/mes/año
  reales) y un botón 📅 de respaldo. Internamente sigue guardando `YYYY-MM-DD`.
- **Constancia de buen trato (FPJ-6):** el mes ahora va con NOMBRE ("octubre"),
  no con número.
- **NUNC por defecto `1100160000`** y **URI en blanco** (antes traía una URI de
  ejemplo); cuando la URI está vacía aparece un botón **Configurar** al lado que
  lleva directo a la configuración.
- **Estadísticas por ciudad/URI** (lado servidor, pendiente de desplegar el
  Worker) y **conteo de informes corregido** (contaba cada clic; ahora cuenta
  informes distintos, como el trial).

- **`v1.13.5-windows-exe`** (*Latest*), SHA `ff70a6a5…`.
- **`v1.13.5-android`** (`--latest=false`), SHA `b240b0d9…`, versionCode 14.
- PWA y **Worker** redesplegados **solos** desde `main` (workflows "Deploy app
  (PWA)" y "Deploy Worker de licencias"). O sea las estadísticas de ciudad/URI y
  el conteo corregido ya están en vivo. Lo único manual que queda: reimportar el
  workflow de n8n para que el resumen diario de Telegram muestre esas secciones.

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
