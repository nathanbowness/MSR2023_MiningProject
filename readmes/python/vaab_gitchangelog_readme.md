============
gitchangelog
============

.. image:: https://img.shields.io/pypi/v/gitchangelog.svg?style=flat
   :target: https://pypi.python.org/pypi/gitchangelog/
   :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/gitchangelog.svg?style=flat
   :target: https://pypi.python.org/pypi/gitchangelog/
   :alt: Number of PyPI downloads

.. image:: https://img.shields.io/travis/vaab/gitchangelog/master.svg?style=flat
   :target: https://travis-ci.org/vaab/gitchangelog/
   :alt: Travis CI build status

.. image:: https://img.shields.io/appveyor/ci/vaab/gitchangelog.svg
   :target: https://ci.appveyor.com/project/vaab/gitchangelog/branch/master
   :alt: Appveyor CI build status

.. image:: https://img.shields.io/codecov/c/github/vaab/gitchangelog.svg
   :target: https://codecov.io/gh/vaab/gitchangelog
   :alt: Test coverage


Use your commit log to make beautifull and configurable changelog file.


Feature
=======

- fully driven by a config file that can be tailored with your changelog
  policies. (see for example the `reference configuration file`_)
- filter out commits/tags based on regexp matching
- refactor commit summary, or commit body on the fly with replace regexp
- classify commit message into sections (ie: New, Fix, Changes...)
- any output format supported thanks to templating, you can even choose
  your own preferred template engine (mako, mustache, full python ...).
- support your merge or rebase workflows and complicated git histories
- support full or incremental changelog generation to match your needs.
- support easy access to `trailers key values`_ (if you use them)
- support of multi-authors for one commit through ``Co-Authored-By`` `trailers key values`_
- support standard python installation or dep-free single executable.
  (this last feature is not yet completely pain free to use on Windows)

.. _trailers key values: https://git.wiki.kernel.org/index.php/CommitMessageConventions


Requirements
============

``gitchangelog`` is compatible Python 2 and Python 3 on
Linux/BSD/MacOSX and Windows.

Please submit an issue if you encounter incompatibilities.


Installation
============


full package
------------

Gitchangelog is published on PyPI, thus:

    pip install gitchangelog

\.. is the way to go for install the full package on any platform.

If you are installing from source, please note that the development tools
are not working fully yet on Windows.

The full package provides the ``gitchangelog.py`` executable as long as:

- a `reference configuration file`_ that provides system wide defaults for
  all values.
- some example templates in ``mustache`` and ``mako`` templating
  engine's language. Ideal to bootstrap your variations.


from source
-----------

If you'd rather work from the source repository, it supports the common
idiom to install it on your system::

    python setup.py install

Note that for linux/BSD, there's a link to the executable in the root of the
source. This can be a convenient way to work on the source version.


single executable installation
------------------------------

The file ``gitchangelog.py`` is a full blown executable and can be used
without any other files. This is easier to use naturally on Linux/BSD
systems. For instance, you could type in::

    curl -sSL https://raw.githubusercontent.com/vaab/gitchangelog/master/src/gitchangelog/gitchangelog.py > /usr/local/bin/gitchangelog &&
    chmod +x /usr/local/bin/gitchangelog

It'll install ``gitchangelog`` to be accessible for all users and will
use the default python interpreter of your running session.

Please note: if you choose to install it in this standalone mode, then
you must make sure to value at least all the required configuration
keys in your config file. As a good start you should probably copy the
`reference configuration file`_ as you base configuration file.

This is due to the fact that ``gitchangelog`` can not anymore reach
the reference configuration file to get default values.


Sample
======

The default output is ReSTructured text, so it should be readable in ASCII.

Here is a small sample of the ``gitchangelog`` changelog at work.

