from django.db.models import Count,Sum
from Tollapp.models import Main
date = "2017-04-16"
a = Main.objects.filter(Lane_Number = 1).values('User_Name').annotate(vs = Count('Vehicle_Status')).order_by('User_Name')
b = Main.objects.filter(Timestamp__startswith = date,Lane_Number = 1,Vehicle_Class = "LMV").values('Lane_Number','User_Name').annotate(clas = Count('Vehicle_Class'),ok = Count('Vehicle_Status'),sta =  Count('Status'),fine = Sum('Fine_Amount'))

#b = Main.objects.filter(Timestamp__startswith = date,Lane_Number = 1).value("User_Name","Timestamp")annotate(clas = Count('Vehicle_Class'))
#a = b[0].clas
print b


	
