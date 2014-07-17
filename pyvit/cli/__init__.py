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

import unittest
from pyvit import tests

def run_tests_for(module_name_list):
    print(module_name_list)
    suite = unittest.TestSuite()

    for module_name in module_name_list:
        print(module_name)
        try:
            # if the module defines a suite() function call it to run the suite
            module = __import__(module_name, globals(), locals(), ['suite'])
            suite_function = getattr(module, 'suite')
            suite.addTest(suite_function)
        except (ImportError, AttributeError):
            print("load everything")
            # otherwise we'll just load *everything* we can find
            tests = unittest.defaultTestLoader.loadTestsFromModule(tests.vcsim)
            print(tests)
            suite.addTest(
                unittest.defaultTestLoader.loadTestsFromName(module_name))

    unittest.TextTestRunner().run(suite)