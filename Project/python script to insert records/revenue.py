from Tollapp.models import Main
from datetime import datetime as Datetime
import datetime

date1 = "2017-04-15"
date2 = "2017-04-30"

ca = date1.split('-')
ss = int(ca[2])

cb = date2.split('-')
ee = int(cb[2]) + 1
vs = "LMV-TR"
user = "aravind"
lane = 1
per = "permit"
sta = "OK"

ff = []

for s in range (ss,ee):

	tt = Main.objects.filter(Timestamp__startswith = datetime.date(2017,04,s),Lane_Number =1 ,User_Name = "aravind").count()
	qq = Main.objects.filter(Timestamp__startswith = datetime.date(2017,04,s),Lane_Number =1 ,User_Name = "aravind",Vehicle_Status = "OK").count()
	rr = Main.objects.filter(Timestamp__startswith = datetime.date(2017,04,s),Lane_Number =1 ).count()


	print datetime.date(2017,04,s),qq,tt,rr
	ff.append(tt)

print ff,ss,ee

