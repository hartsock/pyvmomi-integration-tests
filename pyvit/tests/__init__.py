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

from pyvit import common
import os


def tests_resource_path(local_path=''):
    this_file = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(this_file, local_path)


CONFIG_FILE_NAME = os.path.join(os.path.dirname(__file__),
                                '../../connections.yaml')


def load_connections():
    with open(CONFIG_FILE_NAME, 'r') as f:
        return common.YamlConnections(f)


# Fully qualified path to the fixtures directory underneath this module
fixtures_path = tests_resource_path('cassettes')
record_mode = 'all'