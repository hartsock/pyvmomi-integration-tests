# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
from testfixtures import tempdir
import unittest

from pyvit import common

class TestConnectionLoader(unittest.TestCase):

    def setUp(self):
        self.fake_yaml_text = str('# YAML\n'
                                  'vcsim:\n'
                                  '    host: my.host\n'
                                  '    user: my.user\n'
                                  '    pwd: my.password\n'
                                  '    port: 1443\n'
                                  'vcenter:\n'
                                  '    host: my.other.host\n'
                                  '    user: my.other.user\n'
                                  '    pwd: my.other.password\n'
                                  '    port: 2443')

    def test_no_file(self):
        connections = common.YamlConnections(None)
        self.assertIsInstance(connections.vcsim, common.ConnectionInfo)
        self.assertIsInstance(connections.vcenter, common.ConnectionInfo)
        for con in [connections.vcsim, connections.vcenter]:
            self.assertEqual('localhost', con.host, 'wrong default host')
            self.assertEqual(443, con.port, 'wrong default port')
            self.assertEqual('root', con.user, 'wrong default user')
            self.assertIsNone(con.password, 'wrong default password')

    @tempdir()
    def test_fake_yaml_file(self, d):
        file_name = 'connections.yaml'
        d.write(file_name, bytearray(self.fake_yaml_text,
                                     sys.getdefaultencoding()))
        file_path = os.path.join(d.path, file_name)

        connections = common.YamlConnections.load(file_path)
        self.assertIsInstance(connections.vcsim, common.ConnectionInfo)
        self.assertIsInstance(connections.vcenter, common.ConnectionInfo)

        con = connections.vcsim
        self.assertEqual('my.host', con.host, 'wrong host')
        self.assertEqual(1443, con.port, 'wrong port')
        self.assertEqual('my.user', con.user, 'wrong user')
        self.assertEqual('my.password', con.password, 'wrong password')

        con = connections.vcenter
        self.assertEqual('my.other.host', con.host, 'wrong host')
        self.assertEqual(2443, con.port, 'wrong port')
        self.assertEqual('my.other.user', con.user, 'wrong user')
        self.assertEqual('my.other.password', con.password, 'wrong password')
