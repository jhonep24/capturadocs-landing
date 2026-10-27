# Landing — bitácora de septiembre–octubre 2026 (ventas, versiones publicadas, íconos, guías)

> Movido tal cual desde `CONTEXTO.md` el 2026-10-27 para ahorrar tokens. Cronológico; lo vigente de estas decisiones (ventas normales, rediseño B, 1.13.5) está en `CONTEXTO.md`. Contenido:

- Venta solo para escritorio (provisional, desde 2026-09-29)
- El APK de Android publicado (2026-10-01)
- iPhone: la PWA como opción de descarga (2026-10-01)
- El primer respondiente NO se anuncia todavía (decisión, 2026-10-02)
- La 1.10.1 publicada — versión de seguridad (2026-10-03)
- La 1.11.0 publicada — el relato en un cuadro que crece (2026-10-03)
- El APK de campo recompilado — v7 (2026-10-04)
- Una afirmación de privacidad que era incompleta y hoy sí es exacta (2026-10-04)
- La 1.12.0 publicada — primer cliente con las capas de seguridad (2026-10-08)
- La 1.13.0 (.exe) y el APK v8 publicados (2026-10-10)
- La 1.13.1 (.exe) y el APK v9 — Fase 1 de la auditoría (2026-10-15)
- Videos tutoriales en `guia.html` (2026-10-16)
- Android ahora genera documentos (2026-10-16)
- Íconos profesionales y animaciones (2026-10-22)
- Guías terminadas y publicadas (2026-10-20)
- Guía paso a paso en PDF (2026-10-16) — hecha, SIN publicar
- 1.13.4 publicada (2026-10-26)
- 1.13.3 publicada (2026-10-23)
- 1.13.2 publicada (2026-10-23)

## Venta solo para escritorio (provisional, desde 2026-09-29)

> ⚠️ **REVERTIDO el 2026-10-17** — ver "Vuelven las ventas normales" más abajo. Esta
> sección se deja como historia (qué se tocó y por qué); **ya no describe la landing.**

**Esto es temporal y está pensado para revertirse.** Mientras dure, la landing
vende solo la versión de computador; la de celular existe pero no se ofrece
(ver `README_VERSION_CAMPO.md` en `informes-ponal`: el APK de campo captura el
caso y lo envía al PC, que es donde se generan los documentos).

Qué se cambió, todo en **un solo commit** para poder deshacerlo con
`git revert <sha>`:

- Las cuatro tarjetas de planes dicen "Para computador con Windows" en vez de
  "Web, Android y Windows".
- **"Empezar gratis" ahora baja el instalador.** Antes apuntaba a la versión
  web, que desde un computador muestra la página de bloqueo del portero y lo
  manda a descargar la app igual — un rodeo sin sentido si solo se vende
  escritorio.
- La sección Descargas se queda solo con Windows (las tarjetas de Android e
  iPhone estaban en "Próximamente"). La rejilla pasa a una columna acotada: con
  una sola tarjeta, las tres columnas la dejaban pegada a la izquierda.
- Las preguntas frecuentes y la ficha `operatingSystem` dejan de prometer
  celular.

**Lo que NO se tocó, a propósito:** los términos y condiciones siguen diciendo
que la licencia vale en la app de Android. Es texto legal frente a clientes que
YA pagaron esperando usarla en su celular; recortarlo es una decisión distinta
de dejar de anunciarlo, y la tomó el dueño (2026-09-29) al escoger el alcance.

**Para volver atrás:** `git revert` del commit y push. La página queda
exactamente como estaba, incluidas las tarjetas de Android e iPhone.

### Segunda parte: solo se vende Estación (2026-10-01)

También provisional, también en **un solo commit** para revertirlo igual. Se
retiran de la venta las licencias **Semanal y Mensual**; quedan visibles la
prueba gratuita y Negocio/Estación.

No basta con quitar las dos tarjetas: los planes vivían en cinco sitios más, y
dejar cualquiera habría permitido seguir pidiéndolos.

- Las tarjetas (la rejilla pasa de 4 a 2 columnas acotadas).
- **Las dos listas del chat**: la de cotizar y la de enviar comprobante. Esta es
  la importante — sin tocarla, el cliente seguía escogiendo "Semanal" y pidiendo
  esa licencia aunque la tarjeta ya no estuviera.
