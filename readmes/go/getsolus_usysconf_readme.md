# usysconf

> Universal system configuration interface

[![Go Report Card](https://goreportcard.com/badge/github.com/getsolus/usysconf)](https://goreportcard.com/report/github.com/getsolus/usysconf) [![license](https://img.shields.io/github/license/getsolus/usysconf.svg)](https://raw.githubusercontent.com/getsolus/usysconf/master/LICENSE)

usysconf is a [Solus project](https://getsol.us/).

![logo](https://build.getsol.us/logo.png)

`usysconf` is a stateless binary to provide a centralised configuration system to replace "package hooks" and post-installation triggers.  It involves using TOML based config files for running other binaries, that allow for the capacity to skip running based on either existing or missing paths.

The binary runs all config files in the directories, or only some of them by passing them as arguments.

This replaces the previous version written in C that hardcoded the handlers, to a version written in Go with TOML based config files.

## Building

Install the dependencies:

- go (>=1.13)

Then compile usysconf:

    $ make

usysconf allows the ability to set the configuration and logging directories at compile time:

    $ make PREFIX=/usr USRDIR=/usr/dir SYSDIR=/etc/dir LOGDIR=/var/log/dir

## Installation

    # make install PREFIX=/usr

## Running

    $ usysconf list
    # usysconf run
    # usysconf run apparmor dconf

## License

Copyright 2019-2020 Solus Project <copyright@getsol.us>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
