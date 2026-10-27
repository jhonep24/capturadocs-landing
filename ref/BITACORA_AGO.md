# Landing — bitácora de agosto 2026 (chat cotizador, transparencia legal y correcciones)

> Movido tal cual desde `CONTEXTO.md` el 2026-10-27 para ahorrar tokens. Cronológico, ya cerrado; no es estado vivo. Contenido:

- Chat de la landing — cotizador (2026-08-10)
- Transparencia legal y validación del resumen (2026-08-10)
- Corrección: dónde se anonimiza el texto para la IA (2026-08-11)
- Corrección: contradicción legal sobre cambio de dispositivo (2026-08-11)
- Corrección: botón de chat "aparecía solo al final" en móvil (2026-08-11)
- Corrección: dónde guarda los documentos la app de Windows (2026-08-11)

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

---

## Pendientes antiguos de la landing (congelados; la lista viva es Vikunja, proyecto 5)


- ~~**#14** — Enlazar botones a la app real, no solo a WhatsApp.~~ **Resuelto 2026-08-08** — ver nota de CTAs arriba.
- **#15** — Reemplazar la maqueta falsa de `.preview` (sección Funciones) por una captura o GIF real de la app funcionando.
- ~~**#19** — Centralizar el número de WhatsApp en una constante de JS.~~ **Resuelto 2026-08-11** — quedan solo 2 enlaces reales (footer y menú del chat, `class="wa-link"`), ambos sin `href` fijo: se completan en runtime desde `const WA_NUMBER` (ver `<script>` principal). `check_wa_number.py` se actualizó para validar esa constante en vez de buscar `wa.me/<numero>` hardcodeado en el HTML.
- ~~Reactivar descargas de Android e iPhone~~ — **hecho 2026-10-17** (ver punto 6.5).
- **Precio del espacio publicitario definido, pero NO público**: el usuario fijó
  $150.000 COP/mes (precio de arranque, sin datos de tráfico todavía — se ajustará
  con los primeros anunciantes) — **es el precio para cuando alguien pida cotizar
  por el chat, no debe aparecer escrito en la landing** (pedido explícito
  2026-08-11, tras un primer intento de mostrarlo en `.ads-promo-price` que se
  revirtió el mismo día). La sección `.ads-promo` (punto 10.5) sigue sin precio
  visible a propósito — el botón "Quiero anunciarme →" abre el chat en "Contacto"
  para que se cotice ahí. **Este precio de $150.000/mes solo vive en este archivo
  y en la cabeza de quien responda el chat de publicidad** — no hay automatización
  todavía que lo aplique solo (a diferencia de los precios de licencias, que sí
  están en `PLANES` del Worker). Si en el futuro se agrega un flujo automático de
  cotización de publicidad, usar este valor como el vigente salvo que el usuario
  indique uno nuevo. (La sección de referidos, punto 8.5, ya no está pendiente —
  se rediseñó el 2026-08-10; la mecánica del programa en sí, `REF-XXXXXXXX`/+7
  días, vive en `informes-ponal` sin cambios de este lado.)
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
