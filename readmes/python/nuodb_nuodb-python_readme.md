==============
NuoDB - Python
==============

.. image:: https://app.travis-ci.com/nuodb/nuodb-python.svg?branch=master
    :target: https://app.travis-ci.com/github/nuodb/nuodb-python
    :alt: Test Results
.. image:: https://gitlab.com/cadmin/nuodb-python/badges/master/pipeline.svg
    :target: https://gitlab.com/nuodb-mirror/nuodb-python/-/jobs
    :alt: Dependency Verification

.. contents::

This package contains the community driven pure-Python NuoDB_ client library
that provides a standard `PEP 249`_ SQL API. This is a community driven driver
with limited support and testing from NuoDB.

Requirements
------------

* Python -- one of the following:

  - CPython_ >= 2.7

* NuoDB -- one of the following:

  - NuoDB_ >= 2.0.4

If you don't have a NuoDB domain available you can create one using the Docker
image on DockerHub.  See `Quick Start Guides / Docker <https://doc.nuodb.com/nuodb/latest/quick-start-guide/docker/>`_.

Installation
------------

The current stable release is available on PyPI and can be installed with
``pip``::

    $ pip install pynuodb

Alternatively (e.g. if ``pip`` is not available), a tarball can be downloaded
from GitHub and installed with Setuptools::

    $ curl -L https://github.com/nuodb/nuodb-python/archive/master.tar.gz | tar xz
    $ cd nuodb-python*
    $ python setup.py install
    # The folder nuodb-python* can be safely removed now.

Example
-------

Here is an example using the `PEP 249`_ API that creates some tables, inserts
some data, runs a query, and cleans up after itself:

.. code:: python

    import pynuodb

    options = {"schema": "test"}
    connect_kw_args = {'database': "test", 'host': "localhost", 'user': "dba", 'password': "dba", 'options': options}

    connection = pynuodb.connect(**connect_kw_args)
    cursor = connection.cursor()
    try:
        stmt_drop = "DROP TABLE IF EXISTS names"
        cursor.execute(stmt_drop)

        stmt_create = """
        CREATE TABLE names (
            id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            name VARCHAR(30) DEFAULT '' NOT NULL,
            age INTEGER DEFAULT 0
        )"""
        cursor.execute(stmt_create)

        names = (('Greg', 17,), ('Marsha', 16,), ('Jan', 14,))
        stmt_insert = "INSERT INTO names (name, age) VALUES (?, ?)"
        cursor.executemany(stmt_insert, names)

        connection.commit()

        age_limit = 15
        stmt_select = "SELECT id, name FROM names where age > ? ORDER BY id"
        cursor.execute(stmt_select, (age_limit,))
        print("Results:")
        for row in cursor.fetchall():
            print("%d | %s" % (row[0], row[1]))

    finally:
        cursor.execute(stmt_drop)
        cursor.close()
        connection.close()

For further information on getting started with NuoDB, please refer to the Documentation_.

Resources
---------

DB-API 2.0: https://www.python.org/dev/peps/pep-0249/

NuoDB Documentation: https://doc.nuodb.com/nuodb/latest/introduction-to-nuodb/

License
-------

PyNuoDB is licensed under a `BSD 3-Clause License <https://github.com/nuodb/nuodb-python/blob/master/LICENSE>`_.

.. _Documentation: https://doc.nuodb.com/nuodb/latest/introduction-to-nuodb/
.. _NuoDB: https://www.nuodb.com/
.. _CPython: https://www.python.org/
.. _PEP 249: https://www.python.org/dev/peps/pep-0249/
