# script to continuosly transfer data from the serial port
# and to store it in database for STEM project
import serial
import struct
import pymysql.cursors


# connects to database and stores info
def storeData(data_tuple):
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='smarte',
                                 password='smarte',
                                 db='smarte',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO zone_data( security_id, area_code, attn_count, noise_level, light_level) VALUES (%s, %s, %s, %s, %s);"
            cursor.execute(sql, data_tuple)

        # connection is not autocommit.
        connection.commit()
    finally:
        connection.close()


while True:
    # open serial connection
    with serial.Serial('COM2', 19200) as ser:
        bytes_rec = ser.read(32)

    # cretae struct for data unpacking
    data_struct = struct.Struct('IIIdd')
    unpacked_data = data_struct.unpack(bytes_rec)
    print(unpacked_data)
    storeData(unpacked_data)

