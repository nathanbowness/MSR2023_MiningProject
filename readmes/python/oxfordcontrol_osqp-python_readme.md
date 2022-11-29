Python interface for OSQP
=========================

.. image:: https://github.com/oxfordcontrol/qdldl-python/workflows/Build/badge.svg?branch=master
   :target: https://github.com/oxfordcontrol/osqp-python/actions


Python wrapper for `OSQP <https://osqp.org/>`__: the Operator
Splitting QP Solver.

The OSQP (Operator Splitting Quadratic Program) solver is a numerical
optimization package for solving problems in the form

::

    minimize        0.5 x' P x + q' x

    subject to      l <= A x <= u

where ``x in R^n`` is the optimization variable. The objective function
is defined by a positive semidefinite matrix ``P in S^n_+`` and vector
``q in R^n``. The linear constraints are defined by matrix
``A in R^{m x n}`` and vectors ``l in R^m U {-inf}^m``,
``u in R^m U {+inf}^m``.

Installation
------------

To install ``osqp`` for python, make sure that you're using a recent version of ``pip`` (``pip install --upgrade pip``)
and then use ``pip install osqp``.

To install `osqp` from source, clone the repository (``git clone --recurse-submodules https://github.com/osqp/osqp-python``)
and run ``pip install .`` from inside the cloned folder.

Documentation
-------------

The interface is documented `here <https://osqp.org/>`__.


Packaging
---------
This repository performs the tests and builds the pypi wheels. Conda packages are on `conda-forge <https://github.com/conda-forge/osqp-feedstock>`__.
