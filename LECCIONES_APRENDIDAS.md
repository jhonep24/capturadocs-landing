# Lecciones aprendidas — CapturaDocs Landing

Registro de decisiones, mejoras y problemas resueltos en este repo, sesión a
sesión. El objetivo es que una sesión nueva entienda el "por qué" detrás de
los cambios sin tener que releer todo el `index.html` ni adivinar por qué se
hizo algo de cierta forma.

Ver también [CONTEXTO.md](CONTEXTO.md) para el sistema de diseño y la
estructura de secciones de la landing.

---

## 2026-08-18 — Publicar el `.exe` nuevo: el hash de integridad llevaba rato mal

### Qué se hizo

Se subió al release `v1.6.10-windows-exe` el instalador recién compilado (arreglo
de la numeración de derechos, ids de gráficos y el espacio del FPJ-6) con
`gh release upload --clobber`. El nombre de archivo no cambió, así que el `href`
de `#descargas` en `index.html` siguió sirviendo sin tocarlo. Se actualizó
`#hash-win` en `seguridad.html` al SHA-256 del build nuevo
(`5ce7b577…40b8bb1b`), **verificado descargando el archivo desde el link público
real** (`releases/latest/download/...`), no desde la copia local — que es lo único
que prueba que el usuario recibe exactamente lo que la página promete.

### Problemas encontrados y cómo se resolvieron

1. **El hash publicado estaba desactualizado, y las dos copias no coincidían entre
   sí.** `seguridad.html` decía `c92261ff…` y `CONTEXTO.md` decía `6df2d48b…` —
   distintos, y ninguno correspondía ya al `.exe` que se estaba descargando de la
   landing. O sea que cualquiera que siguiera las instrucciones de verificación
   habría concluido que el instalador estaba **alterado**. En una página que se
   llama "Arquitectura de privacidad" eso es peor que no publicar hash.
   **Arreglado de raíz**: el valor ahora vive solo en `seguridad.html` (la página
   que lo publica) y `CONTEXTO.md` apunta ahí en vez de repetirlo. Duplicarlo no
   daba respaldo, solo una segunda cosa que se desincroniza en silencio.

2. **El comando de verificación citaba un archivo que ya no existe.** La nota decía
   `certutil -hashfile CapturaDocs-Express-Windows.zip SHA256`, nombre heredado de
   la época del `.msix` empaquetado en `.zip`. Desde el 2026-08-14 lo que se
   descarga es `CapturaDocs.Express.Setup.1.6.10.exe`, así que el comando fallaba
   con "no se encuentra el archivo". Corregido al nombre real (entre comillas: lleva
   puntos y es largo).

**Lección**: un dato que se publica para que el usuario *verifique* algo tiene que
actualizarse en el mismo paso en que se publica lo verificado, o se vuelve activamente
dañino — no queda "viejo pero inofensivo", queda **acusando de fraude a tu propio
instalador**. Al republicar un binario: subir asset → recalcular hash desde el link
público → actualizar la página, en ese orden y en la misma sesión.

---

## 2026-08-11 (segunda parte) — Auditoría de consistencia landing ↔ app

### Qué se hizo

El usuario pidió validar si había inconsistencias entre esta landing y la
app (`informes-ponal`) en Términos/Privacidad/Licencias — "todo debe
quedar igual". Se comparó texto por texto contra los `.md` legales de la
app y contra el código real (`worker/index.js`), no solo entre los dos
HTML. Se encontraron 3 inconsistencias reales:

1. **Contradicción legal grave — cambio de dispositivo**: el modal de esta
   landing (Términos §7, Licencias §6) decía que había que **comprar una
   licencia nueva** al cambiar de dispositivo. Pero la propia FAQ pública
   de esta misma landing, y los documentos oficiales de la app
   (`terminos_condiciones.md`, `politica_licencias.md`), decían que la
   reasignación es **gratis por WhatsApp**. Es decir, el modal se
   contradecía con la FAQ **de la misma página**. Corregido para que las
   tres fuentes digan lo mismo: reasignación gratis, sin licencia nueva.
2. **Generaciones del código de regalo**: la landing decía correctamente
   "+5" (verificado contra `TRIAL_GIFT = 5` en el Worker), pero
   `informes-ponal/src/politica_licencias.md` decía "hasta 10" — corregido
   ahí.
3. **Hash SHA-256 "junto al enlace de descarga"**: la política de
   licencias de la app seguía prometiendo que el hash estaba al lado del
   botón de descarga — una promesa que dejó de ser cierta la sesión
   anterior, cuando se movió de ahí a pedido del usuario. El usuario
   definió dónde debía quedar: visible en la landing, pero dentro de la
   documentación de seguridad, no al lado del botón. Se agregó una sección
   `.hashbox` nueva en `seguridad.html` con el hash, la versión y el
   comando para calcularlo (`certutil -hashfile ... SHA256`), y se
   actualizó la referencia en `politica_licencias.md` para apuntar ahí.

### Por qué

