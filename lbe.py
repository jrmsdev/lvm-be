#!/usr/bin/env python3

# Copyright Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__doc__ = 'Linux LVM Boot Environments.'

import os
import sys

from argparse     import ArgumentParser
from configparser import ConfigParser
from pathlib      import Path

DEBUG: bool = os.getenv('LBE_DEBUG', None) is not None

def dbg(msg):
	"""Debug logs."""
	if DEBUG:
		print('[D]', msg, file = sys.stderr)

class Config(object):
	"""LBE configuration."""

	debug: bool = DEBUG
	file:  Path = None

	def __init__(self, argv: list = []):
		dbg(f"Config: init argv={argv}")
		if len(argv) > 0:
			self.argparse(argv)
		dbg(f"Config: debug={self.debug}")
		dbg(f"Config: file={self.file}")
		if not self.file.exists():
			dbg(f"Config: {self.file} not found!")

	def _getpath(self, name: str) -> Path:
		return Path(name).expanduser()

	def argparse(self, args: list):
		"""Config parse from CLI args."""
		dbg(f"Config argparse: {args}")

		parser = ArgumentParser(description = __doc__)

		parser.add_argument('--debug', '-d', action = 'store_true',
			help = 'enable debug logs')
		parser.add_argument('--config', '-f', type = str, required = False,
			help = 'config filename', default = '~/.config/lvm-be.cfg')

		args = parser.parse_args(args = args)

		dbg(f"Config: args.debug={args.debug}")
		self.debug = args.debug is True
		dbg(f"Config: args.config={args.config}")
		self.file = self._getpath(args.config.strip())

	def read(self) -> bool:
		"""Read config filename."""
		dbg(f"Config: read file={self.file}")
		parser = ConfigParser(defaults = {
			'lbe.debug': False,
		})
		loaded = parser.read([self.file.as_posix()])
		dbg(f"Config: loaded files {loaded}")
		return False

class LBE(object):
	"""Linux LVM Boot Environments."""

	cfg: Config = None

	def __init__(self, cfg: Config):
		self.cfg = cfg

def main(argv: list = []) -> int:
	"""CLI main."""
	dbg('main: start')
	lbe = LBE(Config(argv = argv))
	lbe.cfg.read()
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
