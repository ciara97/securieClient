import serial
import struct
import pymysql.cursors



def storeData(data_tuple):
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='securieTest',
                                 password='securieTest',
                                 db='securietestdb',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO securieTestData( guardID, numConnections, noiseLevel, lightLevel) VALUES (%s, %s, %s, %s);"
            cursor.execute(sql, data_tuple)

        # connection is not autocommit.
        connection.commit()
    finally:
        connection.close()


while True:
    with serial.Serial('COM2', 19200) as ser:
        bytes_rec = ser.read(16)

    data_struct = struct.Struct('IIII')
    unpacked_data = data_struct.unpack(bytes_rec)
    print(unpacked_data)
    storeData(unpacked_data)