Con 3 documentos legales casi idénticos en 2 repos distintos (landing y
app), y ediciones frecuentes en ambos por sesiones separadas, es fácil que
uno se actualice y el otro no — exactamente lo que pasó aquí. La lección
operativa: cuando se toca un texto legal en un repo, revisar si el mismo
hecho está descrito en el otro, y si el número/regla que se está por
escribir tiene una fuente de verdad en código (constantes del Worker,
flujos de reasignación) verificarla ahí antes de copiar de un documento a
otro — así fue como se detectó que "+10" en la app estaba mal y "+5" en la
landing estaba bien, no al revés.

### Verificación

Todo se verificó contra el código antes de escribir el texto (no se copió
de un documento a otro sin más): `TRIAL_GIFT` y `REFERIDO_DIAS_BONUS` leídos
directo de `worker/index.js`, la reasignación gratuita confirmada en 3
fuentes independientes (FAQ, `terminos_condiciones.md`,
`politica_licencias.md`) antes de asumir cuál lado era el erróneo. Cambios
probados localmente (modal Términos/Licencias, `#hash-win` en
`seguridad.html`) antes de publicar.

---

## 2026-08-11 — Auditoría externa de privacidad: política reforzada, página /seguridad y limpieza de detalles

### Qué se hizo (en orden)

1. **SHA-256 fuera de la vista principal**: el usuario pidió quitar el hash
   del instalador de Windows que se veía debajo del botón de descarga en
   `#descargas` — "no es necesario" verlo ahí. Se quitó del HTML y quedó
   solo documentado en `CONTEXTO.md` (con el valor exacto, para no
   perderlo) por si hace falta para verificación técnica.
2. **#19 — Centralizar el número de WhatsApp**: quedaban 2 enlaces
   `wa.me/<numero>` hardcodeados (footer y menú del chat). Se movieron a
   una sola constante `const WA_NUMBER` en el `<script>` principal, con
   los anchors usando `class="wa-link"` y `href="#"` hasta que el JS los
   completa en runtime. Hubo que actualizar `check_wa_number.py` (el hook
   de pre-commit) porque validaba buscando `wa.me/<numero>` literal en el
   HTML — ya no aparece ahí, así que el script se reescribió para validar
   la constante `WA_NUMBER` en su lugar.
3. **Segunda ronda de feedback de una auditoría externa de IA** sobre la
   landing (la primera ronda fue la del 2026-08-10, ver entrada de esa
   fecha en este archivo). Traía 3 recomendaciones — se resolvieron en
   dos pasos porque el usuario priorizó cuáles atacar primero:
   - **Refuerzo de la Política de Privacidad** (pestaña `#content-pp` del
     modal, de 9 a 12 secciones). El hallazgo más importante fue una
     **imprecisión real, no solo de tono**: el texto decía "no recopila ni
     transmite datos personales a servidores externos" de forma absoluta,
     pero eso es falso para nombre/correo/WhatsApp/ID de dispositivo/imagen
     del comprobante que sí viajan a la infraestructura propia
     (`capturadocs-bot-pagos` vía Cloudflare Tunnel) cuando alguien usa el
     chat para cotizar, pagar o escribir. Se corrigió distinguiendo
     explícitamente **(a) datos del procedimiento** (100% local) de
     **(b) datos de gestión de pedidos/contacto** (sí se envían, solo para
     eso) — ver detalle en `CONTEXTO.md`, sección "Transparencia legal".
   - **Cambiar "100% privado"**: el usuario no quiso perder el "100%" (a
     diferencia de lo que sugería la auditoría, que prefería evitar
     absolutos del todo) — se acordó un punto medio acotando el "100%" a
     un hecho verificable: **"100% seguros los datos de tu procedimiento"**
     en vez de una promesa de seguridad genérica sobre toda la app.
   - **Página `/seguridad.html`** con diagrama de arquitectura de
     privacidad (dos columnas: 📱 local / ☁️ infraestructura propia) — la
     pieza más grande de las 3. Reutiliza el sistema de diseño pero con su
     propio `<style>` recortado (no todo el de `index.html`). El botón
     "Leer la Política de Privacidad" apunta a `index.html#privacidad`, y
     se agregó un bloque corto de JS en `index.html` que abre el modal
     directo en la pestaña Privacidad si detecta ese hash al cargar — así
     el texto legal sigue viviendo en un solo lugar, sin duplicarlo.

### Por qué

Todo nace de comentarios de una IA externa auditando la landing (no es
`/security-review` de Claude Code, es una revisión aparte que el usuario
pidió evaluar). El punto más importante no era de redacción: la política
de privacidad **contradecía lo que el código realmente hace** en cuanto se
usa el chat de pedidos — eso sí era un problema real que corregir, más allá
de si el texto sonaba "profesional".

### Problemas encontrados al verificar

- El entorno de preview (Browser pane) marca los archivos `file://` fuera
  de la carpeta del proyecto como "instantáneas estáticas": los clics en
  enlaces no navegan de verdad ahí, aunque la lógica en sí sea correcta
  (se confirmó llamando las funciones a mano). Esto llevó a probar el hash
  `#privacidad` directo contra producción (`capturadocs.com`) con un clic
  real, que sí navegó y abrió el modal correctamente — **la prueba que
  importa es siempre la de producción**, no la del preview local con
  archivos fuera del proyecto. Mismo tipo de lección que la del timeout de
  ~30s del `javascript_tool` documentada en la entrada del 2026-08-08: no
  confundir una limitación de la herramienta de prueba con un bug real.
