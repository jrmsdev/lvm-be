#!/usr/bin/env python3

# Copyright Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__doc__ = 'Linux LVM Boot Environments Testing.'

import unittest

from unittest.mock import MagicMock, call

import lbe

from pathlib import Path

class TestLBE(unittest.TestCase):

	enable_debug = False

	config_filename = ''

	msgout = None
	dbgout = None

	__msgout = lbe._msgout
	__dbgout = lbe._dbgout

	def setUp(t):
		lbe.DEBUG = t.enable_debug
		if t.config_filename != '':
			lbe.CONFIG_FILE = t.config_filename.strip()
			lbe.Config.file = Path(lbe.CONFIG_FILE)
		t.msgout = MagicMock()
		lbe._msgout = t.msgout
		t.dbgout = MagicMock()
		lbe._dbgout = t.dbgout

	def tearDown(t):
		lbe._msgout = t.__msgout
		t.msgout = None
		lbe._dbgout = t.__dbgout
		t.dbgout = None
		if t.config_filename != '':
			lbe.CONFIG_FILE = '~/.config/lvm-be.cfg'
			lbe.Config.file = Path(lbe.CONFIG_FILE)
		lbe.DEBUG = False

#
# Logs
#

class LogsTest(TestLBE):

	def test_print(t):
		fh = MagicMock()
		lbe._print('testing', '...', file = fh)
		fh.write.assert_has_calls([
			call('testing'),
			call(' '),
			call('...'),
			call('\n'),
		])

	def test_msg(t):
		lbe.msg('testing ...')
		t.msgout.write.assert_has_calls([
			call('testing ...'),
			call('\n'),
		])

	def test_dbg(t):
		lbe.dbg('testing ...')
		t.dbgout.write.assert_not_called()

class LogsDebugTest(TestLBE):

	enable_debug = True

	def test_dbg(t):
		lbe.dbg('testing ...')
		t.dbgout.write.assert_has_calls([
			call('[D]'),
			call(' '),
			call('testing ...'),
			call('\n'),
		])

#
# Config
#

class ConfigTest(TestLBE):

	def test_init(t):
		t.assertEqual(lbe.CONFIG_FILE, '~/.config/lvm-be.cfg')

	def test__getpath(t):
		cfg = lbe.Config()
		p = Path('~/.config/lvm-be.cfg')
		t.assertEqual(p.expanduser(), cfg._getpath(lbe.CONFIG_FILE))

	def test_argparse(t):
		cfg = lbe.Config()
		cfg.argparse([])
		t.assertFalse(lbe.DEBUG)
		t.assertEqual(cfg._getpath(lbe.CONFIG_FILE), cfg.file)

class ConfigDebugTest(TestLBE):

	enable_debug = True

	def test_init(t):
		cfg = lbe.Config()
		t.dbgout.write.assert_has_calls([
			call('Config: debug was enabled from LBE_DEBUG env var'),
		])

	def test_argparse(t):
		cfg = lbe.Config()
		cfg.argparse(['--debug'])
		t.assertTrue(lbe.DEBUG)
		t.dbgout.write.assert_has_calls([
			call('Config: debug was enabled from CLI args'),
		])

class ConfigFileTest(TestLBE):

	config_filename = './t/devel/lbedev.cfg'

	def test_read(t):
		print(lbe.CONFIG_FILE)
		cfg = lbe.Config()
		print(cfg.file)
		t.assertTrue(cfg.read())

#
# LBE
#

class LBETest(TestLBE):

	def test_init(t):
		t.assertFalse(lbe.DEBUG)

class LBEDebugTest(TestLBE):

	enable_debug = True

	def test_init(t):
		t.assertTrue(lbe.DEBUG)

if __name__ == '__main__':
	unittest.main()
