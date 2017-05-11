from rest_framework.serializers import ModelSerializer
from Tollapp.models import Main



class MainSerializer(ModelSerializer):
	class Meta:
		model=Main
		fields=[
			'User_Name',
			'Transaction_Id',
			'Vehicle_Number',
		]
