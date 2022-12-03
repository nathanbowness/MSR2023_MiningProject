DbBot-SQLAlchemy
================

.. image:: https://travis-ci.org/pbylicki/DbBot-SQLAlchemy.svg?branch=master
    :target: https://travis-ci.org/pbylicki/DbBot-SQLAlchemy

DbBot is a Python script to serialize `Robot Framework`_  output files into
a SQLite database. This way the future `Robot Framework`_ related tools and
plugins will have a unified storage for the test run results.

DbBot-SQLAlchemy is a fork of DbBot project that is using SQLAlchemy in order
to store test run results in any of the major supported database systems.

The goal is to support the following databases:

-  PostgreSQL
-  MySQL
-  Oracle
-  MS SQL
-  SQLite

Requirements
------------
DbBot-SQLAlchemy is tested on

-  `Python`__ 3.5+
-  `Robot Framework`_ 3.0+
-  `SQLAlchemy`_ 1.2+

It may (though it is not guaranteed) work with older versions of dependencies.

How it works
------------

The script takes one or more `output.xml` files as input, initializes the
database schema, and stores the respective results into a SQLite database
(`robot\_results.db` by default, can be changed by specifying SQLAlchemy
database URL with options `-b` or `--database`).
If database schema is already existing, it will insert the new
results into that database.

Installation
------------

This tool is installed with pip with command:

::

    $ pip install dbbot-sqlalchemy

Alternatively you can download the `source distribution`__, extract it and
install using:

::

    $ python setup.py install

What is stored
--------------

Both the test data (names, content) and test statistics (how many did pass or
fail, possible errors occurred, how long it took to run, etc.) related to
suites and test cases are stored by default. However, keywords and related
data are not stored as it might take order of magnitude longer for massive
test runs. You can choose to store keywords and related data by using `-k` or
`--also-keywords` flag.

Usage examples
--------------

Typical usage with a single output.xml file:

::

    python -m dbbot.run atests/testdata/one_suite/test_output.xml

If the database does not already exist, it's created. Otherwise the test
results are just inserted into the existing database. Only new results are
inserted.

The default database is SQLite database named `robot_results.db`.

Additional options are:

+-------------------+---------------------------+--------------------------+
| Short format      | Long format               | Description              |
+===================+===========================+==========================+
| `-k`              | `--also-keywords`         | Parse also suites' and   |
|                   |                           | tests' keywords          |
+-------------------+---------------------------+--------------------------+
| `-v`              | `--verbose`               | Print output to the      |
|                   |                           | console.                 |
+-------------------+---------------------------+--------------------------+
| `-b DB_URL`       | `--database=DB_URL`       | SQLAlchemy database URL  |
|                   |                           | for test run results     |
+-------------------+---------------------------+--------------------------+
| `-d`              | `--dry-run`               | Do everything except     |
|                   |                           | store the results.       |
+-------------------+---------------------------+--------------------------+


Specifying custom database name:

::

    $ python -m dbbot.run  -b sqlite:///my_own_database.db atests/testdata/one_suite/test_output.xml
    $ python -m dbbot.run  -b postgresql://postgres:postgres@localhost:5432/postgres atests/testdata/one_suite/test_output.xml

Parsing test run results with keywords and related data included:

::

    python -m dbbot.run -k atests/testdata/one_suite/test_output.xml

Giving multiple test run result files at the same time:

::

    python -m dbbot.run atests/testdata/one_suite/test_output.xml atests/testdata/one_suite/output_latter.xml

Database
--------

You can inspect the created database using the `sqlite3`_ command-line tool:

.. code:: sqlite3

    $ sqlite3 robot_results.db

    sqlite> .tables
    arguments        suite_status     test_run_errors  tests
    keyword_status   suites           test_run_status
    keywords         tag_status       test_runs
    messages         tags             test_status

    sqlite> SELECT count(), tests.id, tests.name
            FROM tests, test_status
            WHERE tests.id == test_status.test_id AND
            test_status.status == "FAIL"
            GROUP BY tests.name;

Please note that when database is initialized, no indices are created by
DbBot. This is to avoid slowing down the inserts. You might want to add
indices to the database by hand to speed up certain queries in your own
scripts.

For information about the database schema, see `doc/robot_database.md`__.

Use case example: Most failing tests
------------------------------------

One of the common use cases for DbBot is to get a report of the most commonly
failing suites, tests and keywords. There's an example for this purpose in
`examples/FailBot/bin/failbot`.

Failbot is a Python script used to produce a summary web page of the failing
suites, tests and keywords, using the information stored in the DbBot
database. Please adjust (the barebone) HTML templates in
`examples/FailBot/templates` to your needs.

Writing your own scripts
------------------------

Please take a look at the modules in `examples/FailBot/failbot` as an example
on how to build on top of the classes provided by DbBot to satisfy your own
scripting needs.

License
-------

DbBot is released under the `Apache License, Version 2.0`__.

See LICENSE.TXT for details.

__ https://www.python.org/
__ https://pypi.python.org/pypi/dbbot-sqlalchemy
__ https://github.com/pbylicki/DbBot-SQLAlchemy/blob/master/doc/robot_database.md
__ http://www.tldrlegal.com/license/apache-license-2.0
.. _`Robot Framework`: http://www.robotframework.org
.. _`pip`: http://www.pip-installer.org
.. _`sqlite3`: https://www.sqlite.org/sqlite.html
.. _`SQLAlchemy`: http://www.sqlalchemy.org
