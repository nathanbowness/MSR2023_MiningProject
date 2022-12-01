sqlalchemy-vertica-python
=========================

Vertica dialect for sqlalchemy. Forked from the `Vertica ODBC dialect <https://pypi.python.org/pypi/vertica-sqlalchemy>`_, written by `James Casbon <https://github.com/jamescasbon>`_.

This module implements a Vertica dialect for SQLAlchemy using the pure-Python DB-API driver `vertica-python <https://github.com/vertica/vertica-python>`_, as adapted by `Luke Emery-Fertitta <https://github.com/lemeryfertitta>`_.

It is currently maintained by `BlueLabs <https://bluelabs.com/>`_ - PRs are welcome!

Engine creation:

.. code-block:: python

    import sqlalchemy as sa
    sa.create_engine('vertica+vertica_python://user:pwd@host:port/database')

Installation
------------

From PyPI: ::

     pip install sqlalchemy-vertica-python

From git: ::

     git clone https://github.com/bluelabsio/vertica-sqlalchemy-python
     cd vertica-sqlalchemy-python
     python setup.py install
     

Usage
------------

**ID/Primary Key Declaration**

Do not use this. The INSERT will fail as it will try to insert the ID

    id = Column(Integer, primary_key=True)

Do the following instead

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
