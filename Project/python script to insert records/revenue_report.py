import MySQLdb
import sys
import os
from datetime import datetime






# Open database connection
db = MySQLdb.connect("localhost","root","p@ssw0rd","testing" )

# prepare a cursor object using cursor() method
cursor = db.cursor()




result = []   
        
sql = "SELECT User_Name,Lane_Number,Vehicle_Class,count(Transaction_Id)from Tollapp_main where Lane_Number = 1 "
  
              
cursor.execute(sql)
data = {}
data["lane"] = cursor.fetchall()
result.append(data)
print result
        
       
    
      
      





