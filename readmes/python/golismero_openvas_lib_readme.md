What's this lib?
================

This project is a Python library to connect and manage the OpenVAS servers using the OMP protocol. OpenVAS 6, 7, 8 and 9 are supported (7 and 8 versions are still experimental)

Also, you can parse and interpret OpenVas XML reports.

Why this lib?
=============

There is an [official python library](https://pypi.python.org/pypi/openvas.omplib) for OpenVAS, but it doesn't work with OMPv4 based versions (OpenVAS 6).

Also, the official library has many unfixed bugs, and it's not capable to read and interpret the XML reports.

License
=======

This library is released under BSD Clause 3 license

Python versions
===============

Currently, this library only runs under Python 2.7 and above. Port to Python 3.x is not scheduled.

Bug, ports and new features
===========================

Feel free to port, patch or add any new feature to this library, and send us the pull request. We thank you in advance :)

Quick start
===========

Installing
----------

Downloading from code
_____________________

To download the latest source code enter the following command:

.. code-block:: bash

    git clone https://github.com/golismero/openvas_lib.git

Then, install the library in your default Python installation run the following command:

.. code-block:: bash

    python setup.py install

Install using pip
_________________

.. code-block:: bash

    pip install openvas_lib

Manage OpenVas server
---------------------

Connect to the server
_____________________


.. code-block:: python

    from openvas_lib import VulnscanManager, VulnscanException

    try:
        scanner = VulnscanManager(HOST, USER, PASSWORD, PORT, TIMEOUT)
    except VulnscanException as e:
        print("Error:")
        print(e)

Launch a simple scan
____________________

.. code-block:: python

    from openvas_lib import VulnscanManager, VulnscanException

    scanner = VulnscanManager(HOST, USER, PASSWORD, PORT, TIMEOUT)
    scan_id, target_id = scanner.launch_scan(target = "127.0.0.1", # Target to scan
                                             profile = "Full and fast")

Launch advanced scan
____________________

The library supports callbacks. They will be run every 10 seconds and report the status of the scan ("callback_progress") or the end of the scan ("callback_end").

.. code-block:: python

    from threading import Semaphore
    from functools import partial

    from openvas_lib import VulnscanManager, VulnscanException

    def my_print_status(i):
        print(str(i))

    def my_launch_scanner():

        sem = Semaphore(0)

        # Configure
        manager = VulnscanManager("localhost", "admin", "admin")

        # Launch
        manager.launch_scan(target,
                            profile = "empty",
                            callback_end = partial(lambda x: x.release(), sem),
                            callback_progress = my_print_status)

        # Wait
        Sem.acquire()

        # Finished scan
        print("finished")

Running it:

.. code-block:: python

    >>> my_launch_scanner() # It can take some time
    0
    10
    39
    60
    90
    finished

Get results of scan
___________________

.. code-block:: python

    from __future__ import print_function
    from openvas_lib import VulnscanManager, VulnscanException

    scanner = VulnscanManager(HOST, USER, PASSWORD, PORT, TIMEOUT)
    openvas_results = scanner.get_results(SCAN_ID)

Delete scan
___________

.. code-block:: python

    from __future__ import print_function
    from openvas_lib import VulnscanManager, VulnscanException

    scanner = VulnscanManager(HOST, USER, PASSWORD, PORT, TIMEOUT)
    scanner.delete_scan(SCAN_ID)

Delete target
_____________

.. code-block:: python

    from __future__ import print_function
    from openvas_lib import VulnscanManager, VulnscanException

    scanner = VulnscanManager(HOST, USER, PASSWORD, PORT, TIMEOUT)
    scanner.delete_target(TARGET_ID)


Parse OpenVas XML report
------------------------

You can use examples reports, available in test/ folder, as "xml" extension. This reports was made using Metasploitable
Linux distribution.

