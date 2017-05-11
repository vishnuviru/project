from Tollapp.models import Signup
import random
for i in range(1,2):
    h = random.randint(10, 23)
    m = random.randint(10, 56)
    s = random.randint(10, 56)
    time =  "2017-03-03"+" "+str(h)+":"+str(m)+":"+str(s)
    type = "admin"
    pas = "admin123"
    user = "babu"
    z = Signup(User_Type= type,Timestamp = time,Password = pas,User_Name = user)
    z.save()
