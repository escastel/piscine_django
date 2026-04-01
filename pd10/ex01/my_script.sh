#!/bin/sh

DIR="local_lib"
LOGS_FILE="pip.log"
GITHUB_REPO="git+https://github.com/jaraco/path"
GITHUB_REF="refs/archive/maint/path.py-legacy"

echo -n "Pip version: "
pip --version

echo "Creating folder \"$DIR\"..."
if [ -d "$DIR" ]; then
    rm -rf "$DIR"
fi
mkdir "$DIR"

echo "Installing path.py from GitHub..."
python3 -m pip install -q -t "$DIR" --log "$LOGS_FILE" --force-reinstall "$GITHUB_REPO@$GITHUB_REF"

result=$?
if [ "$result" -ne 0 ]; then
    echo "Error installing path package"
else
    echo "Installation completed in $DIR"
    python3 my_program.py
fi
