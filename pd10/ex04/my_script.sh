#!/bin/bash

VENV_NAME="django_venv"

if [ -d "$VENV_NAME" ]; then
    echo "Removing existing virtualenv..."
    rm -rf "$VENV_NAME"
fi

echo "Creating Python 3 virtualenv named $VENV_NAME..."
python3 -m venv "$VENV_NAME"

echo "Activating virtualenv..."
source "$VENV_NAME/bin/activate"

echo "Installing requirements..."
pip install -r requirement.txt

echo "Virtualenv $VENV_NAME is now active and ready to use."
