# NxOS-sim - NxOS ported to run on a virtual ARM simulation platform

## History

The original [NxOS](https://github.com/danderson/nxos) and [NxOS-armdebug](https://github.com/tcwan/nxos-armdebug) were developed to run on the LEGO Mindstorms NXT kit. 

## NxOS-sim

This is a port of the core NxOS code to run on an ARM simulation platform. The target platform is [CPUlator](https://cpulator.01xz.net/?sys=arm-de1soc) which simulates an Altera Cyclone V FPGA-based development board (DE1-SoC) with an ARM Cortex-A9 core.
[CPUlator](https://cpulator.01xz.net) is developed by Henry Wong at the University of Toronto, Canada.

## Features

Not all the features of [CPUlator](https://cpulator.01xz.net/doc/#sim_processors) will be used. 

The focus of this port is to support the ARMv4T architecture's ARM state operation found in the Atmel 91SAM7S256 Microcontroller of the LEGO Mindstorms NXT brick.
Since CPUlator does not have any support for the LEGO Mindstorms sensors or motors, only selected I/O peripherals from the DE1-SoC board simulator will be used.

Interrupt-driven peripheral device drivers will not be implemented (this may change in the future). 

Thumb state support is not available in CPUlator at this time. In addition, only a subset of the Cortex-A9 core ARMv7-A instruction set will be used by NxOS, notably the common ARMv4 subset. 

NOTE: some ARMv5 instructions such as BLX may be adopted since common subroutine call conventions for modern 32-bit ARM coding uses them frequently.

## Directory Structure
- guides: Guides for running NxOS applications
- nxos: NxOS Project Main Directory (see nxos/README for more details)
- scripts: Miscellaneous cross-compiler toolchain utilities

## Getting Started Guide

See the guide for how to [build and execute NxOS-sim applications](guides/CPUlator-setup.md)