Current ``git log`` output so you can get an idea of the log history::

  * 59f902a Valentin Lab new: dev: sections in changelog are now in the order given in ``gitchangelog.rc`` in the ``section_regexps`` option.  (0.1.2)
  * c6f72cc Valentin Lab chg: dev: commented code to toggle doctest mode.
  * a9c38f3 Valentin Lab fix: dev: doctests were failing on this.
  * 59524e6 Valentin Lab new: usr: added ``body_split_regexp`` option to attempts to format correctly body of commit.
  * 5883f07 Valentin Lab new: usr: use a list of tuple instead of a dict for ``section_regexps`` to be able to manage order between section on find match.
  * 7c1d480 Valentin Lab new: dev: new ``unreleased_version_label`` option in ``gitchangelog.rc`` to change label of not yet released code.
  * cf29c9c Valentin Lab fix: dev: bad sorting of tags (alphanumerical). Changed to commit date sort.
  * 61d8f80 Valentin Lab fix: dev: support of empty commit message.
  * eeca31b Valentin Lab new: dev: use ``gitchangelog`` section in ``git config`` world appropriately.
  * 6142b71 Valentin Lab chg: dev: cosmetic removal of trailing whitespaces
  * 3c3edd5 Valentin Lab fix: usr: ``git`` in later versions seems to fail on ``git config <key>`` with errlvl 255, that was not supported.
  * 3f9617d Valentin Lab fix: usr: removed Traceback when there were no tags at all in the current git repository.
  * e0db9ae Valentin Lab new: usr: added section classifiers (ie: New, Change, Bugs) and updated the sample rc file.  (0.1.1)
  * 0c66d59 Valentin Lab fix: dev: Fixed case where exception was thrown if two tags are on the same commit.
  * d2fae0d Valentin Lab new: usr: added a succint ``--help`` support.

And here is the ``gitchangelog`` output::

  0.1.2 (2011-05-17)
  ------------------

  New
  ~~~
  - Sections in changelog are now in the order given in ``git-
    changelog.rc`` in the ``section_regexps`` option. [Valentin Lab]
  - Added ``body_split_regexp`` option to attempts to format correctly
    body of commit. [Valentin Lab]
  - Use a list of tuple instead of a dict for ``section_regexps`` to be
    able to manage order between section on find match. [Valentin Lab]
  - New ``unreleased_version_label`` option in ``gitchangelog.rc`` to
    change label of not yet released code. [Valentin Lab]
  - Use ``gitchangelog`` section in ``git config`` world appropriately.
    [Valentin Lab]

  Changes
  ~~~~~~~
  - Commented code to toggle doctest mode. [Valentin Lab]
  - Cosmetic removal of trailing whitespaces. [Valentin Lab]

  Fix
  ~~~
  - Doctests were failing on this. [Valentin Lab]
  - Bad sorting of tags (alphanumerical). Changed to commit date sort.
    [Valentin Lab]
  - Support of empty commit message. [Valentin Lab]
  - ``git`` in later versions seems to fail on ``git config <key>`` with
    errlvl 255, that was not supported. [Valentin Lab]
  - Removed Traceback when there were no tags at all in the current git
    repository. [Valentin Lab]


  0.1.1 (2011-04-07)
  ------------------

  New
  ~~~
  - Added section classifiers (ie: New, Change, Bugs) and updated the
    sample rc file. [Valentin Lab]
  - Added a succint ``--help`` support. [Valentin Lab]

  Fix
  ~~~
  - Fixed case where exception was thrown if two tags are on the same
    commit. [Valentin Lab]

And the rendered full result is directly used to generate the HTML webpage of
the `changelog of the PyPI page`_.


Usage
=====

The `reference configuration file`_ is delivered within
``gitchangelog`` package and is used to provides defaults to
settings. If you didn't install the package and used the standalone
file, then chances are that ``gitchangelog`` can't access these
defaults values. This is not a problem as long as you provided all the
required values in your config file.

The recommended location for ``gitchangelog`` config file is the root
of the current git repository with the name ``.gitchangelog.rc``.
However you could put it elsewhere, and here are the locations checked
(first match will prevail):

- in the path given thanks to the environment variable
  ``GITCHANGELOG_CONFIG_FILENAME``
- in the path stored in git config's entry ``gitchangelog.rc-path`` (which
  could be stored in system location or per repository)
- (RECOMMENDED) in the root of the current git repository with the name
  ``.gitchangelog.rc``

Then, you'll be able to call ``gitchangelog`` in a GIT repository and it'll
print changelog on its standard output.


Configuration file format
-------------------------

The `reference configuration file`_ is quite heavily commented and is quite
simple.  You should be able to use it as required.

