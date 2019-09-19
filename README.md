# x200-vfd-hal

HAL component enabling communication between the Hitachi X200 VFD and LinuxCNC.

Adapted from the Hitachi WJ200 HAL component.

Changes from WJ200 component (in 2014 @ commit e17d199):
- Rename all mentions of "wj200"/"WJ200" to "x200"/"X200"
- The WJ200 frequency has 0.01Hz resolution whereas the X200 has 0.1Hz resolution. Therefore, the X200 should be scaled by 10, not 100.
- Coil/Register Addresses:
    - TODO 

TODO Changes from WJ200 component (in 2019 @ commit a63ec76):
- license (linuxcnc a63ec76)
- heatsink-temp (linuxcnc fcef430)
- output current monitor (linuxcnc 11ee2b9)
- increase bits array from length 10 to 16 (linuxcnc 97d2452)
    - => the issue this fixes is segfaulting. Is this necessary with the original x200 change to length 12, with initializing?
- add dynamic --device argument (linuxcnc 98bee0d)
- warn on unhandled arguments (linuxcnc 5a617cb)

TODO possible issues:
- The 2016 x200 file sets frequency at address at 0x001, but shouldn't it be at 0x002?
- libmodbus isn't included in the .comp configuration section

Other new changes:
- Corrected formatting
- More comments
- added libmodbus to extra compile/link args

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
