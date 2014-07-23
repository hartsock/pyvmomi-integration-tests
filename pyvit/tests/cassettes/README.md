VCRpy Cassette Directory
========================

The [vcrpy](https://github.com/kevin1024/vcrpy) library is used with this
tool chain. It creates recordings of HTTP events called 'fixtures' in YAML
format. This tool kit is intended as an integration testing kit and the
cassettes are intended as a diagnostic and recording tool.


Use for bug reports
-------------------
If you have an interesting failure or event you can save the YAML recording
and submit the cassette file with a bug report.


Use for feature development
---------------------------
If you invent a new feature that interacts with the API the recording may be
useful in porting the feature up the library tool-chain into pyVmomi itself.


Notes
-----

* You may want to clean out your usernames, passwords and IP addresses from
  cassette files before you submit them.

* You can tamper with cassette files to produce situations that you can't
  nominally produce with working equipment. This is a valuable use case
  when working with HTTP client code.
