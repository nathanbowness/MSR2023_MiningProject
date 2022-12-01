========================
MaxMind DB Python Module
========================

Description
-----------

This is a Python module for reading MaxMind DB files. The module includes both
a pure Python reader and an optional C extension.

MaxMind DB is a binary file format that stores data indexed by IP address
subnets (IPv4 or IPv6).

Installation
------------

If you want to use the C extension, you must first install `libmaxminddb
<https://github.com/maxmind/libmaxminddb>`_ C library installed before
installing this extension. If the library is not available, the module will
fall-back to a pure Python implementation. Note that when installing the C
library from a package, you may be required to install additonal packages
containing build requirements such as `libmaxminddb-dev` on Debian.

To install maxminddb, type:

.. code-block:: bash

    $ pip install maxminddb

If you are not able to use pip, you may also use easy_install from the
source directory:

.. code-block:: bash

    $ easy_install .

Usage
-----

To use this module, you must first download or create a MaxMind DB file. We
provide `free GeoLite2 databases
<https://dev.maxmind.com/geoip/geolocate-an-ip/databases?lang=en>`_. These
files must be decompressed with ``gunzip``.

After you have obtained a database and imported the module, call
``open_database`` with a path, or file descriptor (in the case of ``MODE_FD``),
to the database as the first argument. Optionally, you may pass a mode as the
second argument. The modes are exported from ``maxminddb``. Valid modes are:

* ``MODE_MMAP_EXT`` - use the C extension with memory map.
* ``MODE_MMAP`` - read from memory map. Pure Python.
* ``MODE_FILE`` - read database as standard file. Pure Python.
* ``MODE_MEMORY`` - load database into memory. Pure Python.
* ``MODE_FD`` - load database into memory from a file descriptor. Pure Python.
* ``MODE_AUTO`` - try ``MODE_MMAP_EXT``, ``MODE_MMAP``, ``MODE_FILE`` in that
  order. Default.

**NOTE**: When using ``MODE_FD``, it is the *caller's* responsibility to be
sure that the file descriptor gets closed properly. The caller may close the
file descriptor immediately after the ``Reader`` object is created.

The ``open_database`` function returns a ``Reader`` object. To look up an IP
address, use the ``get`` method on this object. The method will return the
corresponding values for the IP address from the database (e.g., a dictionary
for GeoIP2/GeoLite2 databases). If the database does not contain a record for
that IP address, the method will return ``None``.

If you wish to also retrieve the prefix length for the record, use the
``get_with_prefix_len`` method. This returns a tuple containing the record
followed by the network prefix length associated with the record.

Example
-------

.. code-block:: pycon

    >>> import maxminddb
    >>>
    >>> with maxminddb.open_database('GeoLite2-City.mmdb') as reader:
    >>>
    >>>     reader.get('152.216.7.110')
    {'country': ... }
    >>>
    >>>     reader.get_with_prefix_len('152.216.7.110')
    ({'country': ... }, 24)

Exceptions
----------

The module will return an ``InvalidDatabaseError`` if the database is corrupt
or otherwise invalid. A ``ValueError`` will be thrown if you look up an
invalid IP address or an IPv6 address in an IPv4 database.

Requirements
------------

This code requires Python 3.6+. Older versions are not supported. The C
extension requires CPython.

Versioning
----------

The MaxMind DB Python module uses `Semantic Versioning <https://semver.org/>`_.

Support
-------

Please report all issues with this code using the `GitHub issue tracker
<https://github.com/maxmind/MaxMind-DB-Reader-python/issues>`_

If you are having an issue with a MaxMind service that is not specific to this
API, please contact `MaxMind support <https://www.maxmind.com/en/support>`_ for
assistance.
