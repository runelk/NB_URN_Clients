#!/usr/bin/env python

import unittest
import json
import os

class CliTestHelper(object):
    def __init__(self, config):
        self.config = json.loads(open(config).read())
        self.main_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

class TestBinCommands(unittest.TestCase):
    def setUp(self):
        self.cli_test_helper = CliTestHelper('test_config.json')
        
    def test_config(self):
        print self.cli_test_helper.config;
        

    def test_commands(self):
        pass
