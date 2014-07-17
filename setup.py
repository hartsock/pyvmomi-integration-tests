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

from setuptools import setup, find_packages

setup(
    name="pyvmomi-integration-tests",
    version="0.0.0alpha",
    description="pyVmomi Integration Test Suite",
    author="VMware",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=['pyvit'],
    test_suite='pyvit.tests',
    include_package_data=True,
    install_requires=['pyvmomi', 'testtools>=0.9.34', 'fixtures>=0.3.14',
                      'testfixtures', 'testscenarios>=0.4',
                      'PyYAML>=3.11'],
    tests_require=['coverage'],
    entry_points = {
        'run_vcsim_tests': [
            'run_tests = pyvit.cli.run_vcsim_tests.py:run_tests'
        ],
        'run_vcenter_tests': [
            'run_tests = pyvit.cli.run_vcenter_tests.py:run_tests'
        ]
    }
)