#!/bin/sh
# Regenera CapturaDocs-Express-Guia-Paso-a-Paso.pdf con la app tal como está en
# origin/main de informes-ponal. Correr con Git Bash, desde cualquier carpeta:
#
#   sh guia-pdf/regenerar.sh
#
# Qué hace (todo en una carpeta temporal; NO toca el directorio de trabajo de
# informes-ponal ni sus cambios sin commitear, que suelen ser de otra sesión):
#   1. extrae origin/main de informes-ponal (git archive)
#   2. construye la app y la abre con la red SIMULADA (nada llega al Worker real)
#   3. recorre el primer ingreso y un caso con datos INVENTADOS, capturando cada pantalla
#   4. recorta las capturas, arma la maqueta y exporta el PDF
# Las 3 imágenes que no salen de la app (Explorador, Word, impresión al 60 %) se
# toman a mano y se ponen en generador/img-usuario/ como explorador.png,
# word-pdf.png e imprimir-escala.png; si faltan, la guía sale sin ellas.
set -e

AQUI="$(cd "$(dirname "$0")" && pwd)"
APP="$AQUI/../../informes-ponal"
[ -d "$APP/.git" ] || { echo "No encuentro informes-ponal junto a capturadocs-landing: $APP"; exit 1; }

TRABAJO="$(mktemp -d)"
JUNCTION="$TRABAJO/app/node_modules"
limpiar() {
  # El node_modules de la copia es un enlace al REAL: se desengancha primero,
  # porque borrar la carpeta con el enlace puesto podría llevarse el original.
  [ -e "$JUNCTION" ] && cmd //c rmdir "$(cygpath -w "$JUNCTION")" >/dev/null 2>&1
  rm -rf "$TRABAJO"
}
trap limpiar EXIT

echo "1/4  extrayendo origin/main de informes-ponal..."
git -C "$APP" fetch -q origin
git -C "$APP" archive --format=tar -o "$TRABAJO/main.tar" origin/main
mkdir "$TRABAJO/app"
tar -xf "$TRABAJO/main.tar" -C "$TRABAJO/app"
cmd //c mklink //J "$(cygpath -w "$JUNCTION")" "$(cygpath -w "$APP/node_modules")" >/dev/null
VERSION="$(grep -m1 '"version"' "$TRABAJO/app/package.json" | sed 's/[^0-9.]//g')"
echo "     app versión $VERSION"

cp -r "$AQUI/generador/e2e-guia" "$TRABAJO/app/e2e-guia"
cp "$AQUI/generador/playwright.guia.config.js" "$TRABAJO/app/"

echo "2/4  construyendo y capturando pantallas (1-2 min)..."
mkdir "$TRABAJO/capturas"
( cd "$TRABAJO/app" && GUIA_OUT="$(cygpath -m "$TRABAJO/capturas")" npx playwright test -c playwright.guia.config.js capturas 2>&1 | grep -E 'passed|failed|Error' )

echo "3/4  recortando capturas y armando la maqueta..."
mkdir -p "$TRABAJO/pdf/img"
python -X utf8 "$TRABAJO/app/e2e-guia/preparar-imagenes.py" "$(cygpath -m "$TRABAJO/capturas")" "$(cygpath -m "$TRABAJO/pdf/img")" | tail -1
cp "$AQUI/../logo.png" "$TRABAJO/pdf/img/logo.png"
cp "$AQUI/generador/guia-print.tpl.html" "$TRABAJO/pdf/"
mkdir "$TRABAJO/pdf/img-usuario"
for f in "$AQUI"/generador/img-usuario/*.png "$AQUI"/generador/img-usuario/*.jpg; do
  [ -f "$f" ] && cp "$f" "$TRABAJO/pdf/img-usuario/"
done

echo "4/4  exportando el PDF..."
( cd "$TRABAJO/app" && node e2e-guia/hacer-pdf.mjs "$(cygpath -m "$TRABAJO/pdf")" "$(cygpath -m "$TRABAJO/pdf/guia.pdf")" )
cp "$TRABAJO/pdf/guia.pdf" "$AQUI/CapturaDocs-Express-Guia-Paso-a-Paso.pdf"
echo "Listo: $AQUI/CapturaDocs-Express-Guia-Paso-a-Paso.pdf  (app $VERSION)"
