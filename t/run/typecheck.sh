#!/bin/sh
set -xeu
export PYTHONPATH="${PWD}"
python3 -m mypy ./lbe.py
exit 0
