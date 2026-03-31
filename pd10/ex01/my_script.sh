#!/bin/sh

DIR="local_lib"
LOGS_FILE="pip.log"
GITHUB_REPO="git+https://github.com/jaraco/path"
GITHUB_REF="refs/archive/maint/path.py-legacy"

echo -n "Versión de pip: "
pip --version

echo "Creando la carpeta \"$DIR\"..."
if [ -d "$DIR" ]; then
    rm -rf "$DIR"
fi
mkdir "$DIR"

echo "Instalando path.py desde GitHub..."
python3 -m pip install -q -t "$DIR" --log "$LOGS_FILE" --force-reinstall "$GITHUB_REPO@$GITHUB_REF"

result=$?
if [ "$result" -ne 0 ]; then
    echo "Error al instalar el paquete path"
else
    echo "Instalación completada en $DIR"
    python3 my_program.py
fi
