PySpark Stubs
=============

|Build Status| |PyPI version| |Conda Forge version|

A collection of the Apache Spark `stub
files <https://www.python.org/dev/peps/pep-0484/#stub-files>`__. These
files were generated by
`stubgen <https://github.com/python/mypy/blob/master/mypy/stubgen.py>`__
and manually edited to include accurate type hints.

Tests and configuration files have been originally contributed to the
`Typeshed project <https://github.com/python/typeshed/>`__. Please refer
to its `contributors
list <https://github.com/python/typeshed/graphs/contributors>`__ and
`license <https://github.com/python/typeshed/blob/master/LICENSE>`__ for
details.

Important
----------

This project `has been merged <https://github.com/apache/spark/commit/31a16fbb405a19dc3eb732347e0e1f873b16971d#diff-23eeeb4347bdd26bfc6b7ee9a3b755dd>`_  with the main Apache Spark repository (`SPARK-32714 <https://issues.apache.org/jira/browse/SPARK-32714>`_). All further development for Spark 3.1 and onwards will be continued there.

For Spark 2.4 and 3.0, development of this package will be continued, until their official deprecation.

- If your problem is specific to Spark 2.3 and 3.0 feel free to create an issue or open pull requests here.
- Otherwise, please check `the official Spark JIRA <https://issues.apache.org/jira/projects/SPARK/issues/>`_ and `contributing guidelines <https://spark.apache.org/contributing.html>`_. If you create a JIRA ticket or Spark PR related to type hints, please ping me with `[~zero323] <https://issues.apache.org/jira/secure/ViewProfile.jspa?name=zero323>`_ or `@zero323 <https://github.com/zero323>`_ respectively. Thanks in advance.

Motivation
----------

-  Static error detection (see
   `SPARK-20631 <https://issues.apache.org/jira/browse/SPARK-20631>`__)

   |SPARK-20631|

-  Improved autocompletion.

   |Syntax completion|

Installation and usage
----------------------

Please note that the guidelines for distribution of type information is
still work in progress (`PEP 561 - Distributing and Packaging Type
Information <https://www.python.org/dev/peps/pep-0561/>`__). Currently
installation script overlays existing Spark installations (``pyi`` stub
files are copied next to their ``py`` counterparts in the PySpark
installation directory). If this approach is not acceptable you can add stub
files to the search path manually.

According to `PEP
484 <https://www.python.org/dev/peps/pep-0484/#storing-and-distributing-stub-files>`__:

    Third-party stub packages can use any location for stub storage.
    Type checkers should search for them using PYTHONPATH.

Moreover:

    Third-party stub packages can use any location for stub storage.
    Type checkers should search for them using PYTHONPATH. A default
    fallback directory that is always checked is
    shared/typehints/python3.5/ (or 3.6, etc.)

Please check usage before proceeding.

The package is available on `PYPI <https://pypi.org/project/pyspark-stubs/>`__:

.. code:: bash

    pip install pyspark-stubs

and `conda-forge <https://anaconda.org/conda-forge/pyspark-stubs>`__:

.. code:: bash

    conda install -c conda-forge pyspark-stubs

