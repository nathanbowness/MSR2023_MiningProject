asyncactor
==========

AsyncActor is an async Python module that aids in service discovery and
"somewhat-leader" election in a heterogenous, sometimes-disconnected
network.

AsyncActor can run on top of any reliable broadcast channel.
This version includes back-ends for Serf and MQTT.

AsyncActor sends as few packets as possible, thus is well-suited for
IoT-related applications with many stations but limited bandwidth.

Theory of operation
+++++++++++++++++++

Assume that you have a non-lossy network with a bounded latency (let's
assume one second). Assume further that you'd like to know within ten
seconds whether your node is still online.

AsyncActor sends one beacon message every seven to nine seconds. The message
includes a list of N previous hosts that have transmitted the beacon; the
host that's last in this list will be the next transmitter.

The time slot starting at the seven-second mark is used for random hosts
which would like to enter the beacon sending business. This is somewhat
likely if the list of hosts is currently smaller than N. The slot at eight
seconds is used for the hosts at the end of the list; the last host will
send first, but if its beacon is not seen then the next-to-last will send
its message, and so on.

The time slot at nine seconds is used for last-resort messages, i.e. any
participating host can and will send its beacon message.

Collisions are resolved at the ten-second mark, i.e. the list of messages
is ordered deterministically: the winner will announce to its clients that
a new slot has started and whether all N host slots are filled.

It uses `anyio <https://github.com/agronholm/anyio>` as its underlying
async framework.

.. image:: https://badge.fury.io/py/asyncactor.svg
    :alt: PyPI latest version badge
    :target: https://pypi.python.org/pypi/asyncactor
.. image:: https://coveralls.io/repos/smurfix/asyncactor/badge.png?branch=master
    :alt: Code coverage badge
    :target: https://coveralls.io/r/smurfix/asyncactor?branch=master

Installation
------------

AsyncActor requires a back-end, i.e. either a running Serf agent or a MQTT
broker.

To install AsyncActor, run the following command:

.. code-block:: bash

    $ pip install asyncactor

or alternatively (you really should be using pip though):

.. code-block:: bash

    $ easy_install asyncactor

or from source:

.. code-block:: bash

    $ python setup.py install

Getting Started
---------------

These examples require a running async loop.
`Trio <https://github.com/python-trio/trio>` is recommended, though
``asyncio`` works too.

.. code-block:: python

    from asyncactor import client as actor
    from somewhere import some_transport

    async with some_transport.connect('localhost') as t:
        async with actor(t, prefix=('actor','test')) as client:
            async for client.events as m:
                print(m)

Development
------------

You can run the tests using the following commands:

.. code-block:: bash

    $ serf agent & # start serf agent
    $ mosquitto 
    $ python3 -mpytest tests

