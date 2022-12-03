HBMQTT
======

``HBMQTT`` is an open source `MQTT`_ client and broker implementation.

Built on top of `asyncio`_, Python's standard asynchronous I/O framework, HBMQTT provides a straightforward API
based on coroutines, making it easy to write highly concurrent applications.

.. _asyncio: https://docs.python.org/3/library/asyncio.html

No Longer Maintained
--------------------

**HBMQTT is no longer maintained**. There is a fork `aqmtt`_ under active development by different people. `See here for some background`_.

.. _aqmtt: https://github.com/Yakifo/amqtt
.. _See here for some background: https://github.com/beerfactory/hbmqtt/issues/235

Features
--------

HBMQTT implements the full set of `MQTT 3.1.1`_ protocol specifications and provides the following features:

- Support QoS 0, QoS 1 and QoS 2 messages flow
- Client auto-reconnection on network lost
- Authentication through password file (more methods can be added through a plugin system)
- Basic ``$SYS`` topics
- TCP and websocket support
- SSL support over TCP and websocket
- Plugin system

Build status
------------

.. image:: https://travis-ci.org/beerfactory/hbmqtt.svg?branch=master
    :target: https://travis-ci.org/beerfactory/hbmqtt

.. image:: https://coveralls.io/repos/beerfactory/hbmqtt/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/beerfactory/hbmqtt?branch=master

Project status
--------------

.. image:: https://readthedocs.org/projects/hbmqtt/badge/?version=latest
    :target: http://hbmqtt.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://badge.fury.io/py/hbmqtt.svg
    :target: https://badge.fury.io/py/hbmqtt

Getting started
---------------

hbmqtt is available on `Pypi <https://pypi.python.org/pypi/hbmqtt>`_ and can installed simply using ``pip`` :
::

    $ pip install hbmqtt

Documentation is available on `Read the Docs`_.

Bug reports, patches and suggestions welcome! Just `open an issue`_ or join the `gitter channel`_.

.. image:: https://badges.gitter.im/Join%20Chat.svg
    :target: https://gitter.im/beerfactory/hbmqtt?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
    :alt: 'Join the chat at https://gitter.im/beerfactory/hbmqtt'

.. _MQTT: http://www.mqtt.org
.. _MQTT 3.1.1: http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html
.. _Read the Docs: http://hbmqtt.readthedocs.org/
.. _open an issue: https://github.com/beerfactory/hbmqtt/issues/new
.. _gitter channel: https://gitter.im/beerfactory/hbmqtt
