from Tollapp.models import Sensor_Details
import random
for i in range(1,6):
    height = random.randint(4,10)
    length = random.randint(6,20)
    breadth = random.randint(4,19)
    h = random.randint(10, 23)
    m = random.randint(10, 56)
    s = random.randint(10, 56)
    tim = "2017-03-09"+" "+str(h)+":"+str(m)+":"+str(s)
    laneno = 2
    flag = 0
    z = Sensor_Details(Timestamp = tim,Lane_Number = laneno,Flag = flag,Dimension_Height = height,Dimension_Length = length,Dimension_Breadth = breadth)
    z.save()
