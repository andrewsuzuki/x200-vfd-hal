# x200-vfd-hal

HAL component enabling communication between the Hitachi X200 VFD and LinuxCNC.

Adapted from the Hitachi WJ200 HAL component.

Changes from WJ200 component (in 2014 @ commit e17d199):
- Rename all mentions of "wj200"/"WJ200" to "x200"/"X200"
- The WJ200 frequency has 0.01Hz resolution whereas the X200 has 0.1Hz resolution. Therefore, the X200 should be scaled by 10, not 100.
- Coil Numbers:
    - Run 0x0001
    - Direction command 0x0002 => reversed from WJ200
    - External trip 0x0003
    - Trip reset 0x0004
    - Run status 0x000E
    - Direction status 0x000F
    - Ready 0x0010
    - Alarm signal 0x0014
    - 0x0018
- Register numbers:
    - Operating frequency 0x0002

TODO Changes from WJ200 component (in 2019 @ commit a63ec76):
- license (linuxcnc a63ec76)
- heatsink-temp (linuxcnc fcef430)
- output current monitor (linuxcnc 11ee2b9)
- add dynamic --device argument (linuxcnc 98bee0d)
- warn on unhandled arguments (linuxcnc 5a617cb)

TODO possible issues:
- libmodbus isn't included in the .comp configuration section
- decide on snake case vs camel case and update accordingly

Other new changes:
- Corrected formatting
- More comments
- WJ200/X200 was reading from an unnecessary number of registers
- X200 direction command wasn't working, enable it (opposite of WJ200 bit)

## Loading in LinuxCNC

TODO document

## Dependencies

- libmodbus
- halcompile, gcc

## Credits

* Andrew Suzuki - @andrewsuzuki - [andrewsuzuki.com](http://andrewsuzuki.com)

## Contributing

Issues / pull requests are welcome!

## License

GPL 2.0
