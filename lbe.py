#!/usr/bin/env python3

# Copyright Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__doc__ = 'Linux LVM Boot Environments.'

import os
import sys

from argparse     import ArgumentParser
from configparser import ConfigParser
from pathlib      import Path

DEBUG: bool = os.getenv('LBE_DEBUG', 'false') == 'true'

def dbg(msg):
	"""Debug logs."""
	if DEBUG:
		print('[D]', msg, file = sys.stderr)

CONFIG_FILE = '~/.config/lvm-be.cfg'

class Config(object):
	"""LBE configuration."""

	file:  Path = Path(CONFIG_FILE)

	def __init__(self):
		if DEBUG:
			dbg('Config: debug was enabled from LBE_DEBUG env var')
		dbg(f"Config: file={self.file}")

	def _getpath(self, name: str) -> Path:
		return Path(name).expanduser()

	def argparse(self, argv: list[str]):
		"""Config parse from CLI args."""
		global DEBUG
		dbg(f"Config: argparse {argv}")

		parser = ArgumentParser(description = __doc__)

		parser.add_argument('--debug', '-d', action = 'store_true',
			help = 'enable debug logs', default = False)
		parser.add_argument('--config', '-f', type = str, required = False,
			help = 'config filename', default = CONFIG_FILE)

		args = parser.parse_args(args = argv)

		dbg(f"Config: args.debug={args.debug}")
		if args.debug is True:
			DEBUG = True
			dbg('Config: debug was enabled from CLI args')
		dbg(f"Config: args.config={args.config}")
		self.file = self._getpath(args.config.strip())

	def read(self) -> bool:
		"""Read config filename."""
		global DEBUG
		dbg(f"Config: read file={self.file}")
		if not self.file.exists():
			dbg(f"Config: {self.file} not found!")
			return False
		cfg = ConfigParser(defaults = {
			'debug': 'false',
		})
		loaded = cfg.read([self.file.as_posix()])
		dbg(f"Config: loaded files {loaded}")
		if cfg.getboolean('lbe', 'debug'):
			DEBUG = True
			self.debug = True
			dbg('Config: debug was enable from config file')
		return False

class LBE(object):
	"""Linux LVM Boot Environments."""

	cfg: Config = Config()

	def main(self, argv: list[str] = []) -> int:
		"""LBE: CLI main."""
		dbg('LBE: main')
		self.cfg.argparse(argv)
		self.cfg.read()
		return 0

if __name__ == '__main__':
	dbg('main')
	lbe = LBE()
	sys.exit(lbe.main(sys.argv[1:]))
