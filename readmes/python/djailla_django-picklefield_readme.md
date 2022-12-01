django-picklefield
==================

.. image:: https://img.shields.io/pypi/l/django-picklefield.svg?style=flat
    :target: https://pypi.python.org/pypi/django-picklefield/
    :alt: License

.. image:: https://img.shields.io/pypi/v/django-picklefield.svg?style=flat
    :target: https://pypi.python.org/pypi/django-picklefield/
    :alt: Latest Version

.. image:: https://travis-ci.org/gintas/django-picklefield.svg?branch=master
    :target: https://travis-ci.org/gintas/django-picklefield
    :alt: Build Status

.. image:: https://coveralls.io/repos/gintas/django-picklefield/badge.svg?branch=master
    :target: https://coveralls.io/r/gintas/django-picklefield?branch=master
    :alt: Coverage Status

.. image:: https://img.shields.io/pypi/pyversions/django-picklefield.svg?style=flat
    :target: https://pypi.python.org/pypi/django-picklefield/
    :alt: Supported Python Versions

.. image:: https://img.shields.io/pypi/wheel/django-picklefield.svg?style=flat
    :target: https://pypi.python.org/pypi/django-picklefield/
    :alt: Wheel Status

-----
About
-----

**django-picklefield** provides an implementation of a pickled object field.
Such fields can contain any picklable objects.

The implementation is taken and adopted from `Django snippet #1694`_ by Taavi
Taijala, which is in turn based on `Django snippet #513`_  by Oliver Beattie.

django-picklefield is available under the MIT license.

.. _Django snippet #1694: http://www.djangosnippets.org/snippets/1694/
.. _Django snippet #513: http://www.djangosnippets.org/snippets/513/

-----
Usage
-----

First of all, you need to have **django-picklefield** installed; for your
convenience, recent versions should be available from PyPI.

To use, just define a field in your model:

.. code:: python

    >>> from picklefield.fields import PickledObjectField
    ... class SomeObject(models.Model):
    ...     args = PickledObjectField()

and assign whatever you like (as long as it's picklable) to the field:

.. code:: python

    >>> obj = SomeObject()
    >>> obj.args = ['fancy', {'objects': 'inside'}]
    >>> obj.save()


-----
Notes
-----

If you need to serialize an object with a PickledObjectField for transmission
to the browser, you may need to subclass the field and override the
``value_to_string()`` method.  Currently pickle fields are serialized as
base64-encoded pickles, which allows reliable deserialization, but such a
format is not convenient for parsing in the browser.  By overriding
``value_to_string()`` you can choose a more convenient serialization format.

Fields now accept the boolean key word argument `copy`, which defaults to
`True`. The `copy` is necessary for lookups to work correctly. If you don't
care about performing lookups on the picklefield, you can set `copy=False` to
save on some memory usage. This an be especially beneficial for very large
object trees.

-------------
Running tests
-------------

The full test suite can be run with `Tox`_::

    >>> pip install tox
    >>> tox

.. _Tox: https://testrun.org/tox/latest/

--------------
Original notes
--------------

Here are the notes by taavi223, the original author:

Incredibly useful for storing just about anything in the database (provided it
is Pickle-able, of course) when there isn't a 'proper' field for the job.

PickledObjectField is database-agnostic, and should work with any database
backend you can throw at it. You can pass in any Python object and it will
automagically be converted behind the scenes. You never have to manually pickle
or unpickle anything. Also works fine when querying; supports exact, in, and
isnull lookups. It should be noted, however, that calling QuerySet.values()
will only return the encoded data, not the original Python object.

This PickledObjectField has a few improvements over the one in snippet #513.

This one solves the DjangoUnicodeDecodeError problem when saving an object
containing non-ASCII data by base64 encoding the pickled output stream. This
ensures that all stored data is ASCII, eliminating the problem.

PickledObjectField will now optionally use zlib to compress (and uncompress)
pickled objects on the fly. This can be set per-field using the keyword
argument "compress=True". For most items this is probably not worth the small
performance penalty, but for Models with larger objects, it can be a real space
saver.

You can also now specify the pickle protocol per-field, using the protocol
keyword argument. The default of 2 should always work, unless you are trying to
access the data from outside of the Django ORM.

Worked around a rare issue when using the cPickle and performing lookups of
complex data types. In short, cPickle would sometimes output different streams
for the same object depending on how it was referenced. This of course could
cause lookups for complex objects to fail, even when a matching object exists.
See the docstrings and tests for more information.

You can now use the isnull lookup and have it function as expected. A
consequence of this is that by default, PickledObjectField has null=True set
(you can of course pass null=False if you want to change that). If null=False
is set (the default for fields), then you wouldn't be able to store a Python
None value, since None values aren't pickled or encoded (this in turn is what
makes the isnull lookup possible).

