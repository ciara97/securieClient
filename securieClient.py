import sqlite3, serial, struct

with serial.Serial('COM2', 19200, timeout=10) as ser:
    bytes_rec = ser.read(20)

data_struct = struct.Struct('IIIII')
unpacked_data = data_struct.unpack(bytes_rec)
print(unpacked_data)