- La herramienta `navigate` con `force:true` sobre una URL `file://` con
  fragmento (`#privacidad`) a veces lo pierde silenciosamente al abrir —
  otra razón más para no fiarse de esa ruta de prueba y verificar en el
  sitio real.

---

## 2026-08-10 — Rediseño de la sección de referidos

### Qué se hizo

El usuario pidió que la sección `#referidos` se viera más profesional y no
le gustó el eslogan "Comparte tu código, ganen los dos" (sonaba informal/
gamificado). Se rediseñó:

- **Texto**: eslogan nuevo "Tú recomiendas, los dos ganan." (elegido entre
  varias opciones ofrecidas con `AskUserQuestion`). Las 3 tarjetas genéricas
  (`.tcard`) se reemplazaron por 3 pasos numerados con flechas conectoras
  (`.refgrid`/`.refcard`/`.refarrow`), la última tarjeta destacada en dorado
  (`.refcard-reward`) por ser la recompensa para quien refiere.
- **CSS nuevo**: agregado junto a los estilos de `.tgrid`/`.tcard`
  existentes (no se reutilizaron, la estructura es distinta — numeración +
  flechas). Las flechas se ocultan en móvil (`@media(max-width:780px)`) para
  no romper el layout cuando las tarjetas se apilan.
- La mecánica del programa (código `REF-XXXXXXXX`, +7 días para cada lado)
  **no cambió** — esto fue solo texto/diseño de la landing, ver
  `CONTEXTO.md` punto 8.5.

### Por qué

Pedido explícito del usuario en dos pasos: primero "mejora esos textos",
luego al ver el resultado no le gustó el eslogan inicial que yo propuse
("...y los dos salen ganando") y pidió una opción más corta tipo "tu
recomiendas los dos ganan" — se usó `AskUserQuestion` para no adivinar y
confirmar la versión exacta antes de publicar.

### Verificación antes de publicar

Se abrió la landing en el Browser pane (`preview_start` con el archivo
local), se hizo scroll a `#referidos` y se tomó screenshot en dos anchos
(mobile ~577px y desktop 1280px) para confirmar que las 3 tarjetas se ven
bien en fila en desktop y apiladas sin flechas sueltas en mobile. Después
de publicar, se re-verificó el texto exacto en `capturadocs.com` en vivo
(no solo el commit) antes de darlo por hecho, como es la costumbre en este
repo.

---

## 2026-08-08 — Tono profesional, CTAs al contenido real, revisión de seguridad, comprobante urgente, chat libre y sección de anunciantes

### Qué se hizo (en orden)

1. **Pase de tono/claridad**: el usuario pidió que la landing se sintiera
   más profesional. Se reescribió el hero (antes asumía que el visitante
   ya sabía qué es un "FPJ-5" — ahora dice explícitamente "software para
   informes de captura en flagrancia" y usa nombres completos de los
   documentos, no códigos), se quitaron emojis decorativos sin significado
   (🚀, ✨, 📋 sueltos) manteniendo los que funcionan como iconografía real
   (pasos, funcionalidades), y se reemplazaron los íconos de plataforma de
   la sección Descargas (emoji 🤖/🖥️/📱) por SVG monocromo estilo
   Android/Windows/Apple.
2. **Todos los CTAs dejaron de apuntar a WhatsApp por defecto** — WhatsApp
   pasó a ser el último recurso, no el primero (pedido explícito del
   usuario: *"no quiero incentivar el uso de wsp"*). Nav/hero/CTA final →
   `#descargas` (luego se probó llevar directo a la PWA, pero el usuario
   pidió que primero pasara por Descargas). Planes pagos → abren el chat
   en "Cotizar" con el plan preseleccionado (`abrirChatEnVista('cotizar',
   plan)`). FAQ "Pregúntanos" → abre el chat en "Contacto". El único
   `wa.me` que sobrevive con esa etiqueta es el del propio menú del chat,
   renombrado de "Prefiero WhatsApp" a "Contáctanos por WhatsApp" para no
   sonar a opción recomendada.
3. **Revisión de seguridad** (a pedido del usuario, `/security-review` no
   sirvió porque no había diff — todo ya estaba en `main` — se hizo manual
   sobre el estado completo del archivo): se encontró que 4 puntos del
   widget insertaban campos de la respuesta del backend (`data.mensaje`,
   `data.pedido.estado`, `data.pedidoId`, `data.plan`) directo en
   `innerHTML` sin escapar — si el backend (n8n) alguna vez reflejara texto
   libre del usuario (ej. el campo "nombre" del comprobante) dentro de esos
   campos, se ejecutaría como HTML/JS en el navegador de la víctima. Se
   agregó `escapeHtml()` y se aplicó en los 4 puntos. Verificado con un
   payload de prueba (`<img src=x onerror=...>`) que efectivamente dejó de
   ejecutarse tras el fix.
