#!/usr/bin/env python
"""Verifica que el numero de WhatsApp en index.html sea consistente.
Desde #19 (2026-08-11) el numero vive en una sola constante JS (WA_NUMBER)
y los enlaces <a class="wa-link"> se completan en runtime -- ya no hay
'wa.me/<numero>' hardcodeado en el HTML. Este script revisa que exista
esa constante, que los enlaces wa-link no tengan un numero propio distinto,
y que no haya vuelto a colarse un wa.me/<numero> hardcodeado en otro lado.
No modifica nada del sitio en produccion -- corre solo en dev, antes de
comitear (ver .githooks/pre-commit)."""
import re
import sys

FILE = "index.html"

def main():
    with open(FILE, encoding="utf-8") as f:
        html = f.read()

    const_matches = re.findall(r"WA_NUMBER\s*=\s*'(\d+)'", html)
    hardcoded = set(re.findall(r"wa\.me/(\d+)", html))
    wa_links = len(re.findall(r'<a\s[^>]*class="[^"]*\bwa-link\b', html))

    if not const_matches:
        print(f"[check_wa_number] No se encontro la constante WA_NUMBER en {FILE} -- revisa manualmente.")
        return 1

    if len(set(const_matches)) > 1:
        print(f"[check_wa_number] ERROR: hay mas de una definicion de WA_NUMBER con valores distintos: {sorted(set(const_matches))}")
        return 1

    numbers = set(const_matches) | hardcoded
    if len(numbers) > 1:
        print(f"[check_wa_number] ERROR: {FILE} tiene numeros de WhatsApp distintos: {sorted(numbers)}")
        print("Revisa WA_NUMBER y cualquier 'wa.me/<numero>' hardcodeado y deja todos iguales antes de comitear.")
        return 1

    print(f"[check_wa_number] OK: un solo numero de WhatsApp ({const_matches[0]}) en WA_NUMBER, usado por {wa_links} enlaces wa-link.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
