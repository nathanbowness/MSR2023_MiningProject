django-bleach - Bleach and sanitise user HTML
=============================================

.. image:: https://readthedocs.org/projects/django-bleach/badge/?version=latest
   :target: https://django-bleach.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: http://img.shields.io/pypi/v/django-bleach.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-bleach/
    :alt: Latest Version

.. image:: http://img.shields.io/pypi/l/django-bleach.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-bleach/
    :alt: License

.. image:: http://img.shields.io/pypi/dm/django-bleach.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-bleach/
    :alt: Downloads

|

.. image:: https://codecov.io/gh/marksweb/django-bleach/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/marksweb/django-bleach

.. image:: https://api.codacy.com/project/badge/Grade/c34f923ab0a84a6f96728866c749d511
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/marksweb/django-bleach?utm_source=github.com&utm_medium=referral&utm_content=marksweb/django-bleach&utm_campaign=Badge_Grade_Dashboard

.. image:: https://results.pre-commit.ci/badge/github/marksweb/django-bleach/master.svg
   :target: https://results.pre-commit.ci/latest/github/marksweb/django-bleach/master
   :alt: pre-commit.ci status

.. image:: https://img.shields.io/lgtm/grade/python/g/marksweb/django-bleach.svg?logo=lgtm&logoWidth=18
   :target: https://lgtm.com/projects/g/marksweb/django-bleach/context:python
   :alt: Language grade: Python

.. image:: https://img.shields.io/lgtm/alerts/g/marksweb/django-bleach.svg?logo=lgtm&logoWidth=18
   :target: https://lgtm.com/projects/g/marksweb/django-bleach/alerts/
   :alt: Total alerts

|

Bleach_ is a Python module that takes any HTML input, and returns
valid, sanitised HTML that contains only an allowed subset of HTML tags,
attributes and styles. ``django-bleach`` is a Django app that makes using
``bleach`` extremely easy.

`Read the documentation here`_.

Setup
-----

1. Install ``django-bleach`` via ``pip``::

    pip install django-bleach

2. Add ``django-bleach`` to your ``INSTALLED_APPS``:

   .. code-block:: python

        INSTALLED_APPS = [
            # ...
            'django_bleach',
            # ...
        ]

3. Select some sensible defaults for the allowed tags, attributes and styles;
   and the behaviour when unknown tags are encountered. Each of these are
   optional, and default to using the ``bleach`` defaults. See the
   `bleach documentation`_:

   .. code-block:: python

        # Which HTML tags are allowed
        BLEACH_ALLOWED_TAGS = ['p', 'b', 'i', 'u', 'em', 'strong', 'a']

        # Which HTML attributes are allowed
        BLEACH_ALLOWED_ATTRIBUTES = ['href', 'title', 'style']

        # Which CSS properties are allowed in 'style' attributes (assuming
        # style is an allowed attribute)
        BLEACH_ALLOWED_STYLES = [
            'font-family', 'font-weight', 'text-decoration', 'font-variant']

        # Strip unknown tags if True, replace with HTML escaped characters if
        # False
        BLEACH_STRIP_TAGS = True

        # Strip comments, or leave them in.
        BLEACH_STRIP_COMMENTS = False

4. Select the default widget for bleach fields. This defaults to
   ``django.forms.Textarea``, but you will probably want to replace it with a
   WYSIWYG editor, or something similar:

   .. code-block:: python

        # Use the CKEditorWidget for bleached HTML fields
        BLEACH_DEFAULT_WIDGET = 'wysiwyg.widgets.WysiwygWidget'

   I use `django-ckeditor`_ in my projects, but what you use is up to you.

Usage
-----

In your models
**************

``django-bleach`` provides three ways of creating bleached output. The simplest
way of including user-editable HTML content that is automatically sanitised is
by using the ``BleachField`` model field:

.. code-block:: python

    # in app/models.py

    from django import models
    from django_bleach.models import BleachField

    class Post(models.Model):

        title = models.CharField()
        content = BleachField()

        # ...

``BleachField`` takes the following arguments, to customise the output of
``bleach``. See the `bleach documentation`_ for their use:

* ``allowed_tags``
* ``allowed_attributes``
* ``strip_tags``
* ``strip_comments``
* ``css_sanitizer``

The following argument will be deprecated in the near future:

* ``allowed_styles``

In addition to the ``bleach``-specific arguments, the ``BleachField`` model field
accepts all of the normal field attributes. Behind the scenes, it is a
``TextField``, and accepts all the same arguments as the default ``TextField`` does.

The ``BleachField`` model field sanitises its value before it is saved to the
database and is marked safe so it can be immediately rendered in a template
without further intervention.

In model forms, ``BleachField`` model field are represented with the
``BleachField`` form field by default.

In your forms
*************

A ``BleachField`` form field is provided. This field sanitises HTML input from
the user, and presents safe, clean HTML to your Django application and the
returned value is marked safe for immediate rendering.

In your templates
*****************

If you have a piece of content from somewhere that needs to be printed in a
template, you can use the ``bleach`` filter:

.. code-block:: django

    {% load bleach_tags %}

    {{ some_unsafe_content|bleach }}

If filter has no arguments it uses default settings defined in your
application settings. You can override allowed tags by specifying them
as a parameter to the filter:

.. code-block:: django

    {{ some_unsafe_content|bleach:"p,span" }}

There is also ``bleach_linkify`` which uses the linkify_ function of bleach
which converts URL-like strings in an HTML fragment to links

This function converts strings that look like URLs, domain names and email
addresses in text that may be an HTML fragment to links, while preserving:

1. links already in the string
2. urls found in attributes
3. email addresses


.. _bleach: https://github.com/mozilla/bleach
.. _Read the documentation here: https://django-bleach.readthedocs.io/
.. _bleach documentation: https://bleach.readthedocs.io/en/latest/clean.html
.. _django-ckeditor: https://github.com/shaunsephton/django-ckeditor
.. _linkify: https://bleach.readthedocs.io/en/latest/linkify.html?highlight=linkify#bleach.linkify "linkify"
