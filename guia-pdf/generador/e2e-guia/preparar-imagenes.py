"""Recorta cada captura a su zona útil y la comprime a JPEG para el PDF.

Por qué recortar: una captura de pantalla completa (1440 px de ancho) metida en una
hoja A4 deja el texto de la app en ~5 pt, ilegible impreso. Recortada a la tarjeta
central queda en ~8 pt. Uso: python preparar-imagenes.py <carpeta-capturas> <carpeta-img>
"""
import sys, os, glob
from PIL import Image, ImageChops

src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst, exist_ok=True)

# Zona de la tarjeta central de los pasos del formulario (imagen original 2160x1350).
CAJA_PASO = (430, 350, 1730, 1350)
COMPLETA = {'04-pantalla-principal'}          # necesita la barra superior y el menú
TARJETAS = {'01-terminos', '01b-terminos-marcado', '02-registro-correo', '03-configuracion-inicial'}

def recorte_modal(im, margen=26):
    """Caja del modal: es lo único con borde DORADO sobre el fondo atenuado."""
    dorado = im.point(lambda v: v).convert('RGB')
    px = dorado.load()
    xs, ys = [], []
    for y in range(0, im.height, 2):
        for x in range(0, im.width, 2):
            r, g, b = px[x, y]
            if r > 190 and 120 < g < 190 and b < 70:
                xs.append(x); ys.append(y)
    return im.crop((max(0, min(xs) - margen), max(0, min(ys) - margen), min(im.width, max(xs) + margen), min(im.height, max(ys) + margen)))

def autorecorte(im, margen=30, umbral=18):
    """Recorta el fondo liso alrededor de una tarjeta centrada."""
    fondo = Image.new('RGB', im.size, im.getpixel((5, 5)))
    caja = ImageChops.difference(im, fondo).convert('L').point(lambda v: 255 if v > umbral else 0).getbbox()
    if not caja:
        return im
    l, t, r, b = caja
    return im.crop((max(0, l - margen), max(0, t - margen), min(im.width, r + margen), min(im.height, b + margen)))

total = 0
for f in sorted(glob.glob(os.path.join(src, '[0-9]*.png'))):
    nombre = os.path.splitext(os.path.basename(f))[0]
    im = Image.open(f).convert('RGB')
    if nombre in COMPLETA:
        pass
    elif nombre in TARJETAS:
        im = autorecorte(im)
    elif nombre.startswith('12-'):
        im = recorte_modal(im)
    else:
        im = im.crop(CAJA_PASO)
    ancho = min(1700, im.width)
    im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    salida = os.path.join(dst, nombre + '.jpg')
    im.save(salida, quality=86, optimize=True)
    total += os.path.getsize(salida)
    print(f'{nombre}: {im.size[0]}x{im.size[1]}  {round(os.path.getsize(salida) / 1024)} KB')
print('total', round(total / 1024 / 1024, 2), 'MB')
