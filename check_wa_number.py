#!/usr/bin/env python
"""Verifica que el numero de WhatsApp del sitio sea uno solo.

Historia: en #19 (2026-08-11) el numero salio del HTML hardcodeado y paso a
una constante JS (WA_NUMBER) por pagina. En #64 (2026-08-21) esa constante
salio de cada pagina y quedo en un unico `config.js` (window.CAPTURADOCS),
porque estaba repetida en index/guia/seguridad y cambiarla obligaba a
acordarse de las tres.

Este script revisa que:
  1. `config.js` defina exactamente un WA_NUMBER.
  2. Ninguna pagina haya vuelto a hardcodear un numero (ni en una constante
     propia, ni en un enlace `wa.me/<numero>`).
No modifica nada del sitio en produccion -- corre solo en dev, antes de
comitear (ver .githooks/pre-commit).
"""
import re
import sys
from pathlib import Path

CONFIG = "config.js"
PAGINAS = ["index.html", "guia.html", "seguridad.html"]


def main():
    ruta_config = Path(CONFIG)
    if not ruta_config.exists():
        print(f"[check_wa_number] ERROR: falta {CONFIG}, que es donde debe vivir el numero.")
        return 1

    config = ruta_config.read_text(encoding="utf-8")
    en_config = re.findall(r"WA_NUMBER\s*:\s*'(\d+)'", config)

    if not en_config:
        print(f"[check_wa_number] ERROR: no se encontro WA_NUMBER en {CONFIG}.")
        return 1
    if len(set(en_config)) > 1:
        print(f"[check_wa_number] ERROR: {CONFIG} define numeros distintos: {sorted(set(en_config))}")
        return 1

    numero = en_config[0]
    problemas = []
    enlaces = 0

    for nombre in PAGINAS:
        archivo = Path(nombre)
        if not archivo.exists():
            continue
        html = archivo.read_text(encoding="utf-8")
        enlaces += len(re.findall(r'<a\s[^>]*class="[^"]*\bwa-link\b', html))

        # Un numero literal en la pagina es exactamente lo que #64 vino a quitar.
        for encontrado in re.findall(r"WA_NUMBER\s*=\s*'(\d+)'", html):
            problemas.append(f"{nombre}: constante WA_NUMBER hardcodeada ('{encontrado}')")
        for encontrado in set(re.findall(r"wa\.me/(\d+)", html)):
            problemas.append(f"{nombre}: enlace wa.me/{encontrado} hardcodeado")

        # Si la pagina usa el numero, tiene que estar cargando el config.
        if "WA_NUMBER" in html and "config.js" not in html:
            problemas.append(f"{nombre}: usa WA_NUMBER pero no carga config.js")

    if problemas:
        print("[check_wa_number] ERROR: el numero debe vivir solo en config.js.")
        for p in problemas:
            print("  -", p)
        return 1

    print(f"[check_wa_number] OK: un solo numero ({numero}) en {CONFIG}, usado por {enlaces} enlaces wa-link.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
