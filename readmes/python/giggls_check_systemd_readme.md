[![pypi.org](http://img.shields.io/pypi/v/check_systemd.svg)](https://pypi.python.org/pypi/check_systemd)
[![Build Status](https://travis-ci.org/Josef-Friedrich/check_systemd.svg?branch=master)](https://travis-ci.org/Josef-Friedrich/check_systemd)

# check_systemd

Nagios / Icinga monitoring plugin to check systemd for failed units.

This Python script will report a degraded system to Nagios / Icinga.
It requires only the nagiosplugin library.

You can also test a single service with -s parameter.

Released under GNU GPLv2 License.

## Installation

```
pip3 install check_systemd
```

## Command line interface

```
usage: check_systemd [-h] [-c SECONDS] [-e UNIT | -u UNIT] [-v] [-V] [-w SECONDS]

Copyright (c) 2014-18 Andrea Briganti a.k.a 'Kbyte' <kbytesys@gmail.com>
Copyright (c) 2019-20 Josef Friedrich <josef@friedrich.rocks>

Nagios / Icinga monitoring plugin to check systemd for failed units.

optional arguments:
  -h, --help            show this help message and exit
  -c SECONDS, --critical SECONDS
                        Startup time in seconds to result in critical status.
  -e UNIT, --exclude UNIT
                        Exclude a systemd unit from the checks. This option can be applied multiple times. For
                        example: -e mnt-data.mount -e task.service.
  -u UNIT, --unit UNIT  Name of the systemd unit that is being tested.
  -v, --verbose         Increase output verbosity (use up to 3 times).
  -V, --version         show program's version number and exit
  -w SECONDS, --warning SECONDS
                        Startup time in seconds to result in warning status.

Performance data:
  - count_units
  - startup_time
  - units_activating
  - units_active
  - units_failed
  - units_inactive

```

## Project pages

* https://github.com/Josef-Friedrich/check_systemd
* https://exchange.icinga.com/joseffriedrich/check_systemd
* https://exchange.nagios.org/directory/Plugins/System-Metrics/Processes/check_systemd/details

## Testing

```
pyenv install 3.7.6
pyenv install 3.8.1
pyenv local 3.7.6 3.8.1
pip3 install tox
tox
```

# Deploying

Edit version number in check_systemd.py (without `v`)

```
git tag v2.0.11
git push --tags
```
