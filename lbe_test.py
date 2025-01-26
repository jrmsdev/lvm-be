#!/usr/bin/env python3

# Copyright Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__doc__ = 'Linux LVM Boot Environments Testing.'

import unittest

from unittest.mock import MagicMock, call

import lbe

class TestLBE(unittest.TestCase):

	stderr = None
	stdout = None

	__stderr = lbe.sys.stderr
	__stdout = lbe.sys.stdout

	def setUp(t):
		t.stderr = MagicMock()
		lbe.sys.stderr = t.stderr
		t.stdout = MagicMock()
		lbe.sys.stdout = t.stdout

	def tearDown(t):
		lbe.sys.stderr = t.__stderr
		t.stderr = None
		lbe.sys.stdout = t.__stdout
		t.stdout = None

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

#
# Config
#

class ConfigTest(TestLBE):
	def test_fake(t):
		pass

#
# LBE
#

class LBETest(TestLBE):
	def test_fake(t):
		pass

if __name__ == '__main__':
	unittest.main()
