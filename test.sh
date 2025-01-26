#!/bin/sh
set -xeu

shellcheck ./*.sh
shellcheck ./t/run/*.sh

./t/run/typecheck.sh
./t/run/coverage.sh

exit 0
