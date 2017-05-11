from Tollapp.models import Main
import random
for i in range(100001,200001):
	h = random.randint(10,23)
	m = random.randint(10,55)
	s = random.randint(10,58)
	tim = "2017-04-02"+" "+str(h)+":"+str(m)+":"+str(s)
	a = Main.objects.filter(id = i,Transaction_Id = i).update(Timestamp = tim)
	
	