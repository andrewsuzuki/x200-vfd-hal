#!/usr/bin/env python3
import minimalmodbus
import time

# Set up instrument

instrument = minimalmodbus.Instrument("/dev/ttyS0", 0x0001) # port name, slave address

instrument.mode = minimalmodbus.MODE_RTU
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.6
instrument.serial.write_timeout = 2.0

# Coil, register addresses
# (Represented as their specified "number" in the manual, minus one)

COIL_WRITE_RUN = 0x0001-1
COIL_WRITE_FORWARD = 0x0002-1
COIL_WRITE_TRIP = 0x0003-1
COIL_WRITE_RESET = 0x0004-1
COIL_READ_RUNNING = 0x000E-1
COIL_READ_REVERSE = 0x000F-1
COIL_READ_READY = 0x0010-1
COIL_READ_ALARM = 0x0014-1
COIL_READ_AT_SPEED = 0x0018-1
REGISTER_OPERATING_FREQUENCY = 0x0002-1

def read_coils():
    assert COIL_READ_REVERSE > COIL_READ_RUNNING
    assert COIL_READ_READY > COIL_READ_RUNNING
    assert COIL_READ_ALARM > COIL_READ_RUNNING
    assert COIL_READ_AT_SPEED > COIL_READ_RUNNING

    # read multiple bits. number of bits = last - first + 1
    coils = instrument.read_bits(COIL_READ_RUNNING, COIL_READ_AT_SPEED - COIL_READ_RUNNING + 1)

    # read into dictionary
    return {
        "running": coils[COIL_READ_RUNNING - COIL_READ_RUNNING],
        "reverse": coils[COIL_READ_REVERSE - COIL_READ_RUNNING],
        "ready": coils[COIL_READ_READY - COIL_READ_RUNNING],
        "alarm": coils[COIL_READ_ALARM - COIL_READ_RUNNING],
        "at_speed": coils[COIL_READ_AT_SPEED - COIL_READ_RUNNING]
    }

def write_run(yes):
    instrument.write_bit(COIL_WRITE_RUN, yes)

def write_reverse(is_reverse):
    instrument.write_bit(COIL_WRITE_FORWARD, not is_reverse)

def write_trip():
    instrument.write_bit(COIL_WRITE_TRIP, True)

def write_reset():
    instrument.write_bit(COIL_WRITE_RESET, True)
    # TODO sleep for one second by default?

def read_frequency():
    return instrument.read_register(REGISTER_OPERATING_FREQUENCY, 1)

def write_frequency(freq):
    instrument.write_register(REGISTER_OPERATING_FREQUENCY, freq, 1)

# scratchpad area

def dump():
    cd = read_coils()
    freq = read_frequency()
    print("COILS:")
    for k in cd:
        print(k, str(cd[k]))
    print("FREQ:", freq)

def the_paces():
    print("> resetting")
    write_reset()
    dump()
    time.sleep(1)

    print("> setting run to true")
    write_run(True)
    dump()
    time.sleep(1)

    print("> setting frequency to 30Hz")
    write_frequency(30)
    dump()
    time.sleep(8)

    print("> setting frequency to 50Hz")
    write_frequency(50)
    dump()
    time.sleep(8)

    print("> setting frequency to 100Hz")
    write_frequency(100)
    dump()
    time.sleep(8)

    print("> setting frequency to 15Hz")
    write_frequency(15)
    dump()
    time.sleep(8)

    print("> setting frequency to 15Hz")
    write_frequency(15)
    dump()
    time.sleep(8)

    print("> setting run to false")
    write_run(False)
    dump()
    time.sleep(5)

    print("> tripping")
    write_trip()
    dump()

the_paces()
