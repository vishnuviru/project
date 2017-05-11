from Tollapp.models import Main,Signup
from datetime import date
from dateutil.rrule import rrule, DAILY
from django.db.models import Sum
date1 = "2017-04-23"
date2 = "2017-04-25"
lane = 1


print date1,date2,lane
ca = date1.split('-')


cb = date2.split('-')
dd = []
report = []
a = date(int(ca[0]),int(ca[1]),int(ca[2]))
b = date(int(cb[0]),int(cb[1]),int(cb[2]))
av = Signup.objects.filter(Lane_Number = lane)
for i in av:
	aa = i.User_Name
	
print aa
print a,b
for dt in rrule(DAILY, dtstart=a, until=b):
	final = dt.strftime("%Y-%m-%d")
		
	data = {}
	
	
	
	
	
	
