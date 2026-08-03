#!/usr/bin/env python
"""Verifica que todos los enlaces a WhatsApp en index.html usen el mismo
numero. No modifica nada del sitio en produccion -- corre solo en dev,
antes de comitear (ver .githooks/pre-commit)."""
import re
import sys

FILE = "index.html"

def main():
    with open(FILE, encoding="utf-8") as f:
        html = f.read()

    numbers = set(re.findall(r"wa\.me/(\d+)", html))

    if not numbers:
        print(f"[check_wa_number] No se encontro ningun enlace wa.me en {FILE} -- revisa manualmente.")
        return 1

    if len(numbers) > 1:
        print(f"[check_wa_number] ERROR: {FILE} tiene numeros de WhatsApp distintos: {sorted(numbers)}")
        print("Revisa cada 'wa.me/<numero>' y deja todos iguales antes de comitear.")
        return 1

    print(f"[check_wa_number] OK: un solo numero de WhatsApp ({numbers.pop()}) en {len(re.findall(r'wa.me/', html))} enlaces.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
