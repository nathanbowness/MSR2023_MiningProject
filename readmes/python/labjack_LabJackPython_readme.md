LabJackPython: Cross-platform (Windows, Linux, Mac OS X) Python modules and
examples for the LabJack U3, U6, UE9 and U12.
11/03/2022
support@labjack.com

LabJackPython requires Python 2.7 or 3.x. Please report bugs to
support@labjack.com or on GitHub:

    https://github.com/labjack/LabJackPython

To use Modbus first check that your LabJack device meets the minimum required
firmware version listed on this page:

    https://labjack.com/support/software/api/modbus/ud-modbus

To upgrade firmware look at this page:

    https://labjack.com/support/firmware

To use Modbus on a UE9 over Ethernet, install Comm firmware 1.50 or higher.

To install LabJackPython, run the following command in a terminal (remove "sudo"
on Windows):

    $ sudo python setup.py install

If there are multiple versions Python installed, run the install command with
the Python version you want to install to. For example, on Linux if both
Python 2.7 and 3.5 are installed, you can install to Python 3.5 with:

    $ sudo python3.5 setup.py install

From there, interacting with your devices is easy.

For U3:
>>> import u3
>>> d = u3.U3()
>>> d.configU3()
{'BootloaderVersion': '0.27',
 'CIODirection': 0,
 ...,
}
>>> d.close()

For U6:
>>> import u6
>>> d = u6.U6()
>>> d.configU6()
{'BootloaderVersion': '6.15',
 'FirmwareVersion': '0.88',
 ...,
}
>>> d.close()

For UE9:
>>> import ue9
>>> d = ue9.UE9()
>>> d.commConfig()
{'IPAddress' : '192.168.1.209'
 ...,
}
>>> d.close()

For U12:
>>> import u12
>>> d = u12.U12()
>>> d.eAnalogIn(0)
{'overVoltage': 0,
 'idnum': 0,
 'voltage': 1.42578125
}
>>> d.close()

For examples, check the Examples directory.

For documentation, please refer to the docstrings in the module source code,
or use the help function on the module, class or method.

For the U3, refer to its u3.py source, or use the “help(u3)” call in Python
(“import u3” beforehand).

For the U6, refer to its u6.py source, or use the “help(u6)” call in Python
(“import u6” beforehand).

For the UE9, refer to its ue9.py source, or use the “help(ue9)” call in Python
(“import ue9” beforehand).

For the U12, refer to its u12.py source, or use the “help(u12)” call in Python
(“import u12” beforehand).

For additional information, go to the LabJackPython page on LabJack's website:

    https://labjack.com/support/software/examples/ud/labjackpython


LICENSE

All LabJackPython library and example source code are licensed under MIT X11.
The license can be found in the LICENSE file.
