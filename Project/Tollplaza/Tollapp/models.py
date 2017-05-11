from django.db import models
from datetime import datetime 

place = "TADA"

class  Main(models.Model):
	Transaction_Id = models.CharField(max_length=200)
	Vehicle_Number = models.CharField(max_length=200,default= "NA")
	Dimension_Height = models.IntegerField(default=0)
	Dimension_Length = models.IntegerField(default=0)
	Dimension_Breadth = models.IntegerField(default=0)
	Pollution = models.DateField()
	Fitness = models.DateField()
	Permit = models.DateField()
	User_Name = models.CharField(max_length=200,default="NA")
	Officer_Name = models.CharField(max_length=200,default="NA")
	Axle = models.IntegerField(default=0)
	Vehicle_Type = models.CharField(max_length=200,default="NA")
	Location = models.CharField(max_length=200,default=place)
	Lane_Number = models.IntegerField(default=0)
	Direction = models.CharField(default="NA",max_length=200)
	Weight = models.IntegerField(default=0)
	Timestamp = models.DateTimeField(default=datetime.now())
	Registration_Date = models.DateField()
	Chassis_Number = models.CharField(default="NA",max_length=200)
	Engine_Number = models.CharField(default="NA",max_length=200)
	Vehicle_Fuel_Type = models.CharField(default="NA",max_length=200)
	Engine_Cubic_Capacity = models.CharField(default="NA",max_length=200)
	Tax = models.DateField()
	Insurance = models.DateField()
	National_Permit = models.DateField()
	Authorization = models.DateField()
	Laden_Weight=models.IntegerField(default=0)
	Unladen_Weight = models.IntegerField(default=0)
	Fine_Amount = models.IntegerField(default=0)
	Comment = models.CharField(default="NA",max_length=100)
	Vehicle_Class = models.CharField(default="NA",max_length=100)
	Sensor_Height = models.IntegerField(default=0)
	Sensor_Length = models.IntegerField(default=0)
	Sensor_Breadth = models.IntegerField(default=0)
	Sensor_Axle = models.IntegerField(default=0)
	Vehicle_Status=models.CharField(default="NA",max_length=100)
	Image_1 = models.CharField(default="NA",max_length=1000)
	Image_2 = models.CharField(default="NA",max_length=1000)
	Status=models.CharField(default="NA",max_length=100)


	def save(self, *args, **kwargs):
		if self.id == None:
			super(Main, self).save(*args, **kwargs)
			self.Transaction_Id = datetime.now().strftime("%d%m%y%H%M%S")
			self.save()
		else:
			super(Main, self).save(*args, **kwargs)


class Signup(models.Model):
		
	User_Type = models.CharField(max_length=100)	
	Created_Time = models.DateTimeField(default=datetime.now())
	Updated_Time = models.DateTimeField(default=datetime.now())
	Password = models.CharField(default="NA",max_length=100)
	User_Name = models.CharField(default="NA",max_length=100)
	First_Name = models.CharField(default="NA",max_length=100)
	Last_Name = models.CharField(default="NA",max_length=100)
	Lane_Number = models.IntegerField(default= 0)
	Location = models.CharField(default= place,max_length=100)


class Edit_Lane(models.Model):
	Location = models.CharField(default=place,max_length=200)
	Lane_Number = models.IntegerField()
	User_Name = models.CharField(default="NA",max_length=200)
	Direction = models.CharField(default="NA",max_length=200)
	Created_Time = models.DateTimeField(auto_now_add = True)
	Updated_Time = models.DateTimeField(auto_now = True)
	Anpr_Ip = models.GenericIPAddressField(default="NA")
	Camera_Ip = models.GenericIPAddressField(default="NA")
	Profiler_Ip = models.GenericIPAddressField(default="NA")
	Boombarrier_Ip = models.GenericIPAddressField(default="NA") 
	Weighbridge_Ip = models.GenericIPAddressField(default="NA")
	User_Ip = models.GenericIPAddressField(default="NA")
	Flag = models.BooleanField(default=0)


class Anpr(models.Model):
	Timestamp = models.DateTimeField(default=datetime.now())
	Vehicle_Number = models.CharField(default="NA",max_length=200)
	Lane_Number = models.IntegerField()
	Flag = models.BooleanField(default=0)
	


class Officer(models.Model):
	Vehicle_Number = models.CharField(default=0,max_length=200)
	Transaction_Id = models.CharField(default=0,max_length=200)
	Permit = models.DateField()
	Lane_Number = models.IntegerField()
	Officer_Id = models.IntegerField()
	officer_Name = models.CharField(max_length=100)
	Fine_Amount = models.IntegerField()
	Timestamp = models.DateTimeField(default=datetime.now())
	User_Name = models.CharField(default="NA",max_length=100)
	Location = models.CharField(default= place,max_length=100)



class Log_Details(models.Model):
	Transaction_Id = models.CharField(max_length=200)
	Vehicle_Number = models.CharField(max_length=200)
	Timestamp = models.DateTimeField(default=datetime.now())
	Officer_Name = models.CharField(max_length=100)
	Permit = models.DateField()
	Vehicle_Type = models.CharField(max_length=200,default="NA")
	Weight = models.IntegerField(default=0)
	Lane_Number = models.IntegerField(default=0)
	Location = models.CharField(max_length=200,default= place)
	Comment = models.CharField(default="NA",max_length=100)
	Vehicle_Class = models.CharField(default="NA",max_length=100)
	Vehicle_Status = models.CharField(default="NA",max_length=100)
	Fine_Amount=models.IntegerField(default=0)