- La ficha de precios de la página (`schema.org`), que es lo que leen Google y
  las redes al mostrar el enlace.
- Los textos que decían que la IA era "exclusiva de Mensual y Negocio/Estación"
  y que Estación "cuesta más que la mensual" — comparaciones con un plan que ya
  no se ofrece.

**Efecto secundario conocido:** quien hubiera acordado por WhatsApp un precio
semanal o mensual ANTES del cambio ya no puede reportar su pago desde el chat,
porque esa opción desapareció de la lista de comprobantes. Ese caso se atiende
por WhatsApp directamente.

**Lo que NO se tocó:** la Política de Licencias sigue describiendo las licencias
semanal y mensual. Quien ya compró una se rige por ese texto; retirarlo sería
cambiarle las condiciones a un cliente que ya pagó.

**Faltaba un sitio, reportado por el usuario el mismo día:** la vista
"Ver precios" del chat. Esa lista **no sale de esta página: la sirve el bot**
(`chat.capturadocs.com/webhook`, acción `precios`), y el bot sigue devolviendo
los cuatro planes. El chat pintaba tal cual lo que recibía, así que ahí seguían
la semanal y la mensual aunque las tarjetas y los desplegables ya no estuvieran.

Se filtra en la landing con `CHAT_PLANES_EN_VENTA = ['N']` en vez de cambiar el
bot: así todo el cambio provisional vive en un solo repositorio y se revierte de
una sola vez, sin tocar el bot de pagos (donde además trabajan otras sesiones).

**Consecuencia que hay que tener presente:** el bot sigue conociendo y
devolviendo esos precios. Si el bot cotiza por WhatsApp o Telegram, ese camino
NO está cubierto por este filtro — hay que revisarlo aparte.

## El APK de Android publicado (2026-10-01)

La app de Android vuelve a estar en Descargas. **No es la app completa**:
captura el caso en el celular y lo envía al computador en un `.cdx`; los
documentos se generan en la app de Windows. Es la rama `apk-solo-cdx` de
`informes-ponal` (ver su `README_VERSION_CAMPO.md`).

Se presenta como una descarga normal, igual que Windows, por decisión del
dueño (2026-10-01) y a pesar de la advertencia de que quien la instale esperando
que genere documentos va a escribir preguntando.

**Detalle técnico que NO se puede perder de vista:** el APK vive en su propia
release, creada con **`--latest=false`**, y la landing enlaza a la **URL del
tag**, no a `releases/latest/download/`. El tag vigente es
`v1.8.5-campo-android-v7` (ver abajo, 2026-10-04); el primero fue
`v1.8.5-campo-android`.

El motivo: `latest/download/` resuelve a la release marcada como *Latest*, y
solo puede haber una. Si la del APK se hubiera llevado esa marca, **el botón de
descarga de Windows habría dejado de funcionar**. Al publicar una versión nueva
del APK hay que repetir las dos cosas: `--latest=false` y actualizar el enlace
al tag nuevo.

Se ajustaron además dos textos que habrían quedado mintiendo: la respuesta de
"¿funciona en celular?" decía que la versión de celular no se ofrecía, y la
ficha `operatingSystem` decía solo Windows.

**Ojo con retirarlo:** ese APK tiene un apagador (`MIN_APP_VERSION` a 1.9.0 lo
bloquea al instante, ver `README_VERSION_CAMPO.md`). Publicado en la landing,
ese apagador alcanza a cualquiera que lo haya descargado, no solo a conocidos.

## iPhone: la PWA como opción de descarga (2026-10-01)

La tarjeta de iPhone ya no dice "Próximamente": enlaza a
`https://capturadocs-app.capturadocs.workers.dev/`, que es la PWA.

**No es un archivo que se instale**: es una dirección web que el iPhone abre y
que se puede añadir a la pantalla de inicio. Por eso el botón dice "Abrir en
iPhone" y no "Descargar". Ese Worker **solo deja pasar a iPhone**
(`worker-gate.js` bloquea Android y Windows con un aviso que los manda a su
propia app), así que no hay riesgo de que alguien entre por ahí desde un PC.

Igual que el APK, esa PWA es la versión de **captura en campo**: no genera
documentos, captura el caso y lo envía al computador (ver
`informes-ponal/README_VERSION_CAMPO.md`). Se compila desde la rama
`apk-solo-cdx` — el flujo `deploy-app.yml` quedó apuntando ahí.

