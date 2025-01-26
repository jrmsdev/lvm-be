#!/bin/sh
set -xeu
export PYTHONPATH="${PWD}"
python3 -m mypy ./lbe.py ./lbe_test.py
exit 0
