# pip install mysql-connector-python

import mysql.connector

conn=mysql.connector.connect(host='localhost',
                             password='123456',       # check the password
                             user='root',
                             database='customer')

cursor=conn.cursor()

cursor.execute("show databases")        # no need to give 'database' in conn
for i in cursor:
    print(i)
print()

cursor.execute("show tables")        # need to mention database of the table in 'conn' section
for i in cursor:
    print(i)
print()

cursor.execute("select * from manager")     # need to mention database of the table in 'conn' section
for i in cursor:
    print(i)

cursor.close()
conn.close()        # always close the connection
print("************ Database closed successfully *****************")