Las tres tarjetas de Descargas quedan: Android (APK), iPhone (PWA) y Windows
(instalador). La rejilla vuelve a sus tres columnas de siempre.

## El primer respondiente NO se anuncia todavía (decisión, 2026-10-02)

`index.html` no menciona el proceso de **primer respondiente** ni el **FPJ-4**,
y dice "5 documentos" — que es lo correcto para flagrancia, el proceso que la
página vende. **No es un olvido: es a propósito.** Ese proceso sigue en pruebas
y por eso ni siquiera descuenta generaciones de la licencia (ver el comentario
de `handleGenerarFPJ4` en `informes-ponal/src/App.jsx`).

`guia.html` **sí** lo documenta, porque quien ya tiene la app lo tiene
disponible y necesita saber cómo usarlo. Esa asimetría es deliberada.

Cuando se implemente bien y se decida anunciarlo, hay que tocar: el título y la
descripción de la página (hoy dicen "informes de captura en flagrancia"), la
tarjeta de "5 documentos simultáneos", el paso 03 de "Cómo funciona" y la ficha
de ofertas.

## La 1.10.1 publicada — versión de seguridad (2026-10-03)

Release `v1.10.1-windows-exe`, marcada *Latest*. Procedimiento de arriba
seguido tal cual, incluido el paso 4: el hash de `seguridad.html`
(`1ca8f227…`) se sacó **bajando el archivo desde la URL pública**, y coincide
con el del archivo local.

No cambia nada visible ni de uso. Lleva tres arreglos de seguridad:

- Electron 43.4.0 → 43.7.7 (cuatro avisos *high* del propio Electron).
- El servidor interno de la app ya no se sale de su carpeta por un error al
  comparar rutas con `startsWith`.
- Se cerró el camino para estirar el periodo de prueba trabajando sin
  internet.

**`MIN_APP_VERSION` se queda en 1.8.5, a propósito.** Subirla a 1.10.1
apagaría de un golpe el APK de campo (que está marcado 1.8.5 justamente para
poder apagarlo cuando se quiera) y además dejaría fuera a quien tenga la
1.10.0 instalada y todavía no actualice. Esta versión no arregla nada que
obligue a forzar la actualización.

El enlace del APK sigue apuntando a su **tag**
(`releases/download/v1.8.5-campo-android/...`), no a `latest`, así que
publicar un `.exe` nuevo como *Latest* no lo rompe. Verificado.


## La 1.11.0 publicada — el relato en un cuadro que crece (2026-10-03)

Release `v1.11.0-windows-exe`, marcada *Latest*. Procedimiento de arriba
seguido tal cual, incluido el paso 4: el hash de `seguridad.html`
(`11d42a6c…`) se sacó **bajando el archivo desde la URL pública**, y coincide
con el del archivo local.

**Qué cambia para el cliente**: en el primer respondiente, la narración de los
hechos ya no se parte en los 13 renglones del formato impreso — va en un solo
cuadro que se agranda. El texto ya no se corta, los puntos y aparte se
respetan y queda justificado. Cierra de raíz dos problemas que el usuario
había reportado (texto cortado a mitad del relato, texto que se salía de la
caja). Además las tipografías viajan dentro de la app, así que se ve igual sin
señal.

**`MIN_APP_VERSION` se queda en 1.8.5**, por lo mismo que en la 1.10.1:
subirla apagaría el APK de campo y dejaría fuera a quien no haya actualizado.
Nada de esta versión obliga a forzar la actualización.

El enlace del APK sigue apuntando a su **tag**, no a `latest`, así que
publicar este `.exe` como *Latest* no lo rompe. Verificado otra vez.

## El APK de campo recompilado — v7 (2026-10-04)

