#!/usr/bin/env python3

# Copyright Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__doc__ = 'Linux LVM Boot Environments.'

import os
import sys

from argparse import ArgumentParser

DEBUG: bool = os.getenv('LBE_DEBUG', None) is not None

def dbg(msg):
	"""Debug logs."""
	if DEBUG:
		print('[D]', msg, file = sys.stderr)

class Config(object):
	"""LBE configuration."""

	debug: bool = DEBUG

	def __init__(self, argv: list = []):
		dbg(f"Config: init argv={argv}")
		if len(argv) > 0:
			self.argparse(argv)
		dbg(f"Config: debug={self.debug}")

	def argparse(self, args: list):
		"""Config parse from CLI args."""
		dbg(f"Config argparse: {args}")
		parser = ArgumentParser(description = __doc__)
		parser.add_argument('--debug', '-d', action = 'store_true',
			help = 'enable debug logs')
		args = parser.parse_args(args = args)
		dbg(f"Config: args.debug={args.debug}")
		self.debug = args.debug is True

class LBE(object):
	"""Linux LVM Boot Environments."""

	cfg: Config = None

	def __init__(self, cfg: Config):
		self.cfg = cfg

	def main(self) -> int:
		"""CLI main."""
		dbg('LBE: main')
		return 0

def main(argv: list = []) -> int:
	"""CLI main."""
	dbg('main: start')
	lbe = LBE(Config(argv = argv))
	return lbe.main()

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
