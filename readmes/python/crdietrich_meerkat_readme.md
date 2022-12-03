# Meerkat - Data Acquisition for Raspberry Pi or MicroPython

### Features  

* Support for Raspberry Pi and MicroPython
* Pure Python API to I2C devices
* Data output to JSON or CSV with JSON header
* Standardized timestamps string formats
* Data timestamping and GPS tagging of data  
* Metadata description of devices in JSON
* Parser to convert CSV output to Pandas DataFrame
* Object oriented class structure for REPL use

* Base methods separated from device drivers for reusability and extension

### Getting Started with Examples

The `examples` directory contains usage in Jupyter Notebooks and the `tests` folder contains scripts that will run on MicroPython or Linux.

### Supported Sensors and Devices  
| Device Type | Example Notebook | Driver File | I2C Address |
| ----------- | ---------------- | ----------- | ----------- |
| 1 Channel Relay        | [Sparkfun Qwiic Single Relay](/notebooks/relay_example.ipynb) | relay.py    | 0x18 |
| 8 Channel Relay        | [Peter Jakab 8 Channel Relay](/notebooks/mcp23008_example.ipynb) | mcp23008.py | 0x20 |
| DC & Stepper Motor     | [Grove Motor Driver v1.3](/notebooks/motor_example.ipynb) | motor.py   | 0x0F |
| Ambient Temperature    | [MCP9808](/notebooks/mcp9808_example.ipynb)   | mcp9808.py | 0x18 |
| DC Current & Power     | [INA219](/notebooks/ina219_example.ipynb)     | ina219.py  | 0x40 |
| Acceleration & Gyro    | [MPU6050](/notebooks/mpu6050_example.ipynb)   | mpu6050.py | 0x68 |
| Analog to Digital      | [ADS1115](/notebooks/ads_example.ipynb)   | ads.py     | 0x48 |
| Digital to Analog      | [MCP4728](/notebooks/mcp4728_example.ipynb)  | mcp4728.py | 0x60 |
| pH                     | [Atlas Sensors](/notebooks/atlas_pH.ipynb) | atlas.py   | 0x63 |
| Conductivity           | [Atlas Sensors](/notebooks/atlas_conductivity.ipynb) | atlas.py   | 0x64 |
| Temperature, Humidity, Pressure, VOC Gas | [Bosch BME680](/notebooks/bme_680_example.ipynb) | bme680.py  | 0x77 |
| GPS                    | [PA1010D](/notebooks/pa1010d_example.ipynb)   | pa1010d.py | 0x10 |
| RTC                    | [DS3221](/notebooks/ds3231_example.ipynb)    | ds3231.py  | 0x68 |

### Supported Python Platforms
Python 3, Jupyter and Pandas

* Raspberry Pi Model 3
* Raspberry Pi Model 4

MicroPython

* FiPy (should work on all PyCom boards)
* OpenMV Cam M7 (tested with OV7725)

### Contributing  

Contributions are welcome! Please read our [Code of Conduct](https://www.contributor-covenant.org/version/1/4/code-of-conduct/).
