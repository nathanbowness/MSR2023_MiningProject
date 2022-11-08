# Python library for ZFM fingerprint sensors

[![Documentation Status](https://readthedocs.org/projects/pyfingerprint/badge/?version=latest)](https://pyfingerprint.readthedocs.io/en/latest/?badge=latest)

The PyFingerprint library allows to use ZhianTec ZFM-20, ZFM-60, ZFM-70 and ZFM-100 fingerprint sensors on the Raspberry Pi or other Linux machines. Some other models like R302, R303, R305, R306, R307, R551 and FPM10A also work.

**Note:** The library is inspired by the C++ library from Adafruit Industries:
<https://github.com/adafruit/Adafruit-Fingerprint-Sensor-Library>

## Installation

There are two ways of installing PyFingerprint: Installation of the **stable** or **development** version. The stable version is distributed through the PM Code Works APT repository and is fully tested but does not contain the latest changes.

### Installation of the stable version

Add PM Code Works repository:

* Debian 9/Ubuntu 16 & 17:

    `echo "deb http://apt.pm-codeworks.de stretch main" | sudo tee /etc/apt/sources.list.d/pm-codeworks.list`

* Debian 10/Ubuntu 18 & 19:

    `echo "deb http://apt.pm-codeworks.de buster main" | sudo tee /etc/apt/sources.list.d/pm-codeworks.list`

Add PM Code Works signing key:

    wget -qO - http://apt.pm-codeworks.de/pm-codeworks.de.gpg | sudo apt-key add -
    sudo apt update

Install the package:

    sudo apt install python3-fingerprint

### Installation of the development version

The development version contains the latest changes that may not have been fully tested and should therefore not be used in production. It is recommended to install the stable version.

Install required packages for building:

    sudo apt install git devscripts equivs

Clone this repository:

    git clone https://github.com/bastianraschke/pyfingerprint.git

Build the package:

    cd ./pyfingerprint/src/
    sudo mk-build-deps -i debian/control
    dpkg-buildpackage -uc -us

The library supports Python 2 and Python 3. There are one Debian package for each. It's up to you which version you install.

For Python 3 use:

    sudo dpkg -i ../python3-fingerprint*.deb

For Python 2 use:

    sudo dpkg -i ../python-fingerprint*.deb

Install missing dependencies:

    sudo apt -f install

### Alternative installation using PIP

If you do not have a Debian based OS or something does not work you can also install the Python package via [PIP](https://pypi.org/project/pyfingerprint):

    pip install pyfingerprint

**NOTE**: It is important to not use the Debian package and PIP package at the same time!

## Setup

Allow non-root user "pi" (replace it correctly) to use the serial port devices:

    sudo usermod -a -G dialout pi
    sudo reboot

## How to use the library

### Enroll a new finger

    python /usr/share/doc/python-fingerprint/examples/example_enroll.py

### Search an enrolled finger

    python /usr/share/doc/python-fingerprint/examples/example_search.py

### Delete an enrolled finger

    python /usr/share/doc/python-fingerprint/examples/example_delete.py

### Download image of a scanned finger

    python /usr/share/doc/python-fingerprint/examples/example_downloadimage.py

### Generate a 32-bit random number on the ZFM hardware PRNG

    python /usr/share/doc/python-fingerprint/examples/example_generaterandom.py

## Further information

See my blog post for more information:

<https://sicherheitskritisch.de/2015/03/fingerprint-sensor-fuer-den-raspberry-pi-und-debian-linux-en/>
