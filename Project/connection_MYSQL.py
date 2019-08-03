from mysql.connector import connection
conn = connection.MySQLConnection(host="10.120.14.28", port=3306, database='stock', user='db102stock', password='db102stock_pwd')


mycursor = conn.cursor()

mycursor.execute("SELECT * FROM stock_inf")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

conn.close()
