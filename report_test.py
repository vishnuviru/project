import MySQLdb
import sys
import os
from datetime import datetime






# Open database connection
db = MySQLdb.connect("localhost","root","p@ssw0rd","testing" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT Lane_Number,User_Name,Vehicle_class,count(Transaction_Id) FROM Tollapp_main  WHERE DATE(Timestamp) = '%s' group by Lane_Number,User_Name,Vehicle_Class" % ("2017-04-21")
cursor.execute(sql)
#conn.commit()
results = cursor.fetchall()

widths = []
columns = []
tavnit = '|'
separator = '+' 

for cd in cursor.description:
    widths.append(max(cd[2], len(cd[0])))
    columns.append(cd[0])

for w in widths:
    tavnit += " %-"+"%ss |" % (w,)
    separator += '-'*w + '--+'

print(separator)
print(tavnit % tuple(columns))
print(separator)
for row in results:
    print(tavnit % row)
print(separator)
