===========
pytest-mock
===========

This plugin provides a ``mocker`` fixture which is a thin-wrapper around the patching API
provided by the `mock package <http://pypi.python.org/pypi/mock>`_:

.. code-block:: python

    import os

    class UnixFS:

        @staticmethod
        def rm(filename):
            os.remove(filename)

    def test_unix_fs(mocker):
        mocker.patch('os.remove')
        UnixFS.rm('file')
        os.remove.assert_called_once_with('file')


Besides undoing the mocking automatically after the end of the test, it also provides other
nice utilities such as ``spy`` and ``stub``, and uses pytest introspection when
comparing calls.

|python| |version| |anaconda| |docs| |ci| |coverage| |black| |pre-commit|

.. |version| image:: http://img.shields.io/pypi/v/pytest-mock.svg
  :target: https://pypi.python.org/pypi/pytest-mock

.. |anaconda| image:: https://img.shields.io/conda/vn/conda-forge/pytest-mock.svg
    :target: https://anaconda.org/conda-forge/pytest-mock

.. |ci| image:: https://github.com/pytest-dev/pytest-mock/workflows/test/badge.svg
  :target: https://github.com/pytest-dev/pytest-mock/actions

.. |coverage| image:: https://coveralls.io/repos/github/pytest-dev/pytest-mock/badge.svg?branch=master
  :target: https://coveralls.io/github/pytest-dev/pytest-mock?branch=master

.. |python| image:: https://img.shields.io/pypi/pyversions/pytest-mock.svg
  :target: https://pypi.python.org/pypi/pytest-mock/

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
  :target: https://github.com/ambv/black

.. |pre-commit| image:: https://results.pre-commit.ci/badge/github/pytest-dev/pytest-mock/master.svg
   :target: https://results.pre-commit.ci/latest/github/pytest-dev/pytest-mock/master

.. |docs| image:: https://readthedocs.org/projects/pytest-mock/badge/?version=latest
   :target: https://pytest-mock.readthedocs.io/en/latest/?badge=latest


`Professionally supported pytest-mock is available <https://tidelift.com/subscription/pkg/pypi-pytest_mock?utm_source=pypi-pytest-mock&utm_medium=referral&utm_campaign=readme>`_.


Documentation
=============

For full documentation, please see https://pytest-mock.readthedocs.io/en/latest.

License
=======

Distributed under the terms of the `MIT`_ license.


.. _MIT: https://github.com/pytest-dev/pytest-mock/blob/master/LICENSE
