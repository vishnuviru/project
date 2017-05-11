from Tollapp.models import Main
from datetime import datetime as Datetime
import datetime

date1 = "2017-04-19"
date2 = "2017-04-20"

ca = date1.split('-')
cb = date2.split('-')
print "caaaaa",ca,cb,type(ca)



a = Main.objects.filter(Lane_Number = 1)

for i in a:
	s = i.Timestamp.strftime("%Y-%m-%d")
	
	if date1<=s<=date2:
		print s
		
		


fin = Main.objects.filter(Timestamp__gte = datetime.date(int(ca[0]),int(ca[1]),int(ca[2])),Timestamp__lte = datetime.date(int(cb[0]),int(cb[1]),int(cb[2])),Lane_Number = 5)
full = 0
for x in fin:
	
	am = x.Fine_Amount
	full += am

	
print full