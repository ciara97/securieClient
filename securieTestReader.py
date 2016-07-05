import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='securieTest',
                             password='securieTest',
                             db='securieTestDB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM securieTestData WHERE guardID=%s"
        cursor.execute(sql, 1)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()