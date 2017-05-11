from Tollapp.models import Weigh_Bridge
import random
for x in range(31,61):
    h = random.randint(10, 20)
    m = random.randint(10, 57)
    s = random.randint(10, 58)
    tim = "2017-03-01"+" "+str(h)+":"+str(m)+":"+str(s)
    lane = random.randint(6, 10)
    w = random.randrange(100,8000,200) 
    flag = 0

    s = Weigh_Bridge(Timestamp = tim,Lane_Number = lane,Weight = w,Flag = flag)
    s.save()






