# Lecciones aprendidas — CapturaDocs Landing

Registro de decisiones, mejoras y problemas resueltos en este repo, sesión a
sesión. El objetivo es que una sesión nueva entienda el "por qué" detrás de
los cambios sin tener que releer todo el `index.html` ni adivinar por qué se
hizo algo de cierta forma.

Ver también [CONTEXTO.md](CONTEXTO.md) para el sistema de diseño y la
estructura de secciones de la landing.

---

## 2026-08-03 — Revisión general y mejoras de alta prioridad

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

- JSON-LD (`schema.org/SoftwareApplication`) para resultados enriquecidos
  en Google.
- `robots.txt` / `sitemap.xml`.
- Analítica (Google Analytics/Plausible) — hoy no hay forma de medir
  cuántas visitas llegan a WhatsApp vs. rebotan.
- Centralizar el número de WhatsApp (hoy repetido en ~9 lugares) en una
  constante de JS.
- Pendientes ya documentados en `CONTEXTO.md`: #14 (CTAs a la app real en
  vez de solo WhatsApp), #15 (reemplazar maqueta de funciones por captura
  real), #17 (mover hosting de GitHub Pages a Vercel/Netlify).
