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

import atexit
import time

from pyVim import connect
from pyVmomi import vim

from pyvit.tests.vcsim import BaseTestCase

class TestExceptionMarshalling(BaseTestCase):

    def impossible(self, vm):
        if vm.runtime.powerState != vim.VirtualMachinePowerState.poweredOn:
            task = vm.PowerOn()
            while task.info.state not in [vim.TaskInfo.State.running,
                                          vim.TaskInfo.State.error]:
                time.sleep(1)
        lease = vm.ExportVm()
        raise lease.error

    def test_impossible_action(self):
        si = self.session_instance
        root = si.content.rootFolder
        view = si.content.viewManager.CreateContainerView(root,
                                                          [vim.VirtualMachine],
                                                          True)
        vms = view.view
        view.Destroy()

        vm = vms.pop()
        self.assertRaises(vim.fault.InvalidPowerState, self.impossible, vm)
