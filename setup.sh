#!/bin/sh
# Deja el clon listo para trabajar. Correr una sola vez despues de clonar:
#
#   ./setup.sh
#
# Git no ejecuta nada automaticamente al clonar (a proposito, por seguridad),
# asi que los hooks del repo no se activan solos. Sin esto, el pre-commit que
# cuida el numero de WhatsApp no corre y un numero inconsistente puede llegar
# a produccion sin que nadie se entere.
set -e

git config core.hooksPath .githooks
echo "✓ hooks activados (core.hooksPath -> .githooks)"

# Verificacion real: que el hook efectivamente corra y pase.
if python check_wa_number.py; then
  echo "✓ el chequeo del numero de WhatsApp corre bien"
else
  echo "✗ el chequeo fallo — revisalo antes de comitear"
  exit 1
fi
