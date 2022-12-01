
.. raw:: html

    <h1 align="center">
    <br>
      <a href="https://www.pythonsheets.com"><img src="docs/_static/logo.svg" alt="pysheeet" width=200"></a>
    </h1>
    <p align="center">
      <a href="https://github.com/crazyguitar/pysheeet/actions">
        <img src="https://github.com/crazyguitar/pysheeet/actions/workflows/pythonpackage.yml/badge.svg" alt="Build Status">
      </a>
      <a href="https://coveralls.io/github/crazyguitar/pysheeet?branch=master">
        <img src="https://coveralls.io/repos/github/crazyguitar/pysheeet/badge.svg?branch=master" alt="Coverage">
      </a>
      <a href="https://raw.githubusercontent.com/crazyguitar/pysheeet/master/LICENSE">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License MIT">
      </a>
    </p>

Introduction
=============

Pysheeet was created with intention of collecting python code snippets for
reducing coding hours and making life easier and faster. Any contributions are welcome.
Please feel free to fork and send a pull request to this project.


What’s New In Python 3
======================

This part only provides a quick glance at some important features in Python 3.
If you're interested in all of the most important features, please read the
official document, `What’s New in Python <https://docs.python.org/3/whatsnew/index.html>`_.

- `New in Python3 <docs/notes/python-new-py3.rst>`_


Cheat Sheet
===========

- `Code Style <docs/notes/python-code-style.rst>`_
- `From Scratch <docs/notes/python-basic.rst>`_
- `Future <docs/notes/python-future.rst>`_
- `Unicode <docs/notes/python-unicode.rst>`_
- `List <docs/notes/python-list.rst>`_
- `Set <docs/notes/python-set.rst>`_
- `Dictionary <docs/notes/python-dict.rst>`_
- `Heap <docs/notes/python-heap.rst>`_
- `Function <docs/notes/python-func.rst>`_
- `Class <docs/notes/python-object.rst>`_
- `Generator <docs/notes/python-generator.rst>`_
- `Typing <docs/notes/python-typing.rst>`_
- `Time <docs/notes/python-date.rst>`_
- `File <docs/notes/python-io.rst>`_
- `Operating System <docs/notes/python-os.rst>`_


Advanced Cheat Sheet
====================

- `Regular expression <docs/notes/python-rexp.rst>`_
- `Socket <docs/notes/python-socket.rst>`_
- `Asyncio <docs/notes/python-asyncio.rst>`_
- `Concurrency <docs/notes/python-concurrency.rst>`_
- `Sqlalchemy <docs/notes/python-sqlalchemy.rst>`_
- `Security <docs/notes/python-security.rst>`_
- `SSH <docs/notes/python-ssh.rst>`_
- `Boto3 <docs/notes/python-aws.rst>`_
- `Tests <docs/notes/python-tests.rst>`_
- `C Extensions <docs/notes/python-c-extensions.rst>`_


Appendix
=========

- `Why does Decorator Need @wraps <docs/appendix/python-decorator.rst>`_
- `A Hitchhikers Guide to Asynchronous Programming <docs/appendix/python-concurrent.rst>`_
- `Asyncio behind the Scenes <docs/appendix/python-asyncio.rst>`_
- `PEP 572 and the walrus operator <docs/appendix/python-walrus.rst>`_
- `Python Interpreter in GNU Debugger <docs/appendix/python-gdb.rst>`_

PDF Version
============

`pdf`_

.. _pdf: https://media.readthedocs.org/pdf/pysheeet/latest/pysheeet.pdf

How to run the server
=======================

.. code-block:: bash

    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt
    $ make
    $ python app.py

    # URL: localhost:5000
