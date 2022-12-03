# teslajson
Simple Python class to access the Tesla JSON API.

Written by Greg Glockner

## Description
This is a simple Python interface to the [Tesla JSON
API](https://tesla-api.timdorr.com). With this, you can query your
vehicle, control charge settings, turn on the air conditioning, and
more.  You can also embed this into other programs to automate these
controls.

The class is designed to be simple.  You initialize a _Connection_
object, retrieve the list of _Vehicle_ objects, then perform get/set
methods on a _Vehicle_.  There is a single get method
[_Vehicle.data\_request()_] and a single set method [_Vehicle.command()_] so
that the class does not require changes when there are minor updates
to the underlying JSON API.

This has been tested with Python 3.7 and requires the
[Requests-OAuthlib](https://requests-oauthlib.readthedocs.io) library.

## Installation

Use any of these methods to download and install the teslajson module:

1. Easiest method: use pip via the command :`pip install teslajson`
2. Download the source code from https://github.com/gglockner/teslajson, then run: `python setup.py install`
3. Download the source code, install requests-oauthlib and its dependencies, then add the file teslajson/teslajson.py to your Python project

## Public API
`Connection(email, password, **kwargs)`:
Initialize the connection to the Tesla Motors website.

Required parameters:

- _email_: your login for teslamotors.com
- _password_: your password for teslamotors.com

Optional parameters:
- _mfa_: your multi-factor authentication code, if enabled on your account
- _mfa\_id_: if you have multiple MFA devices, the UUID for the MFA device you want to use
- _\*\*kwargs_: arguments passed to the Requests objects


`Connection.vehicles`: A list of Vehicle objects, corresponding to the
vehicles associated with your account on teslamotors.com.

`Vehicle`: The vehicle class is a subclass of a Python dictionary
(_dict_).  A _Vehicle_ object contains fields that identify your
vehicle, such as the Vehicle Identification Number (_Vehicle['vin']_). 
All standard dictionary methods are supported.

`Vehicle.wake_up()`: Wake the vehicle.

`Vehicle.data_request(name)`: Retrieve data values specified by _name_, such
as _charge\_state_, _climate\_state_, _vehicle\_state_. Returns a
dictionary (_dict_).  For a full list of _name_ values, see the _GET_
commands in the [Tesla JSON API](https://tesla-api.timdorr.com).

`Vehicle.command(name)`: Execute the command specified by _name_, such
as _charge\_port\_door\_open_, _charge\_max\_range_. Returns a
dictionary (_dict_).  For a full list of _name_ values, see the _POST_ commands
in the [Tesla JSON API](https://tesla-api.timdorr.com/).

## Example
	import teslajson
	c = teslajson.Connection('youremail', 'yourpassword')
	v = c.vehicles[0]
	v.wake_up()
	v.data_request('charge_state')
	v.command('charge_start')

## Credits
Many thanks to [Tim Dorr](http://timdorr.com) for documenting the Tesla JSON API.
This would not be possible without his work.

## Disclaimer
This software is provided as-is. This software is not supported by or
endorsed by Tesla. It was developed via reverse-engineering of an
unpublished JSON API. Tesla does not publicly support the underlying
JSON API, so this software may stop working at any time. The author
makes no guarantee to release an updated version to fix any
incompatibilities.
