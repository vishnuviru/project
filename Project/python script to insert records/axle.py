from Tollapp.models import Axle_Count
import random
for x in range(31,61):
    h = random.randint(10, 20)
    m = random.randint(10, 57)
    s = random.randint(10, 58)
    tim = "2017-03-11"+" "+str(h)+":"+str(m)+":"+str(s)
    lane = random.randint(6,10)
    a = random.randint(3,8)
    flag = 0

    s = Axle_Count(Timestamp = tim,Lane_Number = lane,Axle = a,Flag = flag)
    s.save()






