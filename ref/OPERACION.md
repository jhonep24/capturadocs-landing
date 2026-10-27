# Landing — procedimientos de operación (instaladores, hash del .exe, verificación de WhatsApp)

> Movido tal cual desde `CONTEXTO.md` el 2026-10-27 para ahorrar tokens. Cómo regenerar los instaladores Android/Windows, cómo publicar una versión nueva del `.exe` y cómo verificar el número de WhatsApp (`check_wa_number.py`).

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
   En esta máquina vive en `C:/Users/Jhon/jdk21/jdk-21.0.12+8` — **con el
   subdirectorio**; apuntar `JAVA_HOME` a `jdk21` a secas falla.
4. `JAVA_HOME=<ruta-jdk21> ./gradlew.bat assembleRelease` dentro de
   `informes-ponal/android` → genera `app/build/outputs/apk/release/app-release.apk`.
5. **Subir `versionCode` en `android/app/build.gradle` en cada APK que se
   distribuya.** Android se niega a instalar encima uno cuyo `versionCode` no
   sea mayor: falla con "aplicación no instalada" y toca desinstalar, lo que
   borra los casos guardados. El 2026-09-29 estaba en 1 con `versionName
   "1.6"` mientras la app iba por la 1.9.0 (quedó en 2 / "1.9.0").
6. **Verificar el artefacto, no el código de salida.** `gradlew` sale con 0
   aunque `JAVA_HOME` sea inválido y no compile nada. Y `jarsigner -verify`
   dice "jar is unsigned" en un APK que sí está firmado, porque solo entiende
   el esquema v1: usar `apksigner verify` y `aapt2 dump badging` de las
   build-tools del SDK.

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

En su lugar, `check_wa_number.py` (raíz del repo) verifica que el número
esté en un solo lugar, y está enganchado como git hook en
`.githooks/pre-commit`.

**Dónde vive el número (actualizado 2026-08-21, Vikunja #64)**: en
`config.js`, dentro de `window.CAPTURADOCS`. Antes cada página tenía su
propia constante `WA_NUMBER` (index, guia y seguridad: tres copias del
mismo número, y cambiarlo obligaba a acordarse de las tres). Ahora las
páginas cargan `config.js` en el `<head>` y leen
`window.CAPTURADOCS.WA_NUMBER`.

Si cambia el número: se toca **solo `config.js`**. El hook falla si
alguien vuelve a hardcodearlo en una página, si una página usa
`WA_NUMBER` sin cargar `config.js`, o si `config.js` define dos números
distintos.

**El hook no se activa solo** — git no ejecuta nada al clonar, a
propósito. Por eso hay un `setup.sh` (Vikunja #38) que se corre una vez
por clon y además comprueba que el chequeo realmente pase:

```bash
./setup.sh
```

## Publicar una versión nueva del `.exe` (2026-09-28)

El instalador NO vive en este repo: pesa ~117 MB y GitHub rechaza archivos de
más de 100 MB. Va como **asset de una GitHub Release** de este mismo repo, y
el botón de la landing apunta a `releases/latest/download/<nombre>`, que
resuelve solo a la release marcada como *Latest*.

Pasos, en este orden:

1. Compilar en `informes-ponal` (`npm run electron:build`) con la app cerrada
   y sin el servidor de desarrollo corriendo.
2. Copiar el `.exe` a un nombre **sin espacios** (`CapturaDocs.Express.Setup.
   <version>.exe`): GitHub convierte los espacios en puntos y así el nombre
   del asset no depende de esa conversión.
3. `gh release create v<version>-windows-exe <archivo> --repo
   jhonep24/capturadocs-landing --title ... --notes ...`
4. **Bajar el archivo desde la URL pública** (`releases/latest/download/...`)
   y calcularle el SHA-256. Ese, y no el del archivo local, es el que se
   publica.
5. Actualizar en la landing: el enlace de descarga y la línea "Versión
   actual" de `index.html`, y el hash + la etiqueta de versión + el nombre en
   el ejemplo de `certutil` de `seguridad.html`.
6. Commit y push (esto ya publica, ver abajo).

**El hash vive en UN solo lugar**, `seguridad.html`, y tiene que salir del
archivo realmente subido. Un hash que no corresponde le dice al cliente que
el instalador fue manipulado — ya pasó una vez.

Hasta el 2026-09-28 la landing ofrecía la **1.6.10** aunque la app ya iba por
la 1.8.0: publicar una versión nueva de la app y actualizar la landing son
dos tareas distintas, y la segunda se había quedado atrás tres versiones.
