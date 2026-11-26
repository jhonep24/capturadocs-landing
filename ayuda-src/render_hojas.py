"""Convierte las hojas del PDF oficial en blanco en imágenes para el carrusel de la guía.
Uso: python render_hojas.py fpj6   → ../img/carrusel-fpj6-h1.jpg, -h2.jpg (ancho 1500 px, formato sin modificar)."""
import io
import os
import sys

import fitz
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
ANCHO = 1500


def render(fmt):
    pdf = os.path.join(RAIZ, 'ayuda', 'pdf', f'formato-{fmt}-en-blanco.pdf')
    doc = fitz.open(pdf)
    for i, hoja in enumerate(doc, 1):
        zoom = ANCHO / hoja.rect.width
        pix = hoja.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
        img = Image.open(io.BytesIO(pix.tobytes('png'))).convert('RGB')
        out = os.path.join(RAIZ, 'img', f'carrusel-{fmt}-h{i}.jpg')
        img.save(out, 'JPEG', quality=70, optimize=True, progressive=True)
        print(out, img.size, os.path.getsize(out) // 1024, 'KB')


if __name__ == '__main__':
    render(sys.argv[1] if len(sys.argv) > 1 else 'fpj6')
