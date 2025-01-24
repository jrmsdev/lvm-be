#!/usr/bin/env python3

# Copyright Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__doc__ = 'Linux LVM Boot Environments.'

import os
import sys

from argparse import ArgumentParser

DEBUG = os.getenv('LBE_DEBUG', None) is not None

def dbg(msg):
	"""Debug logs."""
	if DEBUG:
		print('[D]', msg, file = sys.stderr)

class LBE(object):
	"""Linux LVM Boot Environments."""
	pass

def main(argv: list = []) -> int:
	"""CLI main."""
	dbg('testing')
	return 9

if __name__ == '__main__':
	sys.exit(main())
