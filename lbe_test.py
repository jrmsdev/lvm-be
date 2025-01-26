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

	stderr = None
	stdout = None

	__stderr = lbe.sys.stderr
	__stdout = lbe.sys.stdout

	def setUp(t):
		lbe.DEBUG = t.enable_debug
		t.stderr = MagicMock()
		lbe.sys.stderr = t.stderr
		t.stdout = MagicMock()
		lbe.sys.stdout = t.stdout

	def tearDown(t):
		lbe.sys.stderr = t.__stderr
		t.stderr = None
		lbe.sys.stdout = t.__stdout
		t.stdout = None
		lbe.DEBUG = False

#
# Logs
#

class LogsTest(TestLBE):

	def test_print(t):
		lbe._print('testing', '...')
		t.stdout.write.assert_has_calls([
			call('testing'),
			call(' '),
			call('...'),
			call('\n'),
		])
		t.stderr.write.assert_not_called()

	def test_msg(t):
		lbe.msg('testing ...')
		t.stdout.write.assert_has_calls([
			call('testing ...'),
			call('\n'),
		])
		t.stderr.write.assert_not_called()

	def test_dbg(t):
		lbe.dbg('testing ...')
		t.stderr.write.assert_not_called()
		t.stdout.write.assert_not_called()

class LogsDebugTest(TestLBE):

	enable_debug = True

	def test_dbg(t):
		lbe.dbg('testing ...')
		t.stderr.write.assert_has_calls([
			call('[D]'),
			call(' '),
			call('testing ...'),
			call('\n'),
		])
		t.stdout.write.assert_not_called()

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
		t.stderr.write.assert_has_calls([
			call('Config: debug was enabled from LBE_DEBUG env var'),
		])

	def test_argparse(t):
		cfg = lbe.Config()
		cfg.argparse(['--debug'])
		t.assertTrue(lbe.DEBUG)
		t.stderr.write.assert_has_calls([
			call('Config: debug was enabled from CLI args'),
		])

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