.. _reference configuration file: https://github.com/vaab/gitchangelog/blob/master/src/gitchangelog/gitchangelog.rc.reference

The changelog of gitchangelog is generated with himself and with the reference
configuration file. You'll see the output in the `changelog of the PyPI page`_.

.. _changelog of the PyPI page: http://pypi.python.org/pypi/gitchangelog


Output Engines
--------------

At the end of the configuration file, you'll notice a variable called
``output_engine``. By default, it's set to ``rest_py``, which is the
legacy python engine to produce the `ReSTructured Text` output format
that is shown in above samples. If this engine fits your needs, you
won't need to fiddle with this option.

To render the template, ``gitchangelog`` will generate a data structure that
will then be rendered thanks to the output engine. This should help you get
the exact output that you need.

As people might have different needs and knowledge, a templating
system using ``mustache`` is available. ``mustache`` templates are
provided to render both `ReSTructured Text` or `markdown` formats. If
you know ``mustache`` templating, then you could easily add or modify
these existing templates.

A ``mako`` templating engine is also provided. You'll find also a ``mako``
template producing the same `ReSTructured Text` output than the legacy one.
It's provided for reference and/or further tweak if you would rather use `mako`_
templates.


Mustache
~~~~~~~~

The ``mustache``  output engine uses `mustache templates`_.

The `mustache`_ templates are powered via `pystache`_ the python
implementation of the `mustache`_ specifications. So `mustache`_ output engine
will only be available if you have `pystache`_ module available in your python
environment.

There are `mustache templates`_ bundled with the default installation
of gitchangelog. These can be called by providing a simple label to the
``mustache(..)`` output_engine, for instance (in your ``.gitchangelog.rc``)::

    output_engine = mustache("markdown")

Or you could provide your own mustache template by specifying an
absolute path (or a relative one, starting from the git toplevel of
your project by default, or if set, the
``git config gitchangelog.template-path``
location) to your template file, for instance::

    output_engine = mustache(".gitchangelog.tpl")

And feel free to copy the bundled templates to use them as bases for
your own variations. In the source code, these are located in
``src/gitchangelog/templates/mustache`` directory, once installed they
are in ``templates/mustache`` directory starting from where your
``gitchangelog.py`` was installed.


.. _mustache: http://mustache.github.io
.. _pystache: https://pypi.python.org/pypi/pystache
.. _mustache templates: http://mustache.github.io/mustache.5.html


Mako
~~~~

The ``makotemplate`` output engine templates for ``gitchangelog`` are
powered via `mako`_ python templating system. So `mako`_ output engine
will only be available if you have `mako`_ module available in your
python environment.

There are `mako`_ templates bundled with the default installation
of gitchangelog. These can be called by providing a simple label to the
``makotemplate(..)`` output_engine, for instance (in your ``.gitchangelog.rc``)::

    output_engine = makotemplate("markdown")

Or you could provide your own mustache template by specifying an
absolute path (or a relative one, starting from the git toplevel of
your project by default, or if set, the
``git config gitchangelog.template-path``
location) to your template file, for instance::

    output_engine = makotemplate(".gitchangelog.tpl")

And feel free to copy the bundled templates to use them as bases for
your own variations. In the source code, these are located in
``src/gitchangelog/templates/mako`` directory, once installed they
are in ``templates/mako`` directory starting from where your
``gitchangelog.py`` was installed.

.. _mako: http://www.makotemplates.org


Changelog data tree
~~~~~~~~~~~~~~~~~~~

This is a sample of the current data structure sent to output engines::

  {'title': 'Changelog',
   'versions': [{'label': '%%version%% (unreleased)',
                 'date': None,
                 'tag': None
                 'sections': [{'label': 'Changes',
                               'commits': [{'author': 'John doe',
                                            'body': '',
                                            'subject': 'Adding some extra values.'},
                                           {'author': 'John Doe',
                                            'body': '',
                                            'subject': 'Some more changes'}]},
                              {'label': 'Other',
                               'commits': [{'author': 'Jim Foo',
                                            'body': '',
                                            'subject': 'classic modification'},
                                           {'author': 'Jane Done',
                                            'body': '',
                                            'subject': 'Adding some stuff to do.'}]}]},
                {'label': 'v0.2.5 (2013-08-06)',
                 'date': '2013-08-06',
                 'tag': 'v0.2.5'
                 'sections': [{'commits': [{'author': 'John Doe',
                                            'body': '',
                                            'subject': 'Updating Changelog installation.'}],
                               'label': 'Changes'}]}]}


