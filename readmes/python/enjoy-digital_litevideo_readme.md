```
                          __   _ __     _   ___    __
                         / /  (_) /____| | / (_)__/ /__ ___
                        / /__/ / __/ -_) |/ / / _  / -_) _ \
                       /____/_/\__/\__/|___/_/\_,_/\__/\___/

                         Copyright 2016-2020 / EnjoyDigital
                         Copyright 2016-2020 / TimVideos.us

                     Small footprint and configurable video cores
                                powered by LiteX
```

[![](https://travis-ci.com/enjoy-digital/litevideo.svg?branch=master)](https://travis-ci.com/enjoy-digital/litevideo) ![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)


[> Intro
--------
LiteVideo provides small footprint and configurable video cores.

LiteVideo is part of LiteX libraries whose aims are to lower entry level of
complex FPGA cores by providing simple, elegant and efficient implementations
of components used in today's SoC such as Ethernet, SATA, PCIe, SDRAM Controller...

Using Migen to describe the HDL allows the core to be highly and easily configurable.

LiteVideo can be used as LiteX library or can be integrated with your standard
design flow by generating the verilog rtl that you will use as a standard core.

[> Features
-----------
PHY:
  - HDMI input (Spartan6, 7-Series)
  - HDMI output (Spartan6, 7-Series)

Core:
  - DMA (input/output)
  - Triple buffering (output)
  - Color space conversion (RGB <--> YCbCr)
  - Chroma resampling
  - Floating point arithmetic (WIP)

[> FPGA Proven
--------------
LiteVideo is already used in commercial and open-source designs:
- HDMI2USB: http://hdmi2usb.tv/home/
- and others commercial designs...

[> Possible improvements
------------------------
- add standardized interfaces (AXI, Avalon-ST)
- add Display Port support
- add more documentation
- ... See below Support and consulting :)

If you want to support these features, please contact us at florent [AT]
enjoy-digital.fr.

[> Getting started
------------------
1. Install Python 3.6+ and FPGA vendor's development tools.
2. Install Migen/LiteX and the LiteX's cores:

```sh
$ wget https://raw.githubusercontent.com/enjoy-digital/litex/master/litex_setup.py
$ chmod +x litex_setup.py
$ ./litex_setup.py init install --user (--user to install to user directory)
```
  Later, if you need to update all repositories:
```sh
$ ./litex_setup.py update
```

3. TODO: add/describe examples

[> Tests
--------
Unit tests are available in ./test/.
To run all the unit tests:
```sh
$ ./setup.py test
```

Tests can also be run individually:
```sh
$ python3 -m unittest test.test_name
```

[> License
----------
LiteVideo is released under the very permissive two-clause BSD license. Under the
terms of this license, you are authorized to use LiteVideo for closed-source
proprietary designs.
Even though we do not require you to do so, those things are awesome, so please
do them if possible:
 - tell us that you are using LiteVideo
 - cite LiteVideo in publications related to research it has helped
 - send us feedback and suggestions for improvements
 - send us bug reports when something goes wrong
 - send us the modifications and improvements you have done to LiteVideo.

[> Support and consulting
-------------------------
We love open-source hardware and like sharing our designs with others.

LiteVideo is developed and maintained by EnjoyDigital.

If you would like to know more about LiteVideo or if you are already a happy user
and would like to extend it for your needs, EnjoyDigital can provide standard
commercial support as well as consulting services.

So feel free to contact us, we'd love to work with you! (and eventually shorten
the list of the possible improvements :)

[> Contact
----------
E-mail: florent [AT] enjoy-digital.fr
