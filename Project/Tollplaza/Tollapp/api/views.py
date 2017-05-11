from rest_framework.generics import ListAPIView
from Tollapp.models import Main

from .serializers import MainSerializer

class MainListAPIView(ListAPIView):
	queryset=Main.objects.all() 
	serializer_class=MainSerializer