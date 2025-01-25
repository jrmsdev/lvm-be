#!/bin/sh
export LBE_DEBUG='true'
exec ./lbe.py --config ./t/devel/lbedev.cfg "$@"