.. code-block:: pycon

    >>> from __future__ import print_function
    >>> from openvas_lib import report_parser
    >>> results = report_parser("tests/metasploitable_all.xml")
    >>> print(results)
    [<openvas_lib.data.OpenVASResult object at 0x108f2d250>, <openvas_lib.data.OpenVASResult object at 0x108f2d290>, <openvas_lib.data.OpenVASResult object at 0x108e7fcd0>, <openvas_lib.data.OpenVASResult object at 0x108e88e90>, <openvas_lib.data.OpenVASResult object at 0x108e88050>, <openvas_lib.data.OpenVASResult object at 0x108e88410>, <openvas_lib.data.OpenVASResult object at 0x108e88550>, <openvas_lib.data.OpenVASResult object at 0x108f2d650>, <openvas_lib.data.OpenVASResult object at 0x108f2d750>, <openvas_lib.data.OpenVASResult object at 0x108f2d850>, <openvas_lib.data.OpenVASResult object at 0x108f2d950>, <openvas_lib.data.OpenVASResult object at 0x108f2da50>, <openvas_lib.data.OpenVASResult object at 0x108f2db50>, <openvas_lib.data.OpenVASResult object at 0x108f2dc50>, <openvas_lib.data.OpenVASResult object at 0x108eb56d0>, <openvas_lib.data.OpenVASResult object at 0x108eb5750>, <openvas_lib.data.OpenVASResult object at 0x108f2ded0>, <openvas_lib.data.OpenVASResult object at 0x108f2dfd0>, <openvas_lib.data.OpenVASResult object at 0x108f35110>, <openvas_lib.data.OpenVASResult object at 0x108eb5950>, <openvas_lib.data.OpenVASResult object at 0x108f35210>, <openvas_lib.data.OpenVASResult object at 0x108eb5a90>, <openvas_lib.data.OpenVASResult object at 0x108eb5ad0>, <openvas_lib.data.OpenVASResult object at 0x108f355d0>, <openvas_lib.data.OpenVASResult object at 0x108f356d0>, <openvas_lib.data.OpenVASResult object at 0x108eb5dd0>, <openvas_lib.data.OpenVASResult object at 0x108f357d0>, <openvas_lib.data.OpenVASResult object at 0x108eb5f90>, <openvas_lib.data.OpenVASResult object at 0x108e101d0>, <openvas_lib.data.OpenVASResult object at 0x108e10390>, <openvas_lib.data.OpenVASResult object at 0x108eb5d90>, <openvas_lib.data.OpenVASResult object at 0x108f35910>, <openvas_lib.data.OpenVASResult object at 0x108f35a10>, <openvas_lib.data.OpenVASResult object at 0x108f35b10>, <openvas_lib.data.OpenVASResult object at 0x108f35c10>, <openvas_lib.data.OpenVASResult object at 0x108f35d10>, <openvas_lib.data.OpenVASResult object at 0x108f35e10>, <openvas_lib.data.OpenVASResult object at 0x108f35f10>, <openvas_lib.data.OpenVASResult object at 0x108f3a050>, <openvas_lib.data.OpenVASResult object at 0x108e102d0>, <openvas_lib.data.OpenVASResult object at 0x108e10910>, <openvas_lib.data.OpenVASResult object at 0x108e10ad0>, <openvas_lib.data.OpenVASResult object at 0x108e10c10>, <openvas_lib.data.OpenVASResult object at 0x108f3a150>, <openvas_lib.data.OpenVASResult object at 0x108f3a250>, <openvas_lib.data.OpenVASResult object at 0x108f3a350>, <openvas_lib.data.OpenVASResult object at 0x108f3a450>, <openvas_lib.data.OpenVASResult object at 0x108f3a550>, <openvas_lib.data.OpenVASResult object at 0x108e10e50>, <openvas_lib.data.OpenVASResult object at 0x108e10e90>, <openvas_lib.data.OpenVASResult object at 0x108e28090>, <openvas_lib.data.OpenVASResult object at 0x108f3a750>, <openvas_lib.data.OpenVASResult object at 0x108f3a910>, <openvas_lib.data.OpenVASResult object at 0x108f3aa10>, <openvas_lib.data.OpenVASResult object at 0x108e28250>, <openvas_lib.data.OpenVASResult object at 0x108e28210>, <openvas_lib.data.OpenVASResult object at 0x108e28350>, <openvas_lib.data.OpenVASResult object at 0x108e28450>, <openvas_lib.data.OpenVASResult object at 0x108f3ad10>, <openvas_lib.data.OpenVASResult object at 0x108f3ae10>, <openvas_lib.data.OpenVASResult object at 0x108f3ac10>, <openvas_lib.data.OpenVASResult object at 0x108e287d0>, <openvas_lib.data.OpenVASResult object at 0x108e28890>, <openvas_lib.data.OpenVASResult object at 0x108e289d0>, <openvas_lib.data.OpenVASResult object at 0x108e28ad0>, <openvas_lib.data.OpenVASResult object at 0x108e28c10>, <openvas_lib.data.OpenVASResult object at 0x108f3e210>, <openvas_lib.data.OpenVASResult object at 0x108e28710>, <openvas_lib.data.OpenVASResult object at 0x108e28d90>, <openvas_lib.data.OpenVASResult object at 0x108e28ed0>, <openvas_lib.data.OpenVASResult object at 0x108e28f10>, <openvas_lib.data.OpenVASResult object at 0x108e28f90>, <openvas_lib.data.OpenVASResult object at 0x108f3e510>, <openvas_lib.data.OpenVASResult object at 0x108f3e610>, <openvas_lib.data.OpenVASResult object at 0x108f3e710>, <openvas_lib.data.OpenVASResult object at 0x108f3e810>, <openvas_lib.data.OpenVASResult object at 0x108f3e910>, <openvas_lib.data.OpenVASResult object at 0x108f3ea10>, <openvas_lib.data.OpenVASResult object at 0x108f3eb10>]
    # get properties from a vuln with more info
    >>> r = None
    >>> for x in results:
      if x.id == "07cdd3dc-9f5b-4a75-a173-f7ca50bfb4f3":
        r = x
    >>> r.id
    '07cdd3dc-9f5b-4a75-a173-f7ca50bfb4f3'
    >>> r.host
    '10.211.55.35'
    >>> r.raw_description
    "\n  Summary:\n  The host is running MySQL and is prone to Denial Of Service\n  vulnerability.\n\n  Vulnerability Insight:\n  The flaw is due to an error when processing the 'ALTER DATABASE' statement and\n  can be exploited to corrupt the MySQL data directory using the '#mysql50#'\n  prefix followed by a '.' or '..'.\n\n  NOTE: Successful exploitation requires 'ALTER' privileges on a database.\n  Impact:\n  Successful exploitation could allow an attacker to cause a Denial of Service.\n  Impact Level: Application\n\n  Affected Software/OS:\n  MySQL version priot to 5.1.48 on all running platform.\n\n  Solution:\n  Upgrade to MySQL version 5.1.48\n  For updates refer to http://dev.mysql.com/downloads\n"
    >>> print(r.raw_description)
      Summary:
      The host is running MySQL and is prone to Denial Of Service
      vulnerability.

      Vulnerability Insight:
      The flaw is due to an error when processing the 'ALTER DATABASE' statement and
      can be exploited to corrupt the MySQL data directory using the '#mysql50#'
      prefix followed by a '.' or '..'.

      NOTE: Successful exploitation requires 'ALTER' privileges on a database.
      Impact:
      Successful exploitation could allow an attacker to cause a Denial of Service.
      Impact Level: Application

      Affected Software/OS:
      MySQL version priot to 5.1.48 on all running platform.

      Solution:
      Upgrade to MySQL version 5.1.48
      For updates refer to http://dev.mysql.com/downloads
    >>> r.summary
    'The host is running MySQL and is prone to Denial Of Service vulnerability.'
    >>> r.vulnerability_insight
    "The flaw is due to an error when processing the 'ALTER DATABASE' statement and can be exploited to corrupt the MySQL data directory using the '#mysql50#' prefix followed by a '.' or '..'. NOTE: Successful exploitation requires 'ALTER' privileges on a database."
    >>> r.impact
    'Successful exploitation could allow an attacker to cause a Denial of Service. Impact Level: Application'
    >>> r.affected_software
    'MySQL version priot to 5.1.48 on all running platform.'
    >>> r.solution
    'Upgrade to MySQL version 5.1.48 For updates refer to http://dev.mysql.com/downloads'
    >>> r.threat
    'Medium'
    >>> r.port.number
    3306
    >>> r.port.proto
    'tcp'
    >>> r.port.port_name
    'mysql'

