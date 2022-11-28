# LineageOS 14.1  Device tree for Samsung GT-S7580 (kylepro)

### Specs (Physically inspected):
  - CPU: Cortex-A9 (Little endian, Dual Core)
  - Codename: KYLEPRO
  - Display Panel: NT35510 (TFT)
  - Display Resolution: 480x800 (240dpi)
  - EMMC: 4GB (Usable ~2.2GB)
  - Family: KONA (BROADCOM)
  - GPU: Broadcom VideoCore IV (? clock, ~50MB VRAM from RAM)
  - Misc: WIFI/Tether, Bluetooth, HSPA+, GPS, FM-Radio
  - PMU: BCM59054
  - Platform: HAWAII (BROADCOM)
  - RAM: 768MB (not shared with GPU)
  - Sensor: Accelerometer (BMC150), Compass (BMC150), Proximity (GP2AP002)
  - Shipped with Android 4.2.2
  - SoC: BCM21664T (1.2GHz)
  - Touch Panel: IST3032 (Max 2 Touch Points?)
  - WIFI/Bluetooth/FM-Radio: BCM4330

### Notice:
  - Apply patch *PATCH_CM-14.1.diff* to root directory of LOS-14.1 source code before build

### Other resource:
  - Kernel source: https://github.com/ishantvivek/android_kernel_samsung_kyleproxx
  - Vendor blobs: https://github.com/ishantvivek/android_vendor_samsung_kyleproxx

### More Information:
```sh
$ cat /proc/cpuinfo
Processor       : ARMv7 Processor rev 0 (v7l)                    
processor       : 0                                              
BogoMIPS        : 1190.29                                        
                                                                 
processor       : 1                                              
BogoMIPS        : 1190.29                                        
                                                                 
Features        : swp half thumb fastmult vfp edsp neon vfpv3 tls
CPU implementer : 0x41                                           
CPU architecture: 7                                              
CPU variant     : 0x3                                            
CPU part        : 0xc09                                          
CPU revision    : 0                                              
                                                                 
Hardware        : hawaii_ss_kylepro                              
Revision        : 0000                                           
Serial          : 0000000000000000                               
```

```sh
$ cat /proc/emmc
dev:         size       erasesize       name
mmcblk0p1: 00000800 00000400 "cal"
mmcblk0p2: 00000200 00000400 "sysparm_dep"
mmcblk0p3: 00000200 00000400 "parm-spml_dep"
mmcblk0p4: 00000200 00000400 "RF_CAL_FILE"
mmcblk0p5: 00004000 00000400 "KERNEL"
mmcblk0p6: 00004000 00000400 "RECOVERY"
mmcblk0p7: 00009600 00000400 "modem"
mmcblk0p8: 00000400 00000400 "reserved"
mmcblk0p9: 00001000 00000400 "SBL1"
mmcblk0p10: 00001000 00000400 "SBL2"
mmcblk0p11: 00004000 00000400 "PARAM"
mmcblk0p12: 00000400 00000400 "DTSBK"
mmcblk0p13: 00000400 00000400 "DTS"
mmcblk0p14: 00000200 00000400 "FOTA_SIG"
mmcblk0p15: 0000a000 00000400 "efs"
mmcblk0p16: 00064000 00000400 "CSC"
mmcblk0p17: 00241570 00000400 "system"
mmcblk0p18: 0000f000 00000400 "HIDDEN"
mmcblk0p19: 0046c000 00000400 "userdata"
```

### Credits (Sort by alphabetical order):
  - ghsr
  - Ishant Vivek
  - Pawitp
  - Sandpox
  - TheComputerGuy96
  - The CyanogenMod Team
  - TheNikiz
  - Zim555
