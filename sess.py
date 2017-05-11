from django.contrib.sessions.models import Session

se = Session.objects.filter(session_key = "vishn")
for i in se:
	d = i.get_decoded()
	ss = i.session_key
	print d,ss
