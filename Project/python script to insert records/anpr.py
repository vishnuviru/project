from Tollapp.models import Anpr
import random
for i in range(1,41):
    v_no = random.choice(['TN06CD1190','AP16T3680','KA19Y7777','MH11J8990','PY22K1919','GA01Q5233','GJ08U7567','TN02U0001','TN12T1234'])
    h = random.randint(10, 23)
    m = random.randint(10, 56)
    s = random.randint(10, 56)
    tim = "2017-02-09"+" "+str(h)+":"+str(m)+":"+str(s)
    laneno = 7
    flag = 0
    
    z = Anpr(Timestamp = tim,Vehicle_Number= v_no,Lane_Number = laneno,Flag = flag)
    z.save()
