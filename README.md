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

```
loadrt x200-vfd --device=/dev/ttyS0 --baud=19200

setp x200-vfd.0.mbslaveaddr 1

# without pncconf (substitute your own signal names)
net machine-is-on halui.machine.is-on => x200-vfd.0.enable
net spindle-on motion.spindle-on => x200-vfd.0.run
net spindle-reverse motion.spindle-reverse => x200-vfd.0.reverse
net spindle-speed-cmd motion.spindle-speed-out-abs => x200-vfd.0.commanded-frequency

# with pncconf (in custom.hal)
net machine-is-on => x200-vfd.0.enable
net spindle-enable => x200-vfd.0.run
net spindle-ccw => x200-vfd.0.reverse
net spindle-vel-cmd-rpm-abs => x200-vfd.0.commanded-frequency

# ?
net spindle-at-speed <= x200-vfd.0.is-at-speed

# Scaling ? trying 60Hz/1RPM

loadrt scale count=1
addf scale.0 servo-thread
setp scale.0.gain 60.0
net spindle-vel-cmd-rpm-abs => scale.0.in
net spindle-frequency scale.0.out => x200-vfd.0.commanded-frequency

```

TODO more out bits (is-running, is-ready, is-alarm)?

TODO watchdog-out

## Dependencies

- libmodbus
- halcompile, gcc

## Credits

* Andrew Suzuki - @andrewsuzuki - [andrewsuzuki.com](http://andrewsuzuki.com)

## Contributing

Issues / pull requests are welcome!

## License

GPL 2.0
