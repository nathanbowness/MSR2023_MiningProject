Preliminary note for Windows users
==================================

The build instructions for `gprbuild` may have a slight UNIX flavor but they can
be used on Windows platforms with a full Cygwin installation. The latter makes
it simpler to build `gprbuild` but is not required to use it.

Bootstrapping
=============

`gprbuild` needs `gprbuild` to build... So we also provide a way to
easily bootstrap if you don't already have `gprbuild`, provided you
already have installed GNAT.

Download XML/Ada sources (from https://github.com/AdaCore/xmlada), together
with the gprconfig knowledge base (from
https://github.com/AdaCore/gprconfig_kb).

Run the `bootstrap.sh` script (written for POSIX systems) specifying the
install location and the sources of `XML/Ada` and `gprconfig_kb`. The script
will build *and* install `gprbuild`.

For example, to build `gprbuild` and install it to `./bootstrap` in the current
working directory, run:

    $ ./bootstrap.sh --with-xmlada=../xmlada --with-kb=../gprconfig_kb --prefix=./bootstrap

For maintainers, the environment `DESTDIR` is honoured for staged installs, see
`./bootstrap.sh -h` for more.

With this bootstrapped `gprbuild`, you can build XML/Ada and `gprbuild`
as documented below.

Configuring
===========

You should first configure the build like this (if you plan to build in
the source tree directly, you can omit setting the SOURCE_DIR variable):

    $ make prefix=xxx SOURCE_DIR=/path/to/gprbuild/sources setup

Building and Installing
=======================

XML/Ada must be installed before building.

Building the main executables is done simply with:

    $ make all

When compiling, you can choose whether you want to link statically with XML/Ada
(the default), or dynamically. To compile dynamically, you should run:

    $ make LIBRARY_TYPE=relocatable all

instead of the above.

Installation is done with:

    $ make install

Doc & Examples
==============

The documentation is provided in various formats in the `doc` subdirectory. You
can also find it
[online](http://docs.adacore.com/gprbuild-docs/html/gprbuild_ug.html).

It refers to concrete examples that are to be found in the `examples`
subdirectory. Each example can be built easily using the simple attached
Makefile:

    $ make all    # build the example
    $ make run    # run the executable(s)
    $ make clean  # cleanup

All the examples can be `built/run/cleaned` using the same targets and the top
level examples Makefile.