Release `v1.8.5-campo-android-v7`, con **`--latest=false`** y el enlace de la
landing apuntando a ese tag, igual que siempre (ver "El APK de Android
publicado" más arriba para el porqué). Verificado después: el `.exe` **sigue
siendo *Latest*** y las dos descargas responden.

**SHA-256**: `c14a92f06de93726832cc4f4865f30b59855d1d228fd903ca9a71f4316cdafcf`,
sacado del archivo **bajado desde la URL pública**, y publicado en
`seguridad.html` como "Android v7".

**No cambia nada de lo que el cliente ve ni de cómo se usa.** Lo que trae es que
las tipografías ahora viajan dentro del APK: antes se descargaban de internet en
cada arranque, así que **sin señal la app se veía con otra letra** — y sin señal
es justo cuando se usa en campo. Se acotó además un permiso interno de compartir
archivos que abarcaba más de lo necesario.

**El APK sigue marcado 1.8.5**, y eso es a propósito: de ese número depende el
apagador de la versión de campo. Lo que subió es el `versionCode` (6 → 7), que
es lo único que Android exige para instalar encima. Se instala sobre el anterior
sin desinstalar y sin perder casos guardados, porque va firmado con el **mismo
certificado**.

El detalle de los dos cambios vive en `informes-ponal`: `README_TECNICO.md`
(Errores 64 y 65) y `README_VERSION_CAMPO.md` (sección del `versionCode 7`).

## Una afirmación de privacidad que era incompleta y hoy sí es exacta (2026-10-04)

`index.html` dice, y sigue diciendo:

> La conexión a Internet se usa **únicamente** para verificar tu licencia y
> consultar actualizaciones.

Hasta el 2026-10-04 eso **no era del todo cierto**, y nadie lo había notado: la
app también le pedía las tipografías a `fonts.googleapis.com` en cada arranque,
con lo que Google recibía la IP y el equipo desde el que trabaja un policía. No
viajaban datos del caso, así que el fondo del mensaje se sostenía, pero el
"únicamente" no.

Salió de la auditoría del APK, no de una revisión de los textos. **No hubo que
cambiar la frase: se cambió la app para que la frase fuera verdad** — las
tipografías ahora viajan dentro (ver el registro del APK v7 más arriba, y
`informes-ponal/README_TECNICO.md`, Error 64). Los tres canales ya quedaron así.

Vale como recordatorio para los textos de esta landing: una afirmación
absoluta ("únicamente", "nunca", "jamás sale de tu dispositivo") hay que poder
sostenerla mirando el tráfico real de la app, no la intención con la que se
escribió. Si algún día se agrega algo que llame a un tercero —una fuente, un
icono, una analítica, un mapa— esta frase es la primera que hay que revisar.

## La 1.12.0 publicada — primer cliente con las capas de seguridad (2026-10-08)

Release `v1.12.0-windows-exe`, marcada *Latest*. Hash de `seguridad.html`
(`24537c7f…`) sacado del archivo **bajado desde la URL pública**, coincide.

Es el primer `.exe` que lleva la defensa en profundidad del candado de licencia
(marca de agua invisible, verificación Ed25519 del token, candado 3b) — todo en
**modo gracia**: nada bloquea, nada cambia para el usuario. El Worker ya firma
tokens (secreto `TOKEN_PRIV_KEY` cargado y desplegado antes). El bloqueo real
sigue apagado hasta prender `enforceToken`. Detalle en
`informes-ponal/README_TECNICO.md`, sección 7b.

El enlace del APK sigue apuntando a su **tag** (`v1.8.5-campo-android-v7`), no a
`latest`, así que publicar este `.exe` como *Latest* no lo rompe. Verificado.

## La 1.13.0 (.exe) y el APK v8 publicados (2026-10-10)

Dos releases, ambos con el hash sacado del archivo **bajado de la URL pública**
(coinciden):
- **`v1.13.0-windows-exe`** (*Latest*), SHA `55f1f120…`. Trae: ofuscación del
  candado de licencia, firma por documento (#5 liviana), y dos arreglos — el
  resumen avisa si falta la dirección de los hechos, y el acta de derechos ya
  no se pasa a una tercera hoja.
- **`v1.8.5-campo-android-v8`** (`--latest=false`), SHA `5c57b5a9…`. Solo trae
  el aviso de dirección de los hechos (lo demás no aplica a la versión de campo,
  que no genera documentos). versionCode 8, versionName sigue 1.8.5.

El enlace del APK apunta a su **tag** (`v8`), no a `latest`, así que publicar el
`.exe` como *Latest* no lo rompe. Verificado que ambas descargas responden.

Pendiente de seguridad que sigue abierto (decisión del dueño): firmar el `.exe`
(Authenticode) para quitar la alerta de SmartScreen y endurecer la
redistribución. Y prender `enforceToken` cuando la base ya esté en 1.12.0+.

## La 1.13.1 (.exe) y el APK v9 — Fase 1 de la auditoría (2026-10-15)

Release de seguridad de la **Fase 1** de la auditoría de código (ver
`informes-ponal/AUDITORIA_SEGURIDAD_2026-10.md`, que vive solo local, no en el
repo). Dos releases, ambos con el hash sacado del archivo **bajado de la URL
pública** (coinciden):
- **`v1.13.1-windows-exe`** (*Latest*), SHA `1c64c864…`. CSP en la app +
  cabeceras de seguridad (X-Frame-Options/nosniff/Referrer-Policy) en el server
  local de Electron. Sigue sin firmar (Authenticode pendiente).
- **`v1.8.5-campo-android-v9`** (`--latest=false`), SHA `8a3f67c7…`. Lo de
  verdad importante del APK: **`@capacitor/android` 8.4.1 → 8.5.3**, que cierra
  GHSA-rvm3-566m-v7fv (carga de contenido remoto en el origen vía el proxy HTTP
  interno de Capacitor) — la única vuln de dependencia que viajaba en el APK.
  Más la CSP. versionCode 9, mismo certificado que v8 (instala encima),
  versionName sigue 1.8.5-campo. Obligó a compilar con **JDK 21** (el JBR de
  Android Studio): Capacitor 8.5.x subió el toolchain mínimo.
- La **PWA de iPhone** también recibió la CSP + cabeceras (se compila desde
  `apk-solo-cdx`, verificado en vivo con User-Agent de iPhone).

El enlace del APK en la landing se actualizó a su nuevo **tag** (`v9`), no a
`latest`, así que el `.exe` como *Latest* no lo rompe. Verificado: ambas
descargas responden 200 y los hashes de `seguridad.html` cuadran con lo
publicado.

Mitigado de paso (ya estaba): A3 de la auditoría — las PCs de producción
corren `npm run produccion` (build + preview), no el `vite dev`, así que el
aviso de esbuild del dev-server no aplica.

## Videos tutoriales en `guia.html` (2026-10-16)

El usuario quiere videos de cómo usar el programa. Se montó la **infraestructura**
y los guiones; los videos los graba y sube él.

- **Cuatro videos**, cada uno dentro de la sección de la guía que ya explicaba lo
  mismo (no se creó página ni sección nueva): `instalar` (sección 1), `licencia`
  (3), `diligenciar` (4) y `rotulo` (6, "dónde quedan los archivos e imprimir al
  60 %"). Los guiones, las reglas de grabación y cómo subirlos viven en
  **`GUIONES_VIDEOS.md`** — dueño de ese hecho, no copiarlo acá.
- **Los IDs viven en `config.js`** (`window.CAPTURADOCS.VIDEOS`), el mismo patrón
  que el número de WhatsApp. **Un ID vacío o inválido deja el hueco oculto**
  (`hidden`): no hay portadas rotas ni espacios vacíos, así que se puede publicar
  uno a uno. Hoy los cuatro están vacíos, o sea que la guía se ve igual que antes.
- **Alojamiento: YouTube, dominio `youtube-nocookie.com`, carga al dar play.**
  Decisión del usuario (2026-10-16) entre YouTube / archivos propios / solo
  enlaces. La portada es propia (botón con ▶ y el título): **no se pide ni la
  miniatura a YouTube**, porque eso ya sería una conexión a un tercero antes de
  que el visitante decida nada. El `<iframe>` se crea solo en el clic. Se verificó
  en vista previa que antes del play hay cero peticiones a YouTube/Google.
- **Defensa:** el ID se valida con `/^[A-Za-z0-9_-]{11}$/` antes de armar la URL
  y los textos se ponen con `textContent`, nunca `innerHTML`; un valor raro en
  `config.js` no puede inyectar nada.
- **Pendiente de privacidad (decisión del usuario, no hecho):** cuando se publique
  el primer video, `guia.html` hará una conexión a YouTube al dar play. La
  portada ya lo avisa en la propia página, pero el **modal de Privacidad no lo
  menciona** (tampoco menciona hoy Google Fonts ni Cloudflare Web Analytics, que
  la landing ya usa). Es texto legal: redactarlo con visto bueno del usuario.
  Esto es de la **página web**, no de la app — la frase "únicamente para verificar
  licencia y consultar actualizaciones" habla del software y no se afecta.
- **Mantenimiento:** los videos 2, 3 y 4 muestran pantallas de la app. Si cambia
  un nombre de botón, el orden de pasos o la carpeta de guardado, hay que repetir
  la escena y corregir a la vez el texto de la sección (mismo cuidado que ya hay
  con la guía escrita). Por eso los guiones piden **no decir precios ni versiones**.

## Android ahora genera documentos (2026-10-16)

El canal **Android** de la landing pasó a ser la **app completa** (que genera
todos los documentos en el teléfono), reemplazando al APK de campo (que solo
capturaba y enviaba el caso al PC). Decisión del dueño.

- Release: **`v1.13.1-android`** (`--latest=false`), asset
  `CapturaDocs.Express.Android.apk`, SHA `c15e4685…`. Se compila desde `main`
  (con generadores), versionCode 10, mismo certificado que el de campo (v8/v9):
  se instala **encima** conservando los casos. El `.exe` sigue siendo *Latest*.
- Se actualizó el botón de descarga (apunta al tag `v1.13.1-android`), el hash
  de `seguridad.html` (etiqueta "Android v1.13.1") y el texto que describía el
  celular como "solo captura": ahora **Windows y Android generan**, y **solo el
  iPhone** (PWA, que se sigue compilando desde `apk-solo-cdx`) captura y envía
  al computador.
- ⚠️ Nota de seguridad: la app completa lleva los generadores y plantillas
  dentro del APK; a diferencia del de campo, eso permite generar sin pagar a
  quien manipule el teléfono (hueco conocido de la generación client-side).
  Decisión de negocio asumida. El apagador del APK de campo (MIN_APP_VERSION
  por APP_VERSION 1.8.5) sigue disponible si se quiere forzar a los equipos de
  campo a migrar.

## Íconos profesionales y animaciones (2026-10-22)

Los programadores a quienes el dueño mostró la landing dijeron que "parecía hecha con IA".
Se probó una portada totalmente nueva (papel/azul) y **el dueño la rechazó**: quiere
**mantener colores y estilo** (azul marino + dorado) y solo cambiar dos cosas.
- **Emojis → íconos Lucide** (licencia ISC): sprite propio `icons.svg`, usado con
  `<svg class="ic"><use href="icons.svg#i-NOMBRE"/></svg>`; hereda `currentColor`, tamaño
  `1em`. Aplicado en `index.html`, `guia.html`, `seguridad.html` (incl. el chat). Para un
  ícono nuevo: copiar su `<path>` de `lucide-static` como `<symbol id="i-…">` en `icons.svg`.
  Los `✓` `✕` de listas/comparación se dejaron (son tipografía, no emoji). **No poner
  emojis/íconos dentro de atributos HTML ni de `textContent`** (no renderizan SVG).
- **Animaciones** (CSS + un `<script>` al final de `index.html`, sin librerías): aparición al
  hacer scroll con retraso escalonado (`.rv`/`.on`, solo si hay JS), barra de progreso
  superior, nav que se compacta, contadores de la portada, brillo del botón principal,
  elevación/ícono en tarjetas, resplandor del plan destacado. Todo respeta
  `prefers-reduced-motion`.
- Sin plugins extra: se usó `frontend-design` solo como guía; `audit-suite` no se instaló.

### Segunda ronda: animación "fuera del molde" (2026-10-22)
El dueño dijo que las animaciones de aparición/hover **no se notaban** y pidió algo radical.
- **Escena de scroll `#escena`** (después de la portada, antes de "Cómo funciona"): sección
  fijada (`position:sticky`, pista de 430vh; 520vh en móvil) donde **el scroll dirige la
  animación**: se escribe un formulario (4 campos con cursor) → "fichas" doradas vuelan por
  curvas Bézier a cada uno de los 5 documentos → sellos "LISTO" → tarjeta de descarga. Texto de
  4 pasos que se resalta según el avance. Es JS propio (~60 líneas, sin librerías); fases por
  `p` (0–1): escribir 0–.28, volar .30–.66, sellar .70–.90, listo .93. Datos de ejemplo
  inventados. Con `prefers-reduced-motion` se muestra el estado final sin pista larga.
- Portada: el título sube **palabra por palabra** desde una máscara; botón principal con imán
  hacia el cursor; foco de luz dorado que sigue al cursor en tarjetas de plan, testimonios y pasos.
- Se probó con `matchMedia` forzado a "sin reducir movimiento" (el panel del navegador lo
  emula siempre activo): para ver la animación real hay que abrir la página en un navegador normal.

**Por qué el dueño "no veía" la animación (2026-10-22):** su Windows tiene **desactivadas
las animaciones del sistema** (`SystemParametersInfo(SPI_GETCLIENTAREAANIMATION)` = False), así
que el navegador reporta `prefers-reduced-motion: reduce` y la página mostraba el estado final.
Es el mismo motivo por el que el panel de pruebas de la app siempre ve la escena "quieta".
Solución: la detección vive en un `<script>` del `<head>` (`window.__quieto`, clase `html.quieto`;
el CSS de movimiento reducido ahora cuelga de `html.quieto`, no de la media query) y la sección
muestra un botón **"Activar la animación de esta sección"** (guarda `cd-mov=1` en
`localStorage` y recarga). Se sigue respetando la preferencia por defecto. Ojo al probar:
`requestAnimationFrame` no corre si el panel del navegador está oculto.

## Guías terminadas y publicadas (2026-10-20)

El dueño pidió entregar las guías ya terminadas. Se cerró:
- **PDF (14 págs.) publicado** en `guia-pdf/` y enlazado desde `guia.html` (botón
  "Descargar la guía en PDF" y enlace en el índice). Las 3 imágenes pendientes se
  resolvieron como **ilustraciones** (ver `guia-pdf/LEEME.md`), no capturas reales.
- **`guia.html`**: sección 1 con aviso de SmartScreen, sección 2 con "Configuración
  inicial" (Vikunja #165, #167). El PDF tiene también el aviso de SmartScreen.
- **Política de privacidad** (punto 7 del modal de `index.html`): se agregaron Google
  Fonts, YouTube (solo al dar play) y Cloudflare Web Analytics; fecha → octubre 2026 (#164).
- **Videos (#163)**: siguen sin grabar; los 4 huecos están ocultos hasta que
  `config.js` `VIDEOS` tenga los IDs. Es lo único que depende del dueño.

## Guía paso a paso en PDF (2026-10-16) — hecha, SIN publicar

El usuario pidió una guía **descargable para estudiar**, con capturas. Vive en
`guia-pdf/` (cómo regenerarla y qué hay dentro: **`guia-pdf/LEEME.md`**, dueño de
ese detalle, no copiarlo acá). Decisiones que conviene no perder:

- **Las capturas las genera un script, no una persona.** Abre la app (`origin/main`
  de `informes-ponal`) con Playwright, red simulada y datos inventados; así cuando
  cambie la app se regenera con `sh guia-pdf/regenerar.sh` (~1 min) en vez de
  volver a tomar 13 pantallas. Reutiliza `aislarRed()` de `e2e/utilidades.js` de la
  app, que ya corta el internet y simula el Worker: **nada llega a producción**.
- **Se captura desde una copia limpia de `origin/main`**, no desde el directorio de
  `informes-ponal`: ahí suele haber cambios sin commitear de otra sesión (el
  15-oct eran los de licencia y la auditoría de seguridad) y servir eso a medias
  habría dado capturas de algo que no está publicado.
- **Recortadas a la zona útil.** Una captura de pantalla completa en una hoja A4
  deja el texto de la app en ~5 pt; recortada a la tarjeta central, en ~8 pt.
- **Sin precios.** El modal de licencia muestra botones de plan con precios; en el
  PDF se reemplazan por "Plan disponible", porque el archivo circula meses.
- **El botón "Abrir carpeta del caso" sí sale**, aunque la captura es de la versión
  web: la app solo lo pinta si existe `window.electronAPI`, y el script lo declara
  para mostrar la pantalla real de la app instalada (ver `prepararRed`).
- **Faltan 3 imágenes que no salen de la app** (Explorador, Word *Guardar como PDF*
  y cuadro de impresión al 60 %): el usuario las tiene que tomar y dejar en
  `guia-pdf/generador/img-usuario/` (`explorador.png`, `word-pdf.png`,
  `imprimir-escala.png`). Las 5 que pegó en el chat el 11-ago NO quedaron guardadas
  en disco, hay que pedirlas como archivos. Sin ellas el paso 12 sale solo con texto.
- **Pendiente para publicar:** (1) las 3 imágenes; (2) visto bueno del usuario al
  PDF; (3) subir el `.pdf` al repo y poner un botón "Descargar la guía en PDF" en
  `guia.html`; (4) agregar el PDF al `sitemap.xml` solo si se quiere indexar.

**Hallazgos de esta tarea que NO son de la landing** (la app es de otra sección;
quedaron como tareas en Vikunja, no se tocaron):

- **La app trae de fábrica un NUNC y una URI que parecen reales.** `src/borrador.js`
  (líneas ~14-17) deja como predeterminado de cualquier equipo nuevo
  `nunc: "1100160000172026"` y `destino: "URI ENGATIVÁ LA GRANJA"`, y la pantalla
  "Configuración inicial" los muestra precargados a todo usuario que instala. Un
  NUNC identifica un caso. Si son de una estación o un caso real, están en el
  instalador público. En las capturas se reemplazaron por valores inventados.
- ~~El modal de licencia de la app ofrecía Semanal y Mensual aunque la landing vendía solo Estación~~ — **resuelto 2026-10-17**: se venden los tres planes otra vez, ya no hay discrepancia.
- **"Configuración inicial" no está en `guia.html`.** Tras registrar el correo la app
  pide NUNC, departamento, municipio y destino; la sección 2 de la guía en línea no
  lo menciona (el PDF sí, paso 3).

## 1.13.4 publicada (2026-10-26)

Arregla DE VERDAD la fecha gris del FPJ-4 (y la hora que no aparecía). **No era
la caché** (ese fue el diagnóstico equivocado de la 1.13.3): se reproducía hasta
en un documento generado desde cero, sin Electron. Dos causas de formato OOXML:
la fecha heredaba el color de TEMA del texto guía (`themeColor` gris, que Word
usa ignorando el `w:val` negro), y las casillas de la hora tenían una sangría
grande que empujaba el dígito fuera de la casilla. Además, la fila de encabezado
(Depto/Municipio/Fecha/Hora) quedó centrada. Afecta a los 3 canales (no solo el
`.exe`), por eso se publicó en todos.

- **`v1.13.4-windows-exe`** (*Latest*), SHA `7007da1a…`.
- **`v1.13.4-android`** (`--latest=false`), SHA `54cc17e7…`, versionCode 13.
- PWA redesplegada desde `main` (commit del fix + docs).

## 1.13.3 publicada (2026-10-23)

Arregla un bug SOLO del `.exe`: tras actualizar, los documentos se generaban
con las plantillas VIEJAS (la fecha del FPJ-4 salía gris) porque el Chromium
de Electron cacheaba las plantillas (URL fija) y la caché sobrevíve a
reinstalar. Fix: el server local manda `Cache-Control: no-store`. Instalar la
1.13.3 encima lo resuelve (reinstalar la 1.13.2 NO, por la caché).

- **`v1.13.3-windows-exe`** (*Latest*), SHA `11caa75c…`.
- **`v1.13.3-android`** (`--latest=false`), SHA `45c0e8b4…`, versionCode 12
  (Android no tenía el bug; se alinea a 1.13.3). PWA redesplegada.

## 1.13.2 publicada (2026-10-23)

Release de los ajustes del **primer respondiente (FPJ-4)** + arreglos de la
sesión. Dos releases, hashes bajados de la URL pública (coinciden):
- **`v1.13.2-windows-exe`** (*Latest*), SHA `e56a87ba…`.
- **`v1.13.2-android`** (`--latest=false`), SHA `6019c559…`, versionCode 11,
  mismo certificado que v10 (se instala encima). App completa (genera).
- **PWA** redesplegada desde `main` (app completa, 1.13.2).

Cambios: en primer respondiente, capturados arranca en 0, la fecha del FPJ-4
sale en negro, y la hora de la actuación se usa tal cual la escribe el policía
(la narración queda en blanco). Más: candado offline más estricto por
vencimiento, registro de errores de generación en `/admin/errores`, y carga de
plantillas robusta. Se actualizaron los enlaces y los hashes de `seguridad.html`.
