from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from .models import Main,Signup
import os
from rest_framework import permissions,authentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render_to_response


from rest_framework.response import Response
from rest_framework import status

from .serializers import SignupSerializer




class UserLogin(APIView):

	""" for the use login """ 
	def get(self,request):
		return render_to_response('login.html',{})
class DisplayView(APIView):
	def get(self,request):
		if request.method=="POST":
			signup=Signup.objects.all()
			
			serializer=SignupSerializer(signup,many=True)
			
			return Response(serializer.data)
		elif request.method=="POST":
			serializer=SignupSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data,status=status.HTTP_201_CREATED)
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)