4. **Arreglo urgente en producción**: la otra sesión (`capturadocs-bot-pagos`)
   avisó por mensaje directo que había cambiado el contrato de
   `accion:"comprobante"` en `landing-chat` para exigir también `sessionId`
   y `plan`, no solo `deviceId`+`imagenBase64`. Se verificó con un `curl`
   real contra producción **antes de hacer nada** — confirmado: cualquier
   cliente que intentara subir un comprobante de pago en ese momento
   recibía `400`. Se agregó un selector de plan a la vista de comprobante y
   `getSessionId()` (UUID en `localStorage`, única "autenticación" del
   hilo). Publicado de inmediato por ser un bloqueo real de ventas, sin
   esperar a construir el resto de mejoras pendientes.
5. **Vista de chat libre** ("Escríbenos: ayuda, renovar, estado,
   referidos"): construida contra el diseño que documentó la otra sesión
   (core conversacional compartido con WhatsApp/Telegram, `accion:"mensaje"`
   + polling en `landing-mensajes`). Al probarla en vivo, `landing-mensajes`
   daba 404 público — la ruta existía en n8n pero nunca se agregó al túnel
   de Cloudflare (mismo gotcha de siempre). Se publicó igual, sin el
   endpoint de recepción funcionando, porque el usuario autorizó
   explícitamente publicarla ya que **todavía no hay clientes reales**
   usando la landing — el costo de que alguien mande un mensaje y no vea
   respuesta era aceptable mientras se resolvía del lado de n8n. Resuelto
   por la otra sesión horas después (migraron el túnel de
   `chat.capturadocs.com` a uno gestionado por config/CLI); confirmado de
   punta a punta con `curl` y en la interfaz real antes de darlo por
   bueno.
6. **`accion:"mensaje"` cambió de asíncrono a síncrono** (la otra sesión
   rediseñó el chat: dejó de ser un menú tipo WhatsApp "responde 1/2/3" y
   pasó a ser un asistente de FAQ con respaldo de IA). Se verificó con
   `curl` antes de tocar código: ahora `{ok:true, respuesta:"..."}` llega
   en la misma llamada, normalmente en 2-3s. Se simplificó
   `chatLibreEnviar()` para usar `data.respuesta` directo — se eliminó el
   `setInterval` de polling que ya no hacía falta. Se agregó un aviso
   ("Esto puede tardar un poco más de lo normal…") a los 6s, porque el
   caso raro de fallback a un modelo local puede tardar ~40-70s
   (confirmado con `curl`, 40s reales en una prueba).
7. **Sección "Anúnciate con nosotros"**: `informes-ponal` ya tenía un
   motor de banners publicitarios (`BannerPublicidad.jsx`, imagen+link,
   solo visible a usuarios sin licencia paga) pero ningún lugar público
   para conseguir anunciantes. Se agregó una sección discreta entre el CTA
   principal y el footer (para no competir con la conversión de policías,
   que es la audiencia real del resto de la página) con un CTA que abre el
   chat en "Contacto" con el tipo "Quiero anunciarme en la app"
   preseleccionado — sin precio fijo todavía, a pedido del usuario
   ("cotizar" en vez de mostrar precio). Primera versión quedó "muy
   simple" según el usuario; se rediseñó con ícono en badge dorado, fondo
   con gradiente/resplandor y chips de beneficios, para que se sintiera al
   nivel del resto de la página.
8. **Descargas de Android e iPhone deshabilitadas temporalmente** (pedido
   explícito, motivo no técnico): los botones quedan visibles pero
   inactivos ("Próximamente", `aria-disabled`), no se ocultaron — solo
   Windows sigue activo.

### Por qué

Todo esto salió de una sola pregunta abierta ("¿alguna mejora que me
recomiendes?") que fue derivando: tono → seguridad → un hallazgo de
seguridad reveló que el contrato del backend había cambiado y rompió
producción → arreglarlo llevó a construir la función que la otra sesión
ya tenía lista del lado de n8n → eso llevó a coordinar en vivo con esa
sesión dos veces (túnel roto, luego contrato síncrono) → la conversación
derivó en monetización (publicidad) como siguiente paso natural.

### Problemas encontrados y cómo se resolvieron

- **No asumir que un aviso de otra sesión ya funciona, aunque diga
  "probado en vivo de punta a punta"**: dos veces en este mismo día se
  verificó con `curl`/pruebas reales antes de dar algo por bueno, y una de
  esas veces (el túnel de `landing-mensajes`) el aviso resultó ser
  prematuro — el endpoint daba 404 real. La otra vez (contrato síncrono)
  sí era exacto. No hay forma de saber cuál es cuál sin probar.
- **Este entorno de pruebas (Browser pane) no aguanta bien esperas largas**:
  al intentar reproducir el caso lento (~40-70s) de `accion:"mensaje"`
  dentro del navegador de prueba de esta sesión, la herramienta se
  recargaba/perdía el estado de JS después de ~30s de espera — un
  `curl` directo (sin ese límite) sí completó la misma petición en 40s
  con la respuesta correcta. Lección: cuando una prueba en este entorno
  falla justo en el límite de tiempo de la herramienta, no asumir que el
  código está roto — repetir con `curl` antes de reportarlo como bug.

---

## 2026-08-07 — Sección de descargas (Android APK, Windows .msix, iPhone PWA)

### Qué se hizo

Sección nueva `.downloads#descargas` con instalador real para Android y
Windows, y enlace a la PWA para iPhone (decisión ya tomada: iOS no tendría
instalador nativo).

- **Android**: se generó un keystore de firma propio (no debug) en
  `informes-ponal/android/keystore/` (gitignored) y se agregó
  `signingConfigs.release` a `android/app/build.gradle`, leyendo el keystore
  desde un `.properties` también gitignored. Se compiló con `gradlew
  assembleRelease`, verificado con `apksigner verify` (firma V2 válida).
- **Windows**: se generó el paquete con la **API pública de PWABuilder
  directamente** (`POST .../msix/generatezip`), no con su interfaz web.
- **iPhone**: solo un link a la PWA con instrucción de "Agregar a inicio"
  desde Safari, sin build nuevo.

### Por qué

El usuario pidió explícitamente "instalador para PC", no solo la PWA (que ya
existía). Se evaluaron Electron/Tauri (meses de trabajo, proyecto aparte) vs.
PWABuilder (empaqueta la PWA existente en un `.msix` real, cero rediseño) —
se eligió PWABuilder por ser el punto intermedio real.

### Problemas encontrados

- **Faltaba JDK 21**: el proyecto Capacitor exige `JavaVersion.VERSION_21`
  (`capacitor.build.gradle`, autogenerado por `cap sync`) y solo había 17/20
  instalados. El instalador `.msi` oficial de Temurin 21 falló con error 1603
  (requiere permisos de administrador que esta sesión no tenía). Se resolvió
  usando el `.zip` portátil de Temurin (sin instalación, solo `JAVA_HOME`
  apuntando ahí) — **lección: para JDKs en máquinas sin admin, usar zip, no
  MSI**. Checksum verificado contra el oficial de adoptium.net antes de usar.
- **El sitio de pwabuilder.com no respondía a clicks automatizados**: sus
  componentes son Lit con shadow DOM; `.click()` y hasta
  `dispatchEvent(MouseEvent)` sobre el botón real no disparaban ninguna
  petición de red (mismo síntoma ya documentado antes: el Browser pane de
  esta sesión no compone frames de verdad, así que algunas interacciones no
  registran). Se resolvió leyendo el bundle JS del sitio
  (`grep -oE 'https?://[^"]*windows[^"]*' index-*.js`) para encontrar el
  endpoint real (`pwabuilder-windows-docker.azurewebsites.net/msix/generatezip`),
  y el shape del payload en el repo open-source de PWABuilder en GitHub
  (`WindowsAppPackageOptions.cs`) — **lección: cuando una herramienta web es
  un SPA pesado y el click automatizado no dispara nada, buscar si expone una
  API pública y llamarla directo es más confiable que seguir intentando con
  el navegador**.
- **GitHub Release 404 para el público**: el primer release con los binarios
  se creó en `informes-ponal`, que es un repo **privado** — los links
  `releases/latest/download/...` devuelven 404 para cualquiera sin acceso al
  repo, aunque el asset esté subido correctamente (`state: uploaded` en la
  API). Se movió el release a `capturadocs-landing` (público, ya lo es porque
  sirve GitHub Pages) — **lección: los assets de descarga pública deben vivir
  en un repo público, nunca asumir que "está en GitHub" es suficiente para
  que un visitante externo lo descargue**.



### Qué se hizo

Revisión completa del `index.html` (SEO, accesibilidad, seguridad,
rendimiento) y aplicación de los hallazgos de mayor impacto:

- `rel="noopener"` en los 9 enlaces `target="_blank"` (WhatsApp/CTAs).
- Imagen de vista previa social (`logo-og.jpg`) regenerada de 512×512 a
  1200×630 — el tamaño cuadrado se veía recortado al compartir el link en
  WhatsApp/Facebook/LinkedIn. Se generó con Python/Pillow componiendo el
  logo + texto de marca sobre el fondo navy del sistema de diseño, en vez
  de solo estirar la imagen vieja.
- `twitter:card` cambiado de `summary` a `summary_large_image` para que la
  imagen panorámica se muestre en grande y no como miniatura cuadrada.
- Modal de términos y condiciones: agregado `role="dialog"`,
  `aria-modal="true"`, `aria-labelledby`, `aria-label="Cerrar"` en el botón
  ✕, focus trap (Tab/Shift+Tab no se escapa del modal) y devolución de foco
  al elemento que lo abrió al cerrarlo.
- Pestañas del modal (Términos/Privacidad/Licencias): `role="tablist"`,
  `role="tab"`, `role="tabpanel"`, `aria-selected` y `aria-controls`,
  sincronizados en `showTab()`.
- `theme-color` (`#070f1f`) para que la barra del navegador en móvil
  combine con el fondo navy en vez de quedar con el color por defecto.
- `apple-touch-icon`, `rel="canonical"` y `preconnect` a Google Fonts.
- `width`/`height` en el `<img>` del logo del nav para evitar salto de
  layout (CLS) mientras carga.

### Por qué

El público objetivo (policías compartiendo el link entre compañeros por
WhatsApp) hace que la vista previa social y el acceso por teclado/lector de
pantalla en el modal de términos legales sean puntos con impacto real, no
solo cosmético. `[[project_pcs_produccion]]` recuerda que estas PCs de
producción son sensibles a cambios mal probados, así que se priorizaron
arreglos acotados y verificables antes que un rediseño.

### Problemas encontrados y cómo se resolvieron

- **`python3` fallaba con exit code 49 sin mensaje útil.** Era el alias de
  Microsoft Store (stub que redirige a instalar Python desde la tienda),
  no el intérprete real. Se resolvió usando `python` directamente — en
  este entorno Windows, `python3` no es de fiar como comando.
- **Estimación a ojo del contraste de `--muted` sobre `--navy` resultó
  errónea.** En la revisión inicial se marcó como posible falla de WCAG AA
  (~4.1:1 estimado). Al calcularlo con la fórmula real de luminancia
  relativa (script Python), el resultado real es **5.51:1**, que sí cumple
  AA (mínimo 4.5:1). Lección: no aplicar un "arreglo" de contraste sin
  calcular el ratio real primero — cambiarlo sin necesidad hubiera sido
  una alteración visual injustificada del sistema de diseño.
- **`og:image` cuadrada (512×512) no es el tamaño que Facebook/WhatsApp
  recomiendan (1200×630).** No bastaba con cambiar los metadatos
  `og:image:width/height` — había que generar una imagen nueva con esas
  proporciones reales, si no la vista previa social se ve mal recortada.

### Pendientes que quedaron fuera de esta pasada (prioridad media/baja)

Del backlog original de la revisión, sin aplicar todavía:

- Analítica (Google Analytics/Plausible) — hoy no hay forma de medir
  cuántas visitas llegan a WhatsApp vs. rebotan.
- Centralizar el número de WhatsApp (hoy repetido en ~9 lugares) en una
  constante de JS.
- Pendientes ya documentados en `CONTEXTO.md`: #14 (CTAs a la app real en
  vez de solo WhatsApp), #15 (reemplazar maqueta de funciones por captura
  real), #17 (mover hosting de GitHub Pages a Vercel/Netlify).

