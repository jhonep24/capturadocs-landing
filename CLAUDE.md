# capturadocs-landing — puerta de entrada

Landing y guía de CapturaDocs Express (HTML estático, sin build).

## Lee primero (en este orden)
1. `../homelab/ESTADO_PROYECTOS.md` (solo la fila de este proyecto).
2. `CONTEXTO.md` (~86 KB): lee «Qué es este repo» y la sección que toque; «Pendientes conocidos» está congelada (la lista viva es Vikunja).

## No lo leas entero (gasta tokens)
- `LECCIONES_APRENDIDAS.md` (~50 KB): busca por tema con grep.

## Particularidades
- Rediseños: por pasos, vista previa privada (Artifact) y esperar «aprobado» antes de cada push. Colores de marca intocables. El Windows del usuario tiene animaciones apagadas.
- Guía de páginas web: `../guia-web/GUIA_PAGINAS_WEB.md`.

## Reglas comunes
- Pendientes reales: **Vikunja** (http://192.168.0.100:3456), proyecto «CapturaDocs Landing (id 5)». Al terminar algo, cierra la tarea ahí.
- Un dueño por hecho: no copies el mismo dato en dos documentos; deja un puntero.
- Tras un cambio importante, actualiza la doc de este proyecto (`CONTEXTO.md` y `LECCIONES_APRENDIDAS.md`) sin esperar a que te lo pidan.
- Estado de todos los proyectos: `../homelab/ESTADO_PROYECTOS.md`. Avisar a otra sección: bitácora Vikunja «Coordinación» (id 9, tarea 63), comentario con prefijo `[capturadocs-landing]`.
