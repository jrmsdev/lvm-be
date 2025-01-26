#!/bin/sh
set -xeu

shellcheck ./*.sh
shellcheck ./t/run/*.sh

./t/run/typecheck.sh

exit 0