---

## 2026-08-03 — Prioridad media: SEO estructural

### Qué se hizo

- **JSON-LD** (`schema.org/SoftwareApplication`) en el `<head>` con nombre,
  descripción, URL, imagen y los 4 planes de precio como `offers`.
- **`robots.txt`** apuntando al sitemap.
- **`sitemap.xml`** con la única URL del sitio (landing de una sola página).

### Por qué

El JSON-LD le da a Google datos estructurados para mostrar (potencialmente)
precio y categoría de la app directamente en resultados de búsqueda, sin
depender de que el crawler infiera esa info del texto visible. `robots.txt`
+ `sitemap.xml` son prácticamente gratis de mantener en un sitio de una
sola página y evitan que el crawling dependa solo de enlaces externos.

### Problemas encontrados y cómo se resolvieron

- Antes de dar el JSON-LD por bueno, se extrajo el bloque del HTML con un
  script de Python (`re` + `json.loads`) para confirmar que parseaba como
  JSON válido — un solo error de coma ahí lo invalida silenciosamente para
  los crawlers sin que se note visualmente en el navegador.

### Nota sobre mantenimiento

Si cambian los precios o los planes en `.pricing` (`index.html`), hay que
actualizar también el bloque `offers` del JSON-LD — no se generan solos a
partir del HTML visible. Ver también la nota correspondiente en
`CONTEXTO.md`.

