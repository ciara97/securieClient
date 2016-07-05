# quick script to test securieClient
# used in conjunction with serial port emulators
import serial
import struct

packed = struct.pack('IIII', 1, 2, 3, 4)

with serial.Serial('COM1', 19200, timeout=3) as ser:
    ser.write(packed)
