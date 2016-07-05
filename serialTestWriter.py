# quick script to test securieClient
# used in conjunction with serial port emulators
import serial
import struct

packed = struct.pack('IIIdd', 1, 112, 32, 3.0, 4.0)

with serial.Serial('COM1', 19200, timeout=10) as ser:
    ser.write(packed)