---

## 2026-08-03 — Prioridad baja: número de WhatsApp y analítica

### Qué se hizo

- **#19 resuelto distinto a como se propuso originalmente.** La idea
  inicial (centralizar el número de WhatsApp en una constante de JS que
  arma los `href` al cargar la página) se descartó tras pensarlo mejor: en
  una landing cuyo único camino de conversión son esos enlaces, hacerlos
  depender de que JS cargue y corra sin errores es cambiar un riesgo bajo
  (typo al editar a mano) por uno peor (CTA muerto si JS falla o el
  usuario lo bloquea). En su lugar se creó `check_wa_number.py`: un script
  que escanea `index.html`, extrae todos los números en enlaces `wa.me/` y
  falla si hay más de uno distinto. Se probó en dos escenarios: número
  consistente (pasa) y con un número alterado a propósito en una sola
  ocurrencia (falla y lo señala). Se enganchó como git hook versionado en
  `.githooks/pre-commit`.
- **#18 (analítica) se dejó pendiente a propósito.** Requiere una cuenta
  real (GA4, Plausible, etc.) — no tiene sentido inventar un ID de
  tracking. Queda para cuando el usuario decida el servicio.

### Por qué

El objetivo real detrás de "centralizar el número" no era el número en sí,
sino evitar que una edición manual futura deje el sitio con enlaces
inconsistentes sin que nadie lo note hasta que un usuario reporte el
problema. Un chequeo que corre antes de comitear resuelve exactamente eso,
sin tocar en nada el comportamiento del sitio publicado.

