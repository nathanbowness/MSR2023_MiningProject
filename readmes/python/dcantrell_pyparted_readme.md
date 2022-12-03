# pyparted

## Python bindings for libparted

---

### Overview

pyparted is a set of native Python bindings for libparted.  libparted
is the library portion of the GNU parted project.  With pyparted, you
can write applications that interact with disk partition tables and
filesystems.

The Python bindings are implemented in two layers.  Since libparted
itself is written in C without any real implementation of objects, a
simple 1:1 mapping of externally accessible libparted functions was
written.  This mapping is provided in the _ped Python module.  You can
use that module if you want to, but it's really just meant for the
larger parted module.

| Module | Description |
| :--- | :--- |
| _ped | libparted Python bindings, direct 1:1: function mapping |
| parted | Native Python code building on _ped, complete with classes, exceptions, and advanced functionality. |

The _ped module is written and maintained by hand.  I chose to do this
rather than rely on a tool like SWIG or Pyrex for several reasons.
Mostly because I was the GNU parted maintainer, but also because
libparted is sort of complex.  It's a lowlevel system tool and I found
it doesn't translate well in the tools I tried.  This is nothing
against those tools, I just don't think libparted is ideal to go
through SWIG or Pyrex.  By writing my own bindings, I can also find
bugs in libparted that I may have overlooked before.  See the WHY file
for more explanation as to why I wrote the bindings by hand.

### History

pyparted started life at Red Hat and continues there today.  The main
reason for writing it was to let anaconda (the Red Hat installation
program, now used by RHEL and Fedora and many other distributions)
interact with libparted.  Anaconda is written in Python, so native
bindings made sense.

pyparted went through many rewrites, but the end result was always the
same.  And incomplete API via Python with just enough provided for
anaconda to do its job.

The latest iteration of pyparted aims to be a complete API mapping and
even provide a nice set of classes so that people might want to
integrate it in to other installers or even write other applications
(maybe a Python based alternative to parted(8) or fdisk(8)).

### Examples

Example code is provided in the examples directory.  These may help
provide a gentle introduction to the usage concepts of pyparted.  More
examples are always welcome, as are improved explanatory commentary
for those that exist.

### Questions

If you are reporting a pyparted failure in Fedora, it's most useful if
you file a bug at http://bugzilla.redhat.com/ against the appropriate
Fedora release you are using.

Alternatively, you can file bugs directly on the project page:
https://github.com/dcantrell/pyparted/issues

If you just have questions about pyparted, you can email us directly
using the contact information in the AUTHORS file.  We will do our
best to help you.
