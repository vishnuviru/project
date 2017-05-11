from rest_framework import serializers
from .models import Main,Signup,Edit_Lane




class MainSerializer(serializers.ModelSerializer):
	class Meta:
		model=Main
		fields=(
			'User_Name',
			'Transaction_Id',
			'Lane_Number',
			'Location'
		)
class SignupSerializer(serializers.ModelSerializer):
	class Meta:
		model=Signup
		fields=('User_Type','Create_Time', 'Password', 'User_Name','First_Name','Last_Name','Lane_Number')

class Edit_Lane(serializers.ModelSerializer):
	class Meta:
		model=Edit_Lane
		fields=('Location', 'Lane_Number', 'User_Name', 'Direction')

