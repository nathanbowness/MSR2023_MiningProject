Glencoe Software jxrlib
=======================

Decode and encode JPEG-XR data from Java

Requirements
============

* make (Linux / OS X)
* Visual Studio (Windows)
* SWIG 3.0.10 or later
* Maven

Building
========

Linux
-----

```
# $JXRLIB is the path to the clone of this repository
$ export SWIG=`which swig`
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$JXRLIB/build
$ make clean swig all
$ cd build
# run tests on the Java bindings
$ mvn -f ../java/pom.xml test
# package the native library for this platform into a jar
$ mvn -f ../java/native-$PLATFORM/pom.xml package
# package the Java bindings into a jar
$ mvn -f ../java/pom.xml package
# package all native libraries and Java bindings into a single jar
$ mvn -f ../java/all/pom.xml package
```

Build artifacts are in $JXRLIB/build and $JXRLIB/java/all/target/.

Continuous integration
----------------------

Travis is currently used to perform Linux and OS X builds and native library jar deployments.
AppVeyor is used for Windows builds.


History
=======

This project was forked from Microsoft's JPEG-XR library formerly at jxrlib.codeplex.com.
The state prior to forking is tagged as https://github.com/glencoesoftware/jxrlib/tree/codeplex-last-commit
A summary of changes and rationale is here: https://github.com/glencoesoftware/jxrlib/issues/17#issuecomment-401063816
