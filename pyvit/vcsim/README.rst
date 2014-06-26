pyvit.vcsim tests
=================

pyVmomi tests that can test against a vCenter Server Simulator (vcsim) instance

What
----

These are tests that can happen against a vCenter Server Simulator instance
instead of requiring a full service vCenter to test with. The majority of
integration tests will hopefully occur in this package.

Why
----

vCenter Server Simulator (vcsim) is not a fully functional vCenter so it
cannot complete certain tasks. We try to avoid using tests we know that vcsim
can't complete or meaningfully tell us about. Stress testing with vcsim
for example only tells us about limitations in the pyVmomi library code
itself.