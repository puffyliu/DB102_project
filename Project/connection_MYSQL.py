from mysql.connector import connection
conn = connection.MySQLConnection(host="10.120.14.18", port=3307, database='stock', user='db102stock', password='db102stock_pwd')


mycursor = conn.cursor()

mycursor.execute("SELECT * FROM stock_inf")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

conn.close()