class Sensor_Details(models.Model):
	Lane_Number=models.IntegerField(default=0)
	Dimension_Height = models.IntegerField(default=0)
	Dimension_Breadth = models.IntegerField(default=0)
	Dimension_Length = models.IntegerField(default=0)
	Timestamp = models.DateTimeField(default=datetime.now())
	Flag = models.BooleanField(default=0)
	
class Rto(models.Model):

	Vehicle_Number = models.CharField(default=0,max_length=200)
	Dimension_Length = models.IntegerField()
	Dimension_Height = models.IntegerField()
	Dimension_Breadth = models.IntegerField()
	Fitness = models.DateField()
	Permit = models.DateField()
	Pollution = models.DateField()
	Axle = models.IntegerField()
	Vehicle_Class = models.CharField(default = "NA",max_length=100)
	Registration_Date=models.DateField()
	Chassis_Number = models.CharField(default = "NA",max_length=200)
	Engine_Number = models.CharField(default = "NA",max_length=200)
	Vehicle_Fuel_Type = models.CharField(default = "NA",max_length=200)
	Engine_Cubic_Capacity = models.CharField(default = "NA",max_length=200)
	Tax = models.DateField()
	Insurance = models.DateField()
	National_Permit = models.DateField()
	Authorization = models.DateField()
	Unladen_Weight = models.IntegerField(default=0)
	Vehicle_Type = models.CharField(default = "NA",max_length=100)
	
class Relay_Panel(models.Model):

	
	Lane_1=models.BooleanField(default=1)
	Lane_2=models.BooleanField(default=1)
	Lane_3=models.BooleanField(default=1)
	Lane_4=models.BooleanField(default=1)
	Lane_5=models.BooleanField(default=1)
	Lane_6=models.BooleanField(default=1)
	Lane_7=models.BooleanField(default=1)
	Lane_8=models.BooleanField(default=1)
	Lane_9=models.BooleanField(default=1)
	Lane_10=models.BooleanField(default=1)
	Lane_11=models.BooleanField(default=1)
	Lane_12=models.BooleanField(default=1)
	Lane_13=models.BooleanField(default=1)
	Lane_14=models.BooleanField(default=1)
	Lane_15=models.BooleanField(default=1)
	Lane_16=models.BooleanField(default=1)

class Weigh_Bridge(models.Model):
	Timestamp=models.DateTimeField(default = datetime.now())
	Lane_Number=models.IntegerField(default=0)
	Weight=models.IntegerField(default=0)
	Flag=models.BooleanField(default=0)

class Axle_Count(models.Model):
	Timestamp=models.DateTimeField(default=datetime.now())
	Lane_Number=models.IntegerField(default=0)
	Axle=models.IntegerField(default=0)
	Flag=models.BooleanField(default=0)


class Monitor(models.Model):
	Lane_Number = models.IntegerField(default=0)
	Webapp = models.GenericIPAddressField(default="NA")
	Anpr = models.GenericIPAddressField(default="NA")
	Profiler =models.GenericIPAddressField(default="NA")
	Weighbridge = models.GenericIPAddressField(default="NA")
	Boombarrier = models.GenericIPAddressField(default="NA")
	Tolluser = models.GenericIPAddressField(default="NA")
	Overall_Health = models.GenericIPAddressField(default="NA")
	Camera = models.GenericIPAddressField(default="NA")
	User_Name = models.CharField(default = "NA",max_length=100)
	Location = models.CharField(default = place,max_length=100)
	Direction = models.CharField(default = "NA",max_length=100)
	Status =  models.IntegerField(default=0)
	Timestamp = models.DateTimeField(default=datetime.now())


class Ping(models.Model):
	Lane_Number = models.IntegerField(default=0)
	Webapp = models.CharField(default = "NA",max_length=200)
	Anpr = models.CharField(default = "NA",max_length=200)
	Profiler =models.CharField(default = "NA",max_length=200)
	Weighbridge = models.CharField(default = "NA",max_length=200)
	Boombarrier = models.CharField(default = "NA",max_length=200)
	Tolluser = models.CharField(default = "NA",max_length=200)
	Overall_Health = models.CharField(default = "NA",max_length=200)
	Camera = models.CharField(default = "NA",max_length=200)
	User_Name = models.CharField(default = "NA",max_length=100)
	Location = models.CharField(default = place,max_length=100)
	Status =  models.IntegerField(default=0)
	Timestamp = models.DateTimeField(default=datetime.now())
	
	
class Login_Time(models.Model):	
	User_Name = models.CharField(default="NA",max_length=200)
	Lane_Number = models.CharField(default = "NA",max_length=200)
	Direction = models.CharField(default = "NA",max_length=200)
	Login_Time =  models.CharField(default="NA",max_length=200)
	Logout_Time = models.CharField(default="NA",max_length=200)

class Configure (models.Model):
	Lane_Number = models.CharField(default = "NA",max_length=200)
	Direction = models.CharField(default = "NA",max_length=200)
	Location = models.CharField(default = "NA",max_length=200)
	Vehicle_Class = models.CharField(default = "NA",max_length=200)







