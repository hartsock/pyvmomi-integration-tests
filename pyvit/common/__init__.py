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

import yaml

class ConnectionInfo(object):

    def __init__(self, data=None):
        if data is None:
            data = dict()
        self._data = dict(data)

    @property
    def host(self):
        return self._data.get('host', 'localhost')

    @property
    def port(self):
        return int(self._data.get('port', 443))

    @property
    def user(self):
        return self._data.get('user', 'root')

    @property
    def password(self):
        return self._data.get('pwd')


class YamlConnections(object):

    def __init__(self, file=None):
        if file is None:
            data = dict()
        else:
            data = yaml.safe_load(file)

        self._vcsim = ConnectionInfo(data.get('vcsim', dict()))
        self._vcenter = ConnectionInfo(data.get('vcenter', dict()))

    @property
    def vcsim(self):
        return self._vcsim

    @property
    def vcenter(self):
        return self._vcenter

    @staticmethod
    def load(file_name):
        with open(file_name, 'r') as file:
            connections = YamlConnections(file)
        return connections