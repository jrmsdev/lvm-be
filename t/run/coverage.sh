#!/bin/sh
set -eu

export PYTHONPATH="${PWD}"

rm -f .coverage

python3-coverage run ./lbe_test.py "$@"

covd="${PWD}/tmp/htmlcov"
rm -rf "${covd}"

python3-coverage report
python3-coverage html -d "${covd}"

exit 0
