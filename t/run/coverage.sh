#!/bin/sh
set -eu

export PYTHONPATH="${PWD}"

OMIT="/usr/lib/python3/*"

rm -f .coverage

covd="${PWD}/tmp/htmlcov"
rm -rf "${covd}"

install -v -d -m 0750 "${PWD}/tmp"

set -x

python3-coverage run --omit "${OMIT}" ./lbe_test.py "$@"

python3-coverage report --omit "${OMIT}"
python3-coverage html --omit "${OMIT}" -d "${covd}"

exit 0