You can now pass in an object as the default argument for the field without it
being converted to a unicode string first. If you pass in a callable though,
the field will still call it. It will not try to pickle and encode it.

You can manually import dbsafe_encode and dbsafe_decode from fields.py if you
want to encode and decode objects yourself. This is mostly useful for decoding
values returned from calling QuerySet.values(), which are still encoded
strings.

Note: If you are trying to store other django models in the PickledObjectField,
please see the comments for a discussion on the problems associated with doing
that. The easy solution is to put django models into a list or tuple before
assigning them to the PickledObjectField.

Update 9/2/09: Fixed the value_to_string method so that serialization should
now work as expected. Also added deepcopy back into dbsafe_encode, fixing #4
above, since deepcopy had somehow managed to remove itself. This means that
lookups should once again work as expected in all situations. Also made the
field editable=False by default (which I swear I already did once before!)
since it is never a good idea to have a PickledObjectField be user editable.

-------
Changes
-------

Changes in version 3.0.0
========================

* Allowed default pickle protocol to be overriden using the
  `PICKLEFIELD_DEFAULT_PROTOCOL` setting.
* Dropped support for Python 2.
* Added testing against Django 3.0.
* Dropped support for Django 1.11.

Changes in version 2.1.0
========================

* Added official support for Django 2.2 (thanks to joehybird).
* Dropped support for Django 2.0 and 2.1 (thanks to joehybird).
* Dropped support for Python 3.4 (thanks to joehybidd).

Changes in version 2.0.0
========================

* Silenced ``RemovedInDjango30Warning`` warnings on Django 2.0+ (thanks to
  canarduck).
* Restructured project directories.
* Disallowed the usage of empty strings for ``PickledObjectField``. That makes
  ``.save()``, ``.create()``, etc. raise ``IntegrityError`` if `null` is not
  ``True`` and no default value was specified like built-in fields do
  (thanks to Attila-Mihaly Balazs).
* Added a check for mutable default values to ``PickledObjectField``.

Changes in version 1.1.0
========================

* Added support for Django 2.1 and dropped support for Django < 1.11.

Changes in version 1.0.0
========================

* Added a new option to prevent a copy of the object before pickling: `copy=True`
* Dropped support for Django 1.4
* Dropped support for Django 1.7
* Dropped support for Python 3.2
* Added support for Python 3.6

Changes in version 0.3.2
========================

* Dropped support for Django 1.3.
* Dropped support for Python 2.5.
* Silenced deprecation warnings on Django 1.8+.

Changes in version 0.3.1
========================

* Favor the built in json module (thanks to Simon Charette).

Changes in version 0.3.0
========================

* Python 3 support (thanks to Rafal Stozek).

Changes in version 0.2.0
========================

* Allow pickling of subclasses of django.db.models.Model (thanks to Simon
  Charette).

Changes in version 0.1.9
========================

* Added `connection` and `prepared` parameters to `get_db_prep_value()` too
  (thanks to Matthew Schinckel).

Changes in version 0.1.8
========================

* Updated link to code repository.

Changes in version 0.1.7
========================

* Added `connection` and `prepared` parameters to `get_db_prep_lookup()` to
  get rid of deprecation warnings in Django 1.2.

Changes in version 0.1.6
========================

* Fixed South support (thanks aehlke@github).

Changes in version 0.1.5
========================

* Added support for South.
* Changed default to null=False, as is common throughout Django.

Changes in version 0.1.4
========================

* Updated copyright statements.

Changes in version 0.1.3
========================

* Updated serialization tests (thanks to Michael Fladischer).

Changes in version 0.1.2
========================

* Added Simplified BSD licence.

Changes in version 0.1.1
========================

* Added test for serialization.
* Added note about JSON serialization for browser.
* Added support for different pickle protocol versions (thanks to Michael
  Fladischer).

Changes in version 0.1
======================

* First public release.


--------
Feedback
--------

There is a home page <http://github.com/gintas/django-picklefield>
with instructions on how to access the code repository.

Send feedback and suggestions to gintautas@miliauskas.lt .