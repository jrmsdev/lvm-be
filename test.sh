#!/bin/sh
set -xeu
shellcheck ./test.sh
shellcheck ./t/run/typecheck.sh
./t/run/typecheck.sh
exit 0
