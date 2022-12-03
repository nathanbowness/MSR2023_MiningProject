SWORD2 python client
--------------------

A python library and client to connect to and use SWORD v2 compliant servers.

SWORD overview

SWORD was originally a JISC-funded initiative to define and develop a standard mechanism for depositing into repositories and other systems. Why was it created? because there was no standard way of doing this. A standard deposit interface to repositories allows more services to be built which can offer functionality such as deposit from multiple locations, e.g. disparate repositories, desktop drag’n'drop tools or from within standard office applications. SWORD can also facilitate deposit to multiple repositories, increasingly important for depositors who wish to deposit to funder, institutional or subject repositories. Other possibilities include migration of content between repositories, transfer to preservation services and many more.

SWORD is an Atom Publishing Profile

Rather than develop a new standard from scratch, SWORD chose to leverage the existing Atom Publishing Protocol (APP), “an application-level protocol for publishing and editing Web resources”. APP is based on the HTTP transfer of Atom-formatted representations yet SWORD has focussed on two key aspects of the protocol – the deposit of files, rather than Atom documents, and the extension mechanism for specifying additional deposit parameters. Also worth noting is that SWORD does not specify the implementation of all of the functionality of APP, rather it supports deposit only – implementations are free to support update and delete if they wish but this is out of the SWORD remit.

Python Client library

Dependencies

The core dependency is httplib2, and uses this for all of its HTTP requests and response handling.

The python client tries to use any suitable ElementTree library implementation (lxml, xml.etree, cElementTree, ElementTree) and will fail without one.

Installation:

```shell
$ pip install .
```

(use of a virtualenv is recommended)

Software links:

Usage documentation: https://github.com/swordapp/python-client-sword2/wiki 

API documentation:   http://packages.python.org/sword2/

Repository:          https://github.com/swordapp/python-client-sword2

Issue-tracker:       https://github.com/swordapp/python-client-sword2/issues