### Problemas encontrados y cómo se resolvieron

- **El hook de git no se activa solo al clonar el repo.** `.git/hooks/`
  no se versiona con git — por eso el hook vive en `.githooks/` (sí
  versionado) y necesita `git config core.hooksPath .githooks` corrido a
  mano una vez por clon. Este comando no se ejecutó automáticamente: la
  sesión que hizo el cambio tiene la regla de no tocar la configuración de
  git nunca, ni siquiera local — queda como paso manual documentado acá y
  en `CONTEXTO.md`.

---

## 2026-08-04 — Dominio propio + widget de chat con compra directa

### Qué se hizo

- Se compró `capturadocs.com` en Cloudflare Registrar y se configuró como
  custom domain de GitHub Pages: archivo `CNAME` en el repo + 4 registros
  DNS tipo A (apex) apuntando a las IPs de GitHub Pages + 1 CNAME para
  `www`, todos con proxy de Cloudflare apagado (DNS only) para que GitHub
  pudiera emitir el certificado HTTPS. `https_enforced` se activó después
  vía la API de GitHub (`PUT /repos/.../pages`).
- Se agregó un widget de chat flotante (`#chatToggle`/`#chatPanel` en
  `index.html`) con 4 acciones: ver precios, cotizar un plan, subir
  comprobante de pago (deviceId + foto), y consultar el estado de un
  pedido por deviceId. No es un chat de texto libre — es un menú
  estructurado con botones y formularios, deliberadamente más simple que
  el bot de WhatsApp (ver el porqué abajo).
- El widget habla directo con dos webhooks nuevos del bot de
  `capturadocs-bot-pagos` (`/webhook/landing-chat` y
  `/webhook/landing-status`), expuestos en el mismo túnel de Cloudflare
  que ya exponía el webhook de WhatsApp, bajo el hostname
  `chat.capturadocs.com`. El diseño completo del lado del bot (motor
  compartido, columna `canal`, dónde se guarda la clave) está en
  `capturadocs-bot-pagos/CONTEXTO.md` sección 50 y
  `LECCIONES_APRENDIDAS.md` de ese repo.

### Por qué

El usuario pidió que la compra (incluyendo subir el comprobante) se
pudiera hacer directo desde la landing, sin depender de que WhatsApp esté
disponible — la aprobación del pago la sigue haciendo el dueño por
WhatsApp como siempre, pero el cliente ya no tiene que salir de la landing
para nada del proceso de compra.

Se decidió construir el widget como un **menú de acciones estructurado**
(botones + formularios) en vez de un chat de texto libre con NLU, porque
replicar el reconocimiento de intención del bot de WhatsApp (que tiene
~200 nodos de n8n dedicados a eso) hubiera sido reinventar esa lógica dos
veces, con doble superficie de bugs. Un menú de acciones fijas cubre
exactamente los casos que se pidieron (precio, cotizar, comprobante,
estado) con una fracción del esfuerzo y sin duplicar el motor existente.

### Problemas encontrados y cómo se resolvieron

- **`landing-status` iba a devolver la clave siempre en `null`.** El plan
  original era leer la clave desde `/admin/consultar` del Worker de
  licencias, pero ese endpoint solo refleja `dispositivo.clave` **después**
  de que el cliente activa la clave en la app — nunca justo después de
  generarla, que es exactamente cuando el cliente web más la necesita. Se
  detectó probando el flujo completo en vivo (comprobante de prueba →
  aprobación → consulta de estado) antes de darlo por terminado. Se
  corrigió guardando la clave directamente en la fila del pedido en el
  momento en que se genera (columna `clave` nueva en la Data Table), y
  `landing-status` prefiere ese valor sobre el del Worker.
- **Seguridad de `landing-status` sin segundo factor.** El endpoint
  público solo pide el `deviceId` (formato `XXXX-XXXX`, ~32 bits) para
  devolver el estado del pedido y la clave de licencia — no hay ninguna
  otra verificación. Es una decisión consciente (coherente con la UX ya
  elegida por el usuario: "volver y verificar con el deviceId"), mitigada
  con la recomendación de activar un rate limit en Cloudflare sobre esa
  ruta — ver pendiente #20 en `CONTEXTO.md`. **Actualización (2026-08-04,
  más tarde)**: se agregó un segundo factor real (correo) en vez de solo
  el rate limit — ver la entrada de abajo.

---

## 2026-08-04 (más tarde) — Formulario de contacto, estadísticas de visitas, y correo obligatorio en el widget

### Qué se hizo

- **Vista "Sugerencias o contacto"** en el widget (`chatEnviarContacto`,
  acción `contacto`): tipo (sugerencia/problema/otro), nombre y
  contacto opcionales, mensaje obligatorio. Llega a una Data Table
  nueva del bot (`mensajes_contacto`) y avisa al dueño por WhatsApp —
  detalle completo en `capturadocs-bot-pagos/CONTEXTO.md` sección 52.
