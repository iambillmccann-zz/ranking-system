#!/bin/bash
# Issue a Pip freeze command to install packages from requirements.txt

python3 --version
pip --version
pip install  --target ./venv/lib --requirement requirements.txt
