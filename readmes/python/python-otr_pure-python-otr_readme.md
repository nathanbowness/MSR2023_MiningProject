[![Build Status](https://travis-ci.org/python-otr/pure-python-otr.svg?branch=master)](https://travis-ci.org/python-otr/pure-python-otr)

Python OTR
==========
This is a pure Python OTR implementation; it does not bind to libotr.

Install the potr Python module:

    sudo python setup.py install

__Dependencies__: pycrypto >= 2.1 (see [dlitz/pycrypto](https://github.com/dlitz/pycrypto))

This software is experimental and potentially insecure. Do not rely on it
=========================================================================

Usage Notes
===========
This module uses pycrypto's RNG. If you use this package in your application and your application
uses `os.fork()`, make sure to call `Crypto.Random.atfork()` in both the parent and the child process.

Reporting bugs
==============
Please read the [FAQ](https://github.com/python-otr/pure-python-otr/wiki) before submitting your
issue to the [tracker](https://github.com/python-otr/pure-python-otr/issues).
Pull requests should be addressed to the staging branch, NOT the master branch.
