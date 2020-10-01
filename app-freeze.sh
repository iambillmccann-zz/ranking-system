#!/bin/bash
# Issue a Pip freeze command to update requirements.txt

python3 --version
pip --version
pip freeze > requirements.txt