Merged branches history support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Commit attribution to a specific version could be tricky. Suppose you have
this typical merge tree (spot the tags!)::

    * new: something  (HEAD, tag: 0.2, develop)
    *   Merge tag '0.1.1' into develop
    |\
    | * fix: out-of-band hotfix  (tag: 0.1.1)
    * | chg: continued development
    |/
    * fix: something  (tag: 0.1)
    * first commit  (tag: 0.0.1, master)

Here's a minimal draft of gitchangelog to show how commit are
attributed to versions::

    0.2
      * new: something.
      * Merge tag '0.1.1' into develop.
      * chg: continued development.

    0.1.1
      * fix: out-of-band hotfix.

    0.1
      * fix: something.


.. note:: you can remove automatically all merge commit from
  gitchangelog output by using ``include_merge = False`` in the
  ``.gitchangelog.rc`` file.


Use cases
=========


No sectionning
--------------

If you want to remove sectionning but keep anything else, you should
probably use::

    section_regexps = [
        ('', None)
    ]

    subject_process = (strip | ucfirst | final_dot)

This will disable sectionning and won't remove the prefixes
used for sectionning from the commit's summary.


Incremental changelog
---------------------

Also known as partial changelog generation, this feature allows to
generate only a subpart of your changelog, and combined with
configurable publishing actions, you can insert the result inside
an existing changelog. Usually this makes sense:

- When wanting to switch to ``gitchangelog``, or change your
  conventions:

  - part of your history is not following conventions.
  - you have a previous CHANGELOG you want to blend in.

- You'd rather commit changes to your changelog file for each release:

  - For performance reason, you can then generate changelog only for
    the new commit and save the result.
  - Because you want to be able to edit it to make some minor
    edition if needed.


Generating partial changelog is as simple as ``gitchangelog
REVLIST``. Examples follows::

    ## will output only tags between 0.0.2 (excluded) and 0.0.3 (included)
    gitchangelog 0.0.2..0.0.3

    ## will output only tags since 0.0.3 (excluded)
    gitchangelog ^0.0.3 HEAD

    ## will output all tags up to 0.0.3 (included)
    gitchangelog 0.0.3


Additionally, ``gitchangelog`` can figure out automatically which
revision is the last for you (with some little help). This is done by
specifying the ``revs`` config option. This config file option will be
used as if specified on the command line.

Here is an example that fits the current changelog format::

    revs = [
        Caret(
            FileFirstRegexMatch(
    	        "CHANGELOG.rst",
    	        r"(?P<rev>[0-9]+\.[0-9]+(\.[0-9]+))\s+\([0-9]+-[0-9]{2}-[0-9]{2}\)\n--+\n")),
    ]

This will look into the file ``CHANGELOG.rst`` for the first match of
the given regex and return the match of the ``rev`` regex sub-pattern
it as a string. The ``Caret`` function will simply prefix the given
string with a ``^``. As a consequence, this code will prevent
recreating any previously generated changelog section (more information
about the `REVLIST syntax`_ from ``git rev-list`` arguments.)

.. _REVLIST syntax: https://git-scm.com/docs/git-rev-list#_description

Note that the data structure provided to the template will set the
``title`` to ``None`` if you provided no REVLIST through command-line
or the config file (or if the revlist was equivalently set to
``["HEAD", ]``).  This a good way to make your template detect it is
in "incremental mode".

By default, this will only output to standard output the new sections
of your changelog, you might want to insert it directly in your existing
changelog. This is where ``publish`` parameters will help you. By default
it is set to ``stdout``, and you might want to set it to::

    publish = FileInsertIntoFirstRegexMatch(
        "CHANGELOG.rst",
        r'/(?P<rev>[0-9]+\.[0-9]+(\.[0-9]+)?)\s+\([0-9]+-[0-9]{2}-[0-9]{2}\)\n--+\n/',
        idx=lambda m: m.start(1)
    )

