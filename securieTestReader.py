import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='smarte',
                             password='smarte',
                             db='smarte',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM zone_data WHERE security_id=%s"
        cursor.execute(sql, 1)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()