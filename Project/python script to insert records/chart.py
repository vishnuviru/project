from Tollapp.models import main
import datetime
a = "2017-02-10"
b = "2017-02-24"
c = a.split('-')
start = int(c[0]),int(c[1]),int(c[2])
d = b.split('-')
end = int(d[0]),int(d[1]),int(d[2])
f = main.objects.filter(timestamp__gte = datetime.date(start),timestamp__lte = datetime.date(end),vehicle_status = "permit").count()