The full recipe could be::

    OUTPUT_FILE = "CHANGELOG.rst"
    INSERT_POINT = r"\b(?P<rev>[0-9]+\.[0-9]+)\s+\([0-9]+-[0-9]{2}-[0-9]{2}\)\n--+\n"
    revs = [
            Caret(FileFirstRegexMatch(OUTPUT_FILE, INSERT_POINT)),
            "HEAD"
    ]

    action = FileInsertAtFirstRegexMatch(
        OUTPUT_FILE, INSERT_POINT,
        idx=lambda m: m.start(1)
    )


Alternatively, you can use this other recipe, using ``FileRegexSubst``, that has
the added advantage of being able to update the unreleased part if you had it already
generated and need a re-fresh because you added new commits or amended some commits::

    OUTPUT_FILE = "CHANGELOG.rst"
    INSERT_POINT_REGEX = r'''(?isxu)
    ^
    (
      \s*Changelog\s*(\n|\r\n|\r)        ## ``Changelog`` line
      ==+\s*(\n|\r\n|\r){2}              ## ``=========`` rest underline
    )

    (                     ## Match all between changelog and release rev
        (
          (?!
             (?<=(\n|\r))                ## look back for newline
             %(rev)s                     ## revision
             \s+
             \([0-9]+-[0-9]{2}-[0-9]{2}\)(\n|\r\n|\r)   ## date
               --+(\n|\r\n|\r)                          ## ``---`` underline
          )
          .
        )*
    )

    (?P<rev>%(rev)s)
    ''' % {'rev': r"[0-9]+\.[0-9]+(\.[0-9]+)?"}

    revs = [
        Caret(FileFirstRegexMatch(OUTPUT_FILE, INSERT_POINT_REGEX)),
        "HEAD"
    ]

    publish = FileRegexSubst(OUTPUT_FILE, INSERT_POINT_REGEX, r"\1\o\g<rev>")


As a second example, here is the same recipe for mustache markdown format::

    OUTPUT_FILE = "CHANGELOG.rst"
    INSERT_POINT_REGEX = r'''(?isxu)
    ^
    (
      \s*\#\s+Changelog\s*(\n|\r\n|\r)        ## ``Changelog`` line
    )

    (                     ## Match all between changelog and release rev
        (
          (?!
             (?<=(\n|\r))                ## look back for newline
             \#\#\s+%(rev)s                     ## revision
             \s+
             \([0-9]+-[0-9]{2}-[0-9]{2}\)(\n|\r\n|\r)   ## date
          )
          .
        )*
    )

    (?P<tail>\#\#\s+(?P<rev>%(rev)s))
    ''' % {'rev': r"[0-9]+\.[0-9]+(\.[0-9]+)?"}

    revs = [
        Caret(FileFirstRegexMatch(OUTPUT_FILE, INSERT_POINT_REGEX)),
        "HEAD"
    ]

    publish = FileRegexSubst(OUTPUT_FILE, INSERT_POINT_REGEX, r"\1\o\n\g<tail>")


Contributing
============

Any suggestion or issue is welcome. Push request are very welcome,
please check out the guidelines.


Push Request Guidelines
-----------------------

You can send any code. I'll look at it and will integrate it myself in
the code base while leaving you as the commit(s) author. This process
can take time and it'll take less time if you follow the following
guidelines:

- check your code with PEP8 or pylint. Try to stick to 80 columns wide.
- separate your commits per smallest concern
- each functionality/bugfix commit should contain the code, tests,
  and doc.
- each commit should pass the tests (to allow easy bisect)
- prior minor commit with typographic or code cosmetic changes are
  very welcome. These should be tagged in their commit summary with
  ``!minor``.
- the commit message should follow gitchangelog rules (check the git
  log to get examples)
- if the commit fixes an issue or finished the implementation of a
  feature, please mention it in the summary.

If you have some questions about guidelines which is not answered here,
please check the current ``git log``, you might find previous commit that
would show you how to deal with your issue. Otherwise, just send your PR
and ask your question. I won't bite. Promise.


License
=======

Copyright (c) 2012-2018 Valentin Lab.

Licensed under the `BSD License`_.

.. _BSD License: http://raw.github.com/vaab/gitchangelog/master/LICENSE
