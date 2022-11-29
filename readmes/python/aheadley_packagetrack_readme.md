==================================================================================
packagetrack - Track packages
==================================================================================

:Authors:
    Scott Torborg (storborg)
    Michael Stella (alertedsnake)
    Alex Headley (aheadley)

:Version: 0.4

This library tracks packages.

*Note* Use at your own risk!

Requirements
============
setuptools, suds, pytz, pip, fedex module

For debian or ubuntu, do::
    $ apt-get install python-setuptools python-suds python-tz python-pip
    $ pip install fedex

Installation
============

Simple as::

    $ easy_install packagetrack

Or if you prefer, download the source and then::

    $ python setup.py build
    $ python setup.py install

Example
=======

>>> from packagetrack import Package
>>> package = Package('1Z9999999999999999')
# Identify packages (UPS, FedEx, DHL, CanadaPost, and USPS)
>>> package.carrier
'UPS'
>>> info = package.track()
>>> print info.status
IN TRANSIT TO
>>> print info.delivery_date
2010-06-25 00:00:00
>>> print info.last_update
2010-06-19 00:54:00
# Get tracking URLs
>>> print package.url
http://wwwapps.ups.com/WebTracking/processInputRequest?TypeOfInquiryNumber=T&InquiryNumber1=1Z9999999999999999


API Configuration
=====================

To enable package tracking (not just finding URLs or matching TNs to carriers),
you will need to get API credentials for most of the carriers you wish to use.
The default configuration method is to read the config values from
~/.packagetrack, which looks like this::

    [UPS]
    license_number = XXXXXXXXXXXXXXXX
    user_id = XXXX
    password = XXXX

    [FedEx]
    key = XXXXXXXXXXXXXXXX
    password = XXXXXXXXXXXXXXXXXXXXXXXXX
    account_number = #########
    meter_number = #########

    [USPS]
    userid = XXXXXXXXXXXX
    password = XXXXXXXXXXXX

    [CanadaPost]
    username = XXXXXXXXXXXXXXXX
    password = XXXXXXXXXXXXXXXXXXXXXX

You can specify an alternate location for the config file like so::

    >>> from packagetrack.configuration import DotFileConfig
    >>> cfg = DotFileConfig('/path/to/file')
    >>> packagetrack.auto_register_carriers(cfg)

Alternatively, you can provide a different type of config like the
DictConfig or making another type (like one that pulls values from a database).


License
=======

Packagetrack is released under the GNU General Public License (GPL). See the
LICENSE file for full text of the license.


.. # vim: syntax=rst expandtab tabstop=4 shiftwidth=4 shiftround
