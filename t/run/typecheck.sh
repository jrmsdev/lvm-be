#!/bin/sh
set -xeu
export PYTHONPATH="${PWD}"
exec python3 -m mypy "${PWD}"
