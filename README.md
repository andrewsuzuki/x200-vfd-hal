# x200-vfd-hal

HAL component enabling communication between the Hitachi X200 VFD and LinuxCNC.

Adapted from the Hitachi WJ200 HAL component.

Changes from WJ200 component (in 2014 @ commit e17d199):
- Rename all mentions of "wj200"/"WJ200" to "x200"/"X200"
- The WJ200 frequency has 0.01Hz resolution whereas the X200 has 0.1Hz resolution. Therefore, the X200 should be scaled by 10, not 100.
- Different Coil Numbers:
    - Run 0x0001
    - Direction command 0x0002 => reversed from WJ200
    - External trip 0x0003
    - Trip reset 0x0004
    - Run status 0x000E
    - Direction status 0x000F
    - Ready 0x0010
    - Alarm signal 0x0014
    - Frequency arrival signal (at speed) 0x0018
- Different Register numbers:
    - Operating frequency 0x0002
- Fix segfaults with bits array (reading 11 bits from modbus => array with 11 elements)
- more fprintfs

Changes from WJ200 component (in 2019 @ commit a63ec76):
- License (linuxcnc a63ec76)
- add dynamic --device argument (linuxcnc 98bee0d)
- warn on unhandled arguments (linuxcnc 5a617cb)

Other new changes:
- Corrected formatting
- More comments
- X200 direction command wasn't working, enable it (inverse of WJ200 bit, and inverse of direction status, confusing in both cases)
- WJ200/X200 was reading from an unnecessary number of registers
- Add extra compiler/linker args to refer gcc to libmodbus on Linux CNC's Debian Wheezy (-I/usr/local/include/modbus and -L/usr/local/lib)

## Loading in LinuxCNC

Note that arguments must be supplied using equal signs (due to unhandled argument checking).

Loading:

```
loadrt x200-vfd --device=/dev/ttyS0 --baud=19200
setp x200-vfd.0.mbslaveaddr 1
```

TODO connect to linuxcnc

## Dependencies

- libmodbus
- halcompile, gcc

## Credits

* Andrew Suzuki - @andrewsuzuki - [andrewsuzuki.com](http://andrewsuzuki.com)

## Contributing

Issues / pull requests are welcome!

## License

GPL 2.0
