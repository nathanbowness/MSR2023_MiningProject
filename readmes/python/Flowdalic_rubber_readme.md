This is Rubber.

Rubber is a building system for LaTeX documents. It is based on a routine that
runs just as many compilations as necessary and runs companion programs like
BibTeX and Makeindex when needed. The module system provides a great
flexibility that virtually allows support for any package with no user
intervention, as well as pre- and post-processing of the document. A good
number of standard packages are supported, including graphics/graphicx with
automatic conversion between various graphics formats and Metapost
compilation. The associated tool "rubber-info" extracts information, such as
dependency relations or post-compilation diagnostics.


* Installation

Running Rubber just requires Python 3.5.  Of course it won't
be of much use without a working LaTeX environment (Rubber is known to work on
TeXLive and VTeX on various flavors of Unix including Darwin and Cygwin, any
feedback is welcome about other systems).

For compilation, you will need the Python Distutils, which are usually included
in development packages (in Debian, this is the python3-dev package).  To build
the documentation, you need texinfo (Debian package: texinfo).

To compile and install Rubber, just follow the usual procedure:

# python3 setup.py --help
# python3 setup.py install
# python3 setup.py clean --all


Some useful options to setup.py include:

Disabling info docs:

# python3 setup.py build --info=False install

and similar for --html, --man, --pdf.

Changing the installation path for manpages:

# python3 setup.py install --mandir=/path/to/man/pages

Installing to a staging directory instead of the root/prefix:

# python3 setup.py install --root=/staging/directory

Note that if you need build and install to be two different steps
(for example when building packages for distribution purposes),
Python's distutils will forget about any 'build' options, and re-build
with default options during the 'install' stage.  This is worrysome if
you'd like not to build some of the documentation.  It is then best
to make options permanent by putting them info a setup.cfg file.  For
example:

[build]
man = 1
html = 0
pdf = 0
info = 0
txt = 0
[install]
prefix  = /usr

Finally, invoke

# python3 setup.py build
# python3 setup.py install --root=/staging/directory


* Usage

As civility requires, saying `rubber --help' and `rubber-info --help' provides
a short description of the command line's syntax. The included manual pages
(available in English and French) and Texinfo documentation contain more
precise usage information.


* Known Bugs

Rubber is generally working fine, though there are some known issues.

1) Rubber tries to do too much.  Rubber attempts to provide a one-stop solution
to compiling a TeX document, and run a lot of related software as needed.

This approach is fragile for three reasons: a) It does so by parsing the .tex
file itself, and all included files, and discovering any related input files.
TeX is a hard language to parse correctly without embedding a full TeX
interpreter, which rubber does not do.  b) To do its work, Rubber needs to be
taught about every version of every package in the TeX ecosystem in order to
gauge its impact on the compilation of a TeX document.  It needs to know the
preferences of any TeX compiler with regards to image formats, search paths
etc.  All this information is hard to keep up to date.  c) In some cases (like
image conversion), it needs to outright guess what the user intends to do, and
may in fact guess incorrectly.

In a future release, some of these features may be taken out in favor of more
modern ways to accomplish the same thing, with to goal to render Rubber simpler
and more robust.  One might want to make use of the -recorder feature (.fls)
for example instead of attempting to read the same information from the
human-readable log file.

2) The codebase has been cleaned up considerably, has been converted to Python3
and is generally in a sane state.  Nevertheless, it has been written over a
number of years, and some features would be implemented differently or skipped
altogether if a rewrite were attempted (e.g. the onchange mechanism, modules,
...).

3) In some cases, Rubber will trigger a recompile that is arguably unnecessary.
Rubber tries to err on the side of caution here.


* Author

Rubber was originally written by Emmanuel Beffara <emmanuel@beffara.org>.
It is currently maintained by Sebastian Kapfer <sebastian.kapfer@fau.de>
and Nicolas Boulenguez <nicolas@debian.org>.

Its homepage can be found at https://launchpad.net/rubber.

Thanks to all those who provided testing, comments and suggestions, and
re-thanks to those who wrote patches and bugfixes.

Any kind of feedback is appreciated, in order to make this program as useful
and robust as possible.
