========
Deckhand
========

|Docker Repository on Quay| |Doc Status|

Deckhand provides document revision management, storage and mutation
functionality upon which the rest of the `Airship`_ components rely for
orchestration of infrastructure provisioning. Deckhand understands declarative
YAML documents that define, end-to-end, the configuration of sites: from the
hardware -- encompassing network topology and hardware and host profile
information -- up to the software level that comprises the overcloud.

* Free software: Apache license
* Documentation: https://airship-deckhand.readthedocs.io/en/latest/
* Source: https://git.openstack.org/cgit/openstack/airship-deckhand
* Bugs: https://storyboard.openstack.org/#!/project/1004
* Release notes: https://airship-deckhand.readthedocs.io/en/latest/releasenotes/index.html

Core Responsibilities
=====================

* layering - helps reduce duplication in configuration by applying the notion
  of inheritance to documents
* substitution - provides separation between secret data and other
  configuration data for security purposes and reduces data duplication by
  allowing common data to be defined once and substituted elsewhere dynamically
* revision history - maintains well-defined collections of documents within
  immutable revisions that are meant to operate together, while providing the
  ability to rollback to previous revisions
* validation - allows services to implement and register different kinds of
  validations and report errors
* secret management - leverages existing OpenStack APIs -- namely
  `Barbican`_ -- to reliably and securely store sensitive data

.. _Barbican: https://docs.openstack.org/barbican/latest/api/

Getting Started
===============

For more detailed installation and setup information, please refer to the
`Getting Started <https://airship-deckhand.readthedocs.io/en/latest/getting-started.html>`_
guide.

Integration Points
==================

Deckhand has the following integration points:

  * `Barbican (OpenStack Key Manager) <https://github.com/openstack/barbican>`_
    provides secure storage for sensitive data.
  * `Keystone (OpenStack Identity service) <https://github.com/openstack/keystone>`_
    provides authentication and support for role based authorization.
  * `PostgreSQL <https://www.postgresql.org>`_ is used to persist information
    to correlate workflows with users and history of workflow commands.

  .. note::

    Currently, other database back-ends are not supported.

Though, being a low-level service, has many other Airship services that integrate
with it, including:

  * `Drydock <https://github.com/openstack/airship-drydock>`_ is orchestrated by
    Shipyard to perform bare metal node provisioning.
  * `Promenade <https://github.com/openstack/airship-promenade>`_ is indirectly
    orchestrated by Shipyard to configure and join Kubernetes nodes.
  * `Armada <https://github.com/openstack/airship-armada>`_ is orchestrated by
    Shipyard to deploy and test Kubernetes workloads.

Further Reading
===============

`Airship`_.

.. _Airship: https://www.airshipit.org

.. |Docker Repository on Quay| image:: https://quay.io/repository/airshipit/deckhand/status
   :target: https://quay.io/repository/airshipit/deckhand
.. |Doc Status| image:: https://readthedocs.org/projects/airship-deckhand/badge/?version=latest
   :target: https://airship-deckhand.readthedocs.io/