- **Cloudflare Web Analytics**: snippet manual en el `<head>`, ver
  pendiente #18 resuelto en `CONTEXTO.md` para el porqué del modo
  manual (no automático).
- **Correo obligatorio en "Consultar mi pedido"**: esto lo hizo una
  sesión distinta trabajando en paralelo sobre el mismo repo (avisada
  por mensaje directo entre sesiones) — agregó el campo `chat-estado-email`
  y actualizó `chatConsultarEstado` para mandar `{deviceId, email}` en
  vez de solo `{deviceId}`. Documentado acá porque cambia el contrato
  del widget con el backend, no porque lo haya construido esta sesión.

### Por qué

El dueño pidió "sugerencias/contacto" y "estadísticas de visitas" en la
misma tanda de mejoras — ambas de bajo esfuerzo y sin decisiones
pendientes, a diferencia de la sección de descargas (bloqueada en si
vale la pena generar/firmar un APK) y de promocionar Telegram (bloqueado
en que el bot de Telegram está apagado en producción). El correo
obligatorio en `landing-status` fue una corrección de seguridad
encontrada por otra sesión, no parte de esta tanda de mejoras, pero se
integró sin fricción porque tocaba una parte del widget que esta sesión
no estaba editando al mismo tiempo.

### Problemas encontrados y cómo se resolvieron

- **Dos sesiones de Claude Code editando el mismo repo (y el mismo
  workflow de n8n) al mismo tiempo, sin coordinación previa.** No hubo
  pérdida de trabajo porque las dos sesiones tocaron partes distintas
  del archivo en cada edición puntual (Data Table nueva vs. campo de
  correo en una vista existente; nodos nuevos vs. nodos existentes) —
  pero fue por suerte de scope, no por ningún mecanismo de bloqueo. Se
  verificó explícitamente después (conteo de nodos, pruebas en vivo de
  ambos lados, lectura del archivo real) en vez de asumir que todo
  seguía intacto solo porque el `git commit` no dio error. Lección
  general: cuando se sepa que hay más de una sesión activa sobre el
  mismo repo/workflow, verificar con evidencia (no con el historial de
  git ni con la documentación de la otra sesión) antes de dar algo por
  bueno.
- **Clics simulados por coordenadas no se registraban en el panel del
  chat** al probar en el navegador de la herramienta (tanto en local
  como contra `capturadocs.com` en vivo) — el error decía "the Browser
  pane is not displayed, so the page is not compositing frames". No es
  un bug del widget: se confirmó invocando directamente la misma
  función que dispara el botón (`chatEnviarContacto(boton)`), que sí
  ejecuta el mismo código y la misma llamada de red que un clic real.
  Cuando el clic por coordenadas no registre en este entorno de
  pruebas, no asumir que el código está roto — verificar llamando la
  función directamente antes de reportar un problema.

## 2026-08-21 — Número de WhatsApp centralizado, meta robots y `setup.sh`

### Qué se hizo

- El número de WhatsApp pasó de estar en tres constantes `WA_NUMBER`
  (una por página: `index`, `guia`, `seguridad`) a vivir en un solo
  `config.js` (`window.CAPTURADOCS`), que las tres páginas cargan en el
  `<head>` (Vikunja #64).
- `<meta name="robots" content="index, follow, max-image-preview:large">`
  explícito en las tres páginas (Vikunja #42).
- `setup.sh`: deja el clon listo (activa `core.hooksPath` y comprueba que
  el chequeo del número corra de verdad), en vez de depender de que
  alguien se acuerde del comando suelto (Vikunja #38).

### Problemas encontrados y cómo se resolvieron

- **El refactor rompió el validador que existía para cuidar justo ese
  valor.** `check_wa_number.py` buscaba `WA_NUMBER = '<numero>'` dentro
  de `index.html`; al mover el número a `config.js` dejó de encontrarlo
  y devolvió `1` — o sea, el `pre-commit` habría bloqueado el commit.
  Se reescribió el script para la estructura nueva: ahora lee el número
  de `config.js` y **falla si una página lo vuelve a hardcodear**, si
  una página usa `WA_NUMBER` sin cargar `config.js`, o si `config.js`
  define dos números distintos.

  Lección general: cuando un refactor mueve el dato que un validador
  vigila, el validador es parte del refactor, no algo que se revisa
  después. Y hay que probarlo **en los dos sentidos** — que pase con el
  estado bueno y que falle con uno malo. Acá se verificó simulando un
  `wa.me/573009999999` hardcodeado: el script lo detectó y devolvió `1`.
  Un validador que solo se prueba en verde puede estar aprobando todo.

- **Un `grep` inicial decía que el número estaba repetido en ~10 sitios**
  (así estaba descrita la tarea) pero en realidad eran 3, y ya dentro de
  constantes. La tarea seguía siendo válida, pero mucho más chica de lo
  que decía el tablero — otra razón para verificar contra el código antes
  de estimar.
