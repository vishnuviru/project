from Tollapp.models import Edit_Lane
import random
for i in range(1,2):
    user = "vishnu"
    h = random.randint(10, 23)
    m = random.randint(10, 56)
    s = random.randint(10, 56)
    tim = "2017-02-09"+" "+str(h)+":"+str(m)+":"+str(s)
    lane = random.randint(1,10)
    d = random.choice(['incoming','outgoing'])
    cam1 = "192.168.30.20"
    cam2 = "192.168.30.15"
    z = Edit_Lane(Location = "TADA",Lane_Number = lane,User_name = user,Direction = d,Created_Time = tim,Update_Time = tim,Camera1 = cam1,Camera2 = cam2)
    z.save()
