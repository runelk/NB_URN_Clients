#!/usr/bin/env python

import unittest
import json
import os
import subprocess

class CliTestHelper(object):
    def __init__(self, config):
        self.config = json.loads(open(config).read())
        # self.main_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
        self.main_directory = '/Users/rkn083/mystuff/projects/clarino/urn'
    
    def call_cmd(self, client, cmd):
        p = subprocess.Popen(
            os.path.join(self.main_directory, 
                         self.config['clients'][client]['directory'], 'bin', cmd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return p.communicate()
        

class TestBinCommands(unittest.TestCase):
    def setUp(self):
        self.helper = CliTestHelper('test_config.json')
        
    def test_config(self):
        # print self.helper.config;
        # print self.helper.config['clients']['python']['directory']
        pass

    def test_client_directory(self):
        for client, info in self.helper.config['clients'].items():
            client_dir = os.path.join(self.helper.main_directory, info['directory'])
            self.assertTrue(os.path.isdir(client_dir))
            self.assertTrue(os.path.isdir(os.path.join(client_dir, 'bin')), 
                            "%s exists?" % os.path.join(client_dir, 'bin'))

    def test_commands_exist(self):
        commands = [cmd for cmd in self.helper.config['commands']]

        for client, info in self.helper.config['clients'].items():
            bindir = os.path.join(self.helper.main_directory, info['directory'], 'bin')
            for cmd in commands:
                self.assertTrue(os.path.exists(os.path.join(bindir, cmd)),
                                "%s exists?" % os.path.join(bindir, cmd))

    def test_command_error_msgs(self):
        for client in self.helper.config['clients']:
            for cmd, info in self.helper.config['commands'].items():
                result = self.helper.call_cmd(client, cmd)
                expected_errmsg = info['usage_error_msg'].strip()
                actual_errmsg = result[1].strip()
                self.assertEqual(
                    actual_errmsg, expected_errmsg,
                    "(in %s: %s) Expected '%s', was '%s'" % (client, cmd, expected_errmsg, actual_errmsg)
                )


        # print self.helper.call_cmd('/Users/rkn083/mystuff/projects/clarino/urn/NB_URN_Client_Python/bin/find_urn')
        # # for client, info in self.helper.config['clients'].items():
        # #     for 
                
            