Depending on your environment you might also need a type checker, like `Mypy`_
or `Pytype`_ [#f1]_, and autocompletion tool, like `Jedi`_.


+--------------------------------------------------+---------------------+--------------------+-------------------------------------+
| Editor                                           |  Type checking      | Autocompletion     | Notes                               |
+==================================================+=====================+====================+=====================================+
|  `Atom`_                                         | ✔ [#f2]_            | ✔ [#f3]_           | Through plugins.                    |
+--------------------------------------------------+---------------------+--------------------+-------------------------------------+
|  `IPython`_ / `Jupyter Notebook`_                | ✘ [#f4]_            | ✔                  |                                     |
+--------------------------------------------------+---------------------+--------------------+-------------------------------------+
| `PyCharm`_                                       | ✔                   | ✔                  |                                     |
+--------------------------------------------------+---------------------+--------------------+-------------------------------------+
|  `PyDev`_                                        | ✔ [#f5]_            | ?                  |                                     |
+--------------------------------------------------+---------------------+--------------------+-------------------------------------+
| `VIM`_ / `Neovim`_                               | ✔ [#f6]_            | ✔ [#f7]_           | Through plugins.                    |
+--------------------------------------------------+---------------------+--------------------+-------------------------------------+
| `Visual Studio Code`_                            | ✔ [#f8]_            | ✔ [#f9]_           | Completion with plugin              |
+--------------------------------------------------+---------------------+--------------------+-------------------------------------+
| Environment independent / other editors          | ✔ [#f10]_           | ✔ [#f11]_          | Through `Mypy`_ and `Jedi`_.        |
+--------------------------------------------------+---------------------+--------------------+-------------------------------------+




This package is tested against MyPy development branch and in rare cases (primarily important upstrean bugfixes), is not compatible with the preceding MyPy release.

PySpark Version Compatibility
-----------------------------

Package versions follow PySpark versions with exception to maintenance releases - i.e. `pyspark-stubs==2.3.0` should be compatible with `pyspark>=2.3.0,<2.4.0`.
Maintenance releases (`post1`, `post2`, ..., `postN`) are reserved for internal annotations updates.

API Coverage:
-------------

As of release 2.4.0 most of the public API is covered. For details please check `API coverage document <https://github.com/zero323/pyspark-stubs/blob/master/doc/api-coverage.rst>`__.

See also
--------

- `SPARK-17333 <https://issues.apache.org/jira/browse/SPARK-17333>`__ - *Make pyspark interface friendly with static analysis*.
- `PySpark typing hints <http://apache-spark-developers-list.1001551.n3.nabble.com/PYTHON-PySpark-typing-hints-td21560.html>`__ and `Revisiting PySpark type annotations <http://apache-spark-developers-list.1001551.n3.nabble.com/Re-PySpark-Revisiting-PySpark-type-annotations-td26232.html>`__ on `Apache Spark Developers List <http://apache-spark-developers-list.1001551.n3.nabble.com/>`__.


Disclaimer
----------

Apache Spark, Spark, PySpark, Apache, and the Spark logo are `trademarks <https://www.apache.org/foundation/marks/>`__ of `The
Apache Software Foundation <http://www.apache.org/>`__. This project is not owned, endorsed, or
sponsored by The Apache Software Foundation.

Footnotes
---------

.. [#f1] Not supported or tested.
.. [#f2] Requires `atom-mypy <https://atom.io/packages/atom-mypy>`__ or equivalent.
.. [#f3] Requires `autocomplete-python-jedi <https://atom.io/packages/autocomplete-python-jedi>`__ or equivalent.
.. [#f4] `It is possible <https://web.archive.org/web/20190126155957/http://journalpanic.com/post/spice-up-thy-jupyter-notebooks-with-mypy/>`__
         to use magics to type check directly in the notebook. In general though, you'll have to export whole notebook to `.py` file and run
         type checker on the result.
.. [#f5] Requires PyDev 7.0.3 or later.
.. [#f6] TODO Using `vim-mypy <https://github.com/Integralist/vim-mypy>`__, `syntastic <https://github.com/vim-syntastic/syntastic>`__ or `Neomake <https://github.com/neomake/neomake>`__.
.. [#f7] With `jedi-vim <https://github.com/davidhalter/jedi-vim>`__.
.. [#f8] With `Mypy linter <https://code.visualstudio.com/docs/python/linting#_specific-linters>`__.
.. [#f9] With `Python extension for Visual Studio Code <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`__.
.. [#f10] Just use your favorite checker directly, optionally combined with tool like `entr <http://eradman.com/entrproject/>`__.
.. [#f11] See `Jedi editor plugins list <https://jedi.readthedocs.io/en/latest/docs/usage.html#editor-plugins>`__.


.. |Build Status| image:: https://github.com/zero323/pyspark-stubs/actions/workflows/test.yml/badge.svg
   :target: https://github.com/zero323/pyspark-stubs/actions/workflows/test.yml
.. |PyPI version| image:: https://img.shields.io/pypi/v/pyspark-stubs.svg
   :target: https://pypi.org/project/pyspark-stubs/
.. |Conda Forge version| image:: https://img.shields.io/conda/vn/conda-forge/pyspark-stubs.svg
   :target: https://anaconda.org/conda-forge/pyspark-stubs
.. |SPARK-20631| image:: https://i.imgur.com/GfDCGjv.gif
     :alt: SPARK-20631
.. |Syntax completion| image:: https://i.imgur.com/qvkLTAp.gif
     :alt: Syntax completion

.. _Atom: https://atom.io/
.. _IPython: https://ipython.org/
.. _Jedi: https://github.com/davidhalter/jedi
.. _Jupyter Notebook: https://jupyter.org/
.. _Mypy: http://mypy-lang.org/
.. _Neovim : https://neovim.io/
.. _PyCharm: https://www.jetbrains.com/pycharm/
.. _PyDev: https://www.pydev.org/
.. _Pytype: https://github.com/google/pytype
.. _VIM: https://www.vim.org/
.. _Visual Studio Code: https://code.visualstudio.com/