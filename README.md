pyvmomi-integration-tests
=========================

pyVmomi Integration Testing Project for validating the pyVmomi library


Test libraries used
-------------------

 * https://pythonhosted.org/testfixtures/
 * https://pypi.python.org/pypi/testscenarios/
 * https://testtools.readthedocs.org/en/latest/


vCenter Server Simulator notes
------------------------------
 * http://www.virtuallyghetto.com/2012/12/vcenter-server-simulator.html
 * http://www.virtuallyghetto.com/2014/04/simulating-vsphere-performance-metrics-using-vcsim.html

connections.yaml
----------------

Connection information for the tests is stored in a local yaml file that we
do *not* check into the repository. The file name is connections.yaml and
the format is:
```
 # YAML
 vcsim:
   host: my.host
   user: my.user
   pwd: my.password
   port: 443
 vcenter:
   host: my.other.host
   user: my.other.user
   pwd: my.other.password
   port: 443
```
