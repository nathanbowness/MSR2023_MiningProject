## PX4Flow Firmware

[![Build Status](https://travis-ci.org/PX4/Flow.svg?branch=master)](https://travis-ci.org/PX4/Flow)

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/PX4/Firmware?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

PX4 FLOW is a smart camera processing optical flow directly on the camera module. It is optimized for processing and outputs images only for development purposes. Its main output is a UART or I2C stream of flow measurements at ~400 Hz.

Dev guide / toolchain installation:
https://docs.px4.io/master/en/sensor/px4flow.html

For help, run:

```bash
make help
```

To build, run:
```bash
  make archives # this needs to be done only once
  make
```

To flash via the PX4 bootloader (first run this command, then connect the board):
```bash
  make upload-usb
```

By default the px4flow-v1_default is uploaded; to upload a different version, run:

```bash
  make <target> upload-usb
```
Where `<target>` is one of the px4flow targets listed by `make help`.
