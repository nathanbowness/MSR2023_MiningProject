Jumble
======

An Android service implementation of the Mumble protocol, designed as the backend of [Plumble](https://www.github.com/acomminos/Plumble).

About
-----

The primary goal of the Jumble project is to encourage developers to embrace the Mumble protocol on Android through a free, complete, and stable implementation. At the moment, development is focused on improving stability and security.

Prior to the release of Jumble, all implementations of the Mumble protocol on Android have been using the same non-free code developed by @pcgod. To ensure the unencumbered use of Jumble, no sources or derivatives will be copied from that project.

Projects using Jumble
---------------------

[Plumble 3.0+](https://www.github.com/acomminos/Plumble)

Including in your project
-------------------------

Jumble is a standard Android library project using the gradle build system. [See here for instructions on how to include it into your gradle project](http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Referencing-a-Library).

Currently, there is no tutorial to integrate Jumble with your project. In the mean time, please examine the exposed interface IJumbleService as well as Plumble's implementation.

License
-------

Jumble is now licensed under the GNU GPL v3+. See LICENSE.

If you wish to incorporate Jumble into your proprietary project, please email me to discuss licensing.
