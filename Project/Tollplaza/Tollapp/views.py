
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib import messages
from Tollapp.models import *
from django.shortcuts import render
from time import time,strftime,gmtime

from django.contrib.sessions.models import Session
import os
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Permission, User
import unicodedata
import MySQLdb
import barcode
import PIL
from PIL import Image, ImageWin
from barcode.writer import ImageWriter
import random
import md5
from django.contrib.auth.hashers import MD5PasswordHasher
from django.shortcuts import redirect
from datetime import datetime as Datetime
import datetime
from .forms import  LoginForm
import threading
from time import sleep
from datetime import date
from dateutil.rrule import rrule, DAILY
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#locale is used  for adding comma to digits
import locale

def nano_login_required(function):
	def inner(request,*args, **kwargs):
		''' Login decorator creating using sessions '''
		if not  request.session.has_key('User_Name'):
			return redirect("/")

		return function(request,*args, **kwargs)
		
	return inner
	
def mainpage(request):
	''' this function is used for displaying login page'''
	form = LoginForm()
	return render_to_response('Login/login.html',{'form':form})


def display_homepage(request):
	
	try:
		''' Login form for the user it will go the form.py file and then based on user type page will be redirected.'''	
		if request.method=="POST":
			
			form =LoginForm(request.POST or None)
			'''form validation inside checking for that user is valid or not'''
			if form.is_valid():
				User =form.cleaned_data['username']
				password=form.cleaned_data['password']
				
				time = Datetime.now()
				
				''' session id is created '''
				request.session['User_Name']=User
				
				
				
			
				if Signup.objects.filter(User_Name=User).exists():
					
					data=Signup.objects.filter(User_Name=User)
					for d in data:
						user_type = d.User_Type
						lane = d.Lane_Number
						
					''' it will redirect based on user type '''	
					
					#if USER_TYPE = 'USER' ====> TOLL_USERPAGE
					if user_type == "user":											
						instance=Signup.objects.get(User_Name=User).Password
						
						''' password verification'''
						
						if  password==instance :
					
							lanee = Signup.objects.filter(User_Name = User)
							for l in lanee:
								lane_num = l.Lane_Number
							
							
							flaag = Edit_Lane.objects.filter(Lane_Number = lane_num)
							for f in flaag:
								flag = f.Flag
								name = f.User_Name
								LANE = f.Lane_Number
								toll_number=f.Lane_Number
								toll_dir=f.Direction
								toll_loc=f.Location					
								cam=f.Anpr_Ip
								cam1=f.Camera_Ip
							
							''' 
								flag is placed in edit_lane table for to avoid lane and user collision and authentication 
								if falg = 0 and user_name = 'NA' only tolluser will allow to login 
							
							'''
							
							if flag == 0 and name == "NA":
								
								login = time.strftime('%d''-''%m''-''%Y' ' ' '%H'':''%M'':''%S')
								
								d = Login_Time(User_Name=User,Lane_Number=toll_number,Direction=toll_dir,Login_Time = login)
								d.save()
								''' new Transaction with default value entry created in MAIN TABLE '''
								
								my_data1 = Main(User_Name=User,Lane_Number=toll_number,Direction=toll_dir,Location=toll_loc,Pollution=Datetime.now(),Fitness=Datetime.now(),Permit=Datetime.now(),Timestamp=Datetime.now(),Registration_Date=Datetime.now(),Tax=Datetime.now(),Insurance=Datetime.now(),National_Permit=Datetime.now(),Authorization=Datetime.now(),)
								my_data1.save()
								
								'''update User Name in Edit lane table while user login'''
					
								d = Edit_Lane.objects.filter(Lane_Number = LANE ).update(User_Name = User,Flag = True)
								#'''
									#snapshot code
								
								
								#my_data2=Main.objects.filter(Lane_Number=toll_number).order_by('-Timestamp')[0]
								#tran=my_data2.Transaction_Id
								
								#snapshot=str(tran)+'-'+'1'+".png"
								#path = os.getcwd() + r'//media_san//snapshot//'+ snapshot
								#os.system("ffmpeg  -i http://admin:12345@192.168.30.15/axis-cgi/mjpg/video.cgi -vframes 1 -q:v 2  %s"%path)
								#my_data3=Main.objects.filter(Lane_Number=toll_number).order_by('-Timestamp')[0]
								
								#my_data3.Image_1='/media_san/snapshot/'+snapshot
								#my_data3.save()
								#'''
								
								return render_to_response("Tolluser/userpage_first.html",{"lane_N":toll_number,"toll_dir":toll_dir,"toll_loc":toll_loc,"User_Name":User,"Password":password,"cam":cam,"cam1":cam1,})
								response.set_cookie('logged_in_mango_status', User)
								return response	
								
								
								
							else:	
								msg = "lane Number"+" " +str(lane)+" "+"is already in use by User"+" "+str(User)
								return render_to_response("Login/login.html",{'flag':msg})
						else:
							msg="Password is Invalid!!"
							return render_to_response('Login/login.html',{'flag':msg})
					
				
					
						
						
					
						
					elif user_type == "officer":
						instance=Signup.objects.get(User_Name=User).Password
						loc = Signup.objects.get(User_Name=User).Location
						
						if password==instance:
							my=Signup.objects.get(User_Name=User)																		
							return render_to_response('Officer/officer.html',{"User_Name":User,"Password":password,"loc":loc})
				
						else:
							msg="Password is Invalid!!"
							return render_to_response("Login/login.html",{'flag':msg})
							
							
					elif user_type == "transport":
						instance=Signup.objects.get(User_Name=User).Password
						if password==instance:
							return redirect ('/report')
						else:
							msg="Password is Invalid"
							return render_to_response("Login/login.html",{'flag':msg})
						
							
					elif user_type == "admin":
						instance=Signup.objects.get(User_Name=User).Password
						if password==instance:
							return render_to_response("Admin/Admin.html",{"User_Name":User,"Password":password})
						else:
							msg="password will be invalid!"
							return render_to_response("Login/login.html",{'flag':msg})
							
						
							
					elif user_type == "monitor" :	
						'''
						if USERTYPE IS MONITOR
						'''	
						instance=Signup.objects.get(User_Name=User).Password		
						if password==instance:		
							return redirect('/display')		
						else:		
							msg="password will be invalid!"		
							return render_to_response("Login/login.html",{'flag':msg})								
					

					else:
						msg="USER TYPE IS INVALID"
						return render_to_response("Login/login.html",{'flag':msg})
																
						
				else:
						msg="Username is invalid!"
						return render_to_response("Login/login.html",{'flag':msg})
			else:
				form=form
				return render_to_response("Login/login.html",{'form':form})			
			
		else:
			return redirect("/")	
	except:
		msg="Please Enter Correct User Name and Password"
		return render_to_response("Login/login.html",{'flag':msg})
		
#@nano_login_required
def ANPR(request):

	'''ANPR Method for just  getting the vehicle number from anpr table'''
	try:
		if request.session.has_key('User_Name'):
			User_Name=request.POST['User_Name']
			password=request.POST['Password']
			lan = Signup.objects.filter(User_Name = User_Name)
			for u in lan:
				lanee = u.Lane_Number
			
			d = Edit_Lane.objects.filter(Lane_Number = lanee).update(User_Name = User_Name)
			e = Edit_Lane.objects.filter(Lane_Number = lanee)
			for i in e:
				toll_number = i.Lane_Number
				toll_dir = i.Direction
				toll_loc = i.Location
			
				cam=i.Anpr_Ip
				cam1=i.Camera_Ip
				
				
			try:
	
				data=Anpr.objects.filter(Lane_Number=toll_number).order_by('Flag','Timestamp')[0]
				if data.Flag==0:
					Vehicle_Number=data.Vehicle_Number
				else:
					Vehicle_Number="NULL"
			except:
				Vehicle_Number="NULL"
			
			return render_to_response("Tolluser/userpage_first.html",{'Vehicle_Number':Vehicle_Number,'User_Name':User_Name,"Password":password,"lane_N":toll_number,"toll_dir":toll_dir,"toll_loc":toll_loc,"cam":cam,"cam1":cam1})

	except:
		return redirect("/")	
			
		




#@nano_login_required
def get_details(request):
	if  request.session.has_key('User_Name'):
		
		'''
			get_details method used for search vehicle number into the rto central database and display 
			the result of vehicle and axle count,sensor details(height,width,length),weight bridge details 
			are getting from hardware device
		'''
		if request.method=="POST":
			try:
				
				username =request.session['User_Name']
				value = Signup.objects.filter(User_Name = username )
				for v in value:
					lane = v.Lane_Number
					
				value1 = Edit_Lane.objects.filter(Lane_Number = lane)
				for e in value1:
					user = e.User_Name
					direction = e.Direction
					loc = e.Location
				Number=request.POST["Vehicle_Number"]
				User_Name=request.POST["User_Name"]
				password=request.POST["Password"]
				
				
				'''
					from ANPR WE GET VEHICLE NUMBER and search IN rto database and get required RTO DETAILS 
				'''
				data1=Rto.objects.filter(Vehicle_Number=Number)
				if (data1):	
					for data in data1:
						if  data.Vehicle_Number==Number:
							veh_no=data.Vehicle_Number
							Die_h=data.Dimension_Height
							Pol_va=data.Pollution
							Per_va=data.Permit
							Fit_va=data.Fitness
							Die_l=data.Dimension_Length
							Die_h=data.Dimension_Height 
							Die_b=data.Dimension_Breadth
							axle_d =data.Axle							
							Veh_cla=data.Vehicle_Class
							reg=data.Registration_Date
							fuel=data.Vehicle_Fuel_Type
							cubic=data.Engine_Cubic_Capacity
							chassis=data.Chassis_Number
							engine=data.Engine_Number
							national=data.National_Permit
							tax=data.Tax
							Authorization=data.Authorization
							Vehicle_Type=data.Vehicle_Type
							insurance=data.Insurance
							Unladen_Weight=data.Unladen_Weight
							
							
							
							'''
								Lane Number,Location,Direction,ANPR,CAMERA IP get from SIGNUP and EDIT LANE
							'''
							lane = Signup.objects.get(User_Name = User_Name).Lane_Number	
							my_data=Edit_Lane.objects.filter(Lane_Number=lane)
							for i in my_data:
								toll_number=i.Lane_Number
								cam=i.Anpr_Ip
								cam1=i.Camera_Ip
								 
								add = i.Location
								toll_loc = i.Location
								toll_dir = i.Direction
							l1=[]
							l2=[]
							
							try:
								
								'''
									SENSOR DETAILS and update FLAG TO 1 
								'''
								x=Sensor_Details.objects.filter(Lane_Number=toll_number).order_by('Flag','Timestamp')[0]
								if x.Flag==0:
									Sensor_Height=x.Dimension_Height
									Sensor_Breadth=x.Dimension_Breadth
									Sensor_Length=x.Dimension_Length
									x.Flag='True'
									x.save()
									
								else:
									Sensor_Height = "-0"
									Sensor_Breadth = "-0"
									Sensor_Length = "-0"
									msg="Sensor details are not came!"
									
									l1.append(msg)
							except:
								Sensor_Height= "-0"
								Sensor_Breadth= "-0"
								Sensor_Length= "-0"
								msg1="sensor table is empty!"
								
								l2.append(msg1)
							try:	
								
								''' 
									WEIGHBRIDGE DETAILS and update FLAG TO 1 
								'''
								data1=Weigh_Bridge.objects.filter(Lane_Number=toll_number).order_by('Flag', 'Timestamp')[0]
								if data1.Flag==0:
									Weight=data1.Weight
									laden = Weight - Unladen_Weight
									data1.Flag='True'
									data1.save()
									color_weight = "white"
									
								else:
									Weight= "-0"
									msg="weight bridge details are not came!"
									
									l1.append(msg)
									if Weight == "-0":
										laden = 0
										color_weight = "grey"
								
									
							except:
								Weight= "-0"
								msg1="Weigh bridge table is empty!"
								
								l2.append(msg1)
							
							try:
								
								''' 
									AXLE COUNT and update FLAG TO 1 
								
								'''
								obj=Axle_Count.objects.filter(Lane_Number=toll_number).order_by('Flag','Timestamp')[0]
								if obj.Flag==0:
									axle_a=obj.Axle
									obj.Flag='True'
									obj.save()
									
								else:
									axle_a= "-0"
									msg="Axle count details are not came!"
									
									l1.append(msg)
							except:
								axle_a="-0"
								msg1="Axle count table is empty!"
								
								l2.append(msg1)
								
							''' 
								filter by lane number and transaction id and update all details in MAIN TABLE 
							
							'''	
							m=Main.objects.filter(Lane_Number=toll_number).order_by('-Timestamp')[0]
								
							
							Transaction=m.Transaction_Id
							
							if toll_number:
								Main.objects.filter(Lane_Number=toll_number,Transaction_Id=Transaction).update(Vehicle_Number=Number,Dimension_Length=Die_l,Dimension_Height=Die_h,Dimension_Breadth=Die_b,Sensor_Axle = axle_a,Sensor_Length =Sensor_Length,Sensor_Breadth=Sensor_Breadth,Sensor_Height=Sensor_Height,Fitness=Fit_va,Permit=Per_va,Pollution=Pol_va,Axle=axle_d,Registration_Date=reg,
											Tax=tax,Authorization=Authorization,Insurance=insurance,National_Permit=national,Engine_Number=engine,Chassis_Number=chassis,Vehicle_Class=Veh_cla,Vehicle_Fuel_Type=fuel,Engine_Cubic_Capacity=cubic,Laden_Weight=laden,Unladen_Weight=Unladen_Weight,Vehicle_Type=Vehicle_Type,Weight=Weight)							
								''' 
									below code is used to generate BARCODE in PNG format
								
								'''
								
											
								tran=str(Transaction)
								
								filenames=tran+".png"
								path = os.getcwd() + r'//media_san//barcode//'+ tran
								
								ean = barcode.get('code39', tran , writer=ImageWriter())
								filename= ean.save(path)
								try:
								
									'''
										UPDATE ANPR TABLE  FLAG FROM 0 TO 1 
																			
									'''
									
									data=Anpr.objects.filter(Lane_Number=toll_number).order_by('Flag','Timestamp')[0]
								
									data.Flag='True'
									data.Vehicle_Number = Number
									data.save()
								except:
									pass	
								
								date=Datetime.now().strftime("%Y-%m-%d")
								
								current_page=Datetime.now() 
								'''
									all sensor details is compare with rto details and 
									RTO validity date is check with current date is check produce output as (OK or NOT OK status )
									
								'''
								
								sta=""
								permit = ""
								
								if Sensor_Height =="-0" or Sensor_Breadth =="-0" or Sensor_Length =="-0" or axle_d == "-0":
									permit = "PERMIT"
									
									if date<=str(national) and date<=str(insurance) and date<=str(Authorization) and date<=str(Pol_va)  and date<=str(Fit_va) and date<=str(Per_va) and date<=str(tax):
										sta = "OK"
										
									else:
										sta = "NOTOK"
										permit = "DENIED"
										
								
	
								elif Die_h>=Sensor_Height and Die_b>=Sensor_Breadth and Die_l>=Sensor_Length and axle_a<=axle_d and date<=str(national) and date<=str(insurance) and date<=str(Authorization) and date<=str(Pol_va)  and date<=str(Fit_va) and date<=str(Per_va) and date<=str(tax):
									sta="OK"
									permit = "PERMIT"
									
								else:
									sta="NOTOK"
									permit = "DENIED"
									
															
								'''  
									color validation (red or green) for date
								
								'''
								
								if date<=str(Pol_va):
									color1="green"
								else:
									color1="red"
									
								if date<=str(Per_va) : 
									color2="green"
								else:
									color2="red"
								
								if date<=str(Fit_va):
									color3="green"
								else:
									color3="red"
									
								if date<=str(national):
									color4="green"
								else:
									color4="red"
									
								if date<=str(tax):
									color5="green"
								else:
									color5="red"
									
									
								if date<=str(Authorization):
									color6="green"
								else:
									color6="red"
									
									
								if date<=str(insurance):
									color7="green"
								else:
									color7="red"
									
								
								
								''' 
									color validation (red or green or grey) for sensor details
								
								'''
								
								if Sensor_Height == "-0":
									color8 = "grey"
								elif Sensor_Height<=Die_h:
									color8="green"
								else:
									color8="red"
									
								if Sensor_Breadth == "-0":
									color9="grey"
								elif Sensor_Breadth<=Die_b:
									color9="green"
								else:
									color9="red"
									
								if Sensor_Length == "-0":
									color10 = "grey"
								elif Sensor_Length<=Die_l:
									color10="green"
								else:
									color10="red"
								
									
								if axle_a == "-0":
									color11 = "grey"
								elif axle_a <= axle_d:
									color11 = "green"
								else:
									color11 = "red"
								
								if Sensor_Height == "-0":
									h = "-0"
								else:	
									height = Sensor_Height - Die_h
									height_h = "+" + str(height)
									if height <=0:
										h = 0
									else:
										h = height_h
								if Sensor_Length == "-0":
									l = "-0"
								else:
									length = Sensor_Length  - Die_l
									length_l = "+" + str(length)
									if length <=0:
										l = 0
									else:
										l = length_l
								if 	Sensor_Breadth == "-0":
									w = "-0"
								else:
									width = Sensor_Breadth - Die_b
									width_w = "+" + str(width)
									if width <=0:
										w = 0
									else:
										w = width_w
								if axle_a == "-0":
									a = "-0"
								else:
									Axle = axle_a - axle_d
									Axle_a = "+" + str(Axle)
									if Axle <=0:
										a = 0
									else:
										a = Axle_a
								
								
								''' All error msg are listed '''	
									
								
								
								ms=",".join(l1[0:])
								ms1=",".join(l2[0:])
								
								
								comments = str(ms) +","+ str(ms1)
								Main.objects.filter(Transaction_Id=Transaction).update(Comment = comments,Vehicle_Status=sta,Status = permit)
								
								if l1 == []:
									if l2 == [] :
										msg_color = ""
										
									else:
										msg_color = "center"
										
								else:
									msg_color = "center"
									
								
								
								return render_to_response('Tolluser/userpage_second.html',{"permit":permit,"Lane_Number":lane,"msg_color":msg_color,"color_weight":color_weight,'flag':ms,'flag1':ms1,"w":w,"a":a,"l":l,"h":h,"color1":color1,"color2":color2,"color3":color3,"color4":color4,"color5":color5,"color6":color6,"color7":color7,"color8":color8,"color9":color9,"color10":color10,"color11":color11,"ladden":laden,"Unladen_Weight":Unladen_Weight,"filenames":filenames,"sta":sta,
																		"current_date":current_page,"Diemension_h":Die_h,"Vehicle_Number":veh_no,"Pollution_va":Pol_va,"Permit_va":Per_va,"Fitness_va":Fit_va,"Diemension_l":Die_l,"Diemension_b":Die_b,
																		"axle_a":axle_a,"axle_d":axle_d ,"Vehicle_Status":sta,"Transaction_Id":tran,"Vehicle_class":Veh_cla,"lane_N":toll_number,
																		"sensor_h":Sensor_Height,"sensor_b":Sensor_Breadth,"sensor_le":Sensor_Length ,"address":add,"Weight":Weight,"registration_date":reg,"fuel":fuel,"toll_loc":toll_loc,"Vehicle_Type":Vehicle_Type,
																		"cubic":cubic,"Chassis_Number":chassis,"Engine_Number":engine,"national":national,"tax":tax,"Authorization":Authorization,"filename":filename,"insurance":insurance,"toll_dir":toll_dir,"Vehicle_Type":Vehicle_Type,"User_Name":User_Name,"Password":password,"cam":cam,"cam1":cam1})

							else:
								msg="No Vehicles Are In Que!!"
								clas = "center"
								return render_to_response("Tolluser/userpage_second.html",{'flag':msg,'clas':clas})

						else:
							msg="Please enter a valid Vehicle Transaction_ID!!!!"
							clas = "center"
							return render_to_response('Tolluser/userpage_second.html',{'flag':msg,'clas':clas})
				else:
					msg="Please search with valid number!"
					clas = "center"
					return render_to_response("Tolluser/Tolluser/userpage_first.html",{'clas':clas,'flag':msg,"User_Name":user,"lane_N":lane,"toll_dir":direction,"toll_loc":loc})

			except:
				msg="Please enter Vehicle Number after Next"
				clas = "center"
				return render_to_response("Tolluser/userpage_second.html",{'flag':msg,'clas':clas})
	else:
		msg="Your session will be anothorized"
		return render_to_response("Login/login.html",{'flag':msg})


def Userpage_update(request):
	'''this method for the updation of vehicle status purpose.'''
	if request.session.has_key('User_Name'):
		try:
			
			
			permission = request.POST['permit']
			filenames = request.POST['barcode']
			Transaction = request.POST['Transaction']
			number = request.POST['vehicle_number']
			lane = request.POST['lane']
			v_class = request.POST['class']
			
			
			h = request.POST['height']
			w = request.POST['width']
			l = request.POST['length']
			a = request.POST['axle']
			weig = request.POST['weight']
			color8 = request.POST['color_h']
			color9 = request.POST['color_w']
			color10 = request.POST['color_l']
			color11 = request.POST['color_a']
			color_weig = request.POST['color_weig']
			
			
			Main.objects.filter(Transaction_Id = Transaction,Vehicle_Number = number,Lane_Number = lane ).update(Vehicle_Class = v_class,Status = permission)
			msg = "Updated Successfully!!!!!!"
			color = "green"
			
			
			final = Main.objects.filter(Transaction_Id = Transaction,Vehicle_Number = number,Lane_Number = lane)
			for i in final:
				tran = i.Transaction_Id
				Vehicle_Number = i.Vehicle_Number
				Vehicle_Status = i.Vehicle_Status
				permit = i.Status
				Vehicle_class = i.Vehicle_Class
				registration_date = i.Registration_Date
				Vehicle_Type = i.Vehicle_Type
				Chassis_Number = i.Chassis_Number
				cubic = i.Engine_Cubic_Capacity
				Engine_Number = i.Engine_Number
				fuel = i.Vehicle_Fuel_Type
				Pollution_va = i.Pollution
				Permit_va = i.Permit
				Fitness_va = i.Fitness
				national = i.National_Permit
				tax = i.Tax
				Authorization = i.Authorization
				insurance = i.Insurance
				Weight = i.Weight
				ladden = i.Laden_Weight
				Unladen_Weight = i.Unladen_Weight
				axle_a = i.Sensor_Axle
				sensor_b = i.Sensor_Breadth
				sensor_h = i.Sensor_Height
				sensor_le = i.Sensor_Length
				Diemension_b = i.Dimension_Breadth
				Diemension_h = i.Dimension_Height
				Diemension_l = i.Dimension_Length
				axle_d = i.Axle
				lane_N = i.Lane_Number
				toll_loc = i.Location
				toll_dir = i.Direction
				User_Name = i.User_Name
				
			current_date = Datetime.now()
			
			date=Datetime.now().strftime("%Y-%m-%d")
			if date<=str(Pollution_va):
				color1="green"
			else:
				color1="red"
				
			if date<=str(Permit_va) : 
				color2="green"
			else:
				color2="red"
			
			if date<=str(Fitness_va):
				color3="green"
			else:
				color3="red"
				
			if date<=str(national):
				color4="green"
			else:
				color4="red"
				
			if date<=str(tax):
				color5="green"
			else:
				color5="red"
				
				
			if date<=str(Authorization):
				color6="green"
			else:
				color6="red"
				
				
			if date<=str(insurance):
				color7="green"
			else:
				color7="red"
									
			
			
			msg = " Successfully Updated !!!!!! "
			color_success = "success"
			
			return render_to_response('Tolluser/userpage_second.html',{"color_success":color_success,"success":msg,"w":w,"a":a,"l":l,"h":h,"Weight":weig,"color1":color1,"color2":color2,"color3":color3,"color4":color4,"color5":color5,"color6":color6,"color7":color7,"color8":color8,"color9":color9,"color10":color10,"color11":color11,"color_weight":color_weig,'filenames':filenames,'Transaction_Id':tran,'current_date':current_date,'Vehicle_Number':Vehicle_Number,'Vehicle_Status':Vehicle_Status,'permit':permit,'Vehicle_class':Vehicle_class,
										'registration_date':registration_date,'Vehicle_Type':Vehicle_Type,'Chassis_Number':Chassis_Number,'cubic':cubic,
										'Engine_Number':Engine_Number,'fuel':fuel,'Pollution_va':Pollution_va,'Permit_va':Permit_va,'Fitness_va':Fitness_va,
										'national':national,'tax':tax,'Authorization':Authorization,'insurance':insurance,'ladden':ladden,
										'Unladen_Weight':Unladen_Weight,'Diemension_b':Diemension_b,
										'Diemension_h':Diemension_h,'Diemension_l':Diemension_l,'axle_d':axle_d,'lane_N':lane_N,'Lane_Number':lane_N,'toll_loc':toll_loc,
										'toll_dir':toll_dir,'User_Name':User_Name})	
			
		except:
			return render_to_response('Login/login.html')
	else:
		return redirect('/')
		
		
#@nano_login_required
def logout(request):
	'''this method used for the logout and session will be deleted'''
	try:
		user = request.session['User_Name']
	
		''' update USER NAME -> NA and FLAG -> 0'''
		m = Edit_Lane.objects.filter(User_Name = user).update(User_Name = "NA",Flag = False)
		
		#calculate LOGOUT TIME
		time_out = Datetime.now()
		logout = time_out.strftime('%d''-''%m''-''%Y' ' ' '%H'':''%M'':''%S')
		''' UPDATE LOGOUT TIME to login_Time table'''
		d = Login_Time.objects.filter(User_Name = user,Logout_Time = "NA").update(Logout_Time = logout)
		
	except:
		pass
	form=LoginForm()
	
	return render_to_response("Login/login.html",{'form':form})

#edit_property for officer gui
#@nano_login_required
def edit_property(request):
	'''edit property under officer gui side for just entering transaction_id based on that it will go to our local database and display the vehicle details'''
	if request.session.has_key('User_Name'):
			
		try:
			Number=request.POST['transaction']
			User_Name=request.session['User_Name']
			password=request.POST['Password']
			
			
			lo = Signup.objects.filter(User_Name = User_Name)
			for i in lo:
				loc = i.Location
			
			data2=Main.objects.filter(Transaction_Id=Number)
			
			if (data2):
				for data in data2:
					
					
					if data.Transaction_Id == Number:
					
						Trans=data.Transaction_Id
						
						
						veh_no=data.Vehicle_Number
						Per_va=data.Permit
						pollut=data.Pollution
						die_l=data.Dimension_Length
						die_h=data.Dimension_Height
						die_b=data.Dimension_Breadth
						Fitness=data.Fitness
						office=data.Officer_Name
						Time=data.Timestamp
						user=data.User_Name
						Axle=data.Axle
						lane=data.Lane_Number
						add=data.Location
						direction = data.Direction
						Weight=data.Weight
						veh_class=data.Vehicle_Class
						regis=data.Registration_Date
						chassis=data.Chassis_Number
						engine=data.Engine_Number
						fuel=data.Vehicle_Fuel_Type
						cubic=data.Engine_Cubic_Capacity
						national=data.National_Permit
						insurance=data.Insurance
						Authorization=data.Authorization
						tax=data.Tax
						Unladen_Weight=data.Unladen_Weight
						amount=data.Fine_Amount
						
						ok_status = data.Vehicle_Status
						permit_status = data.Status
						comm = data.Comment
						Main.objects.filter(Transaction_Id=Number).update(Officer_Name=User_Name)
						Sensor_Height=data.Sensor_Height
						Sensor_Breadth=data.Sensor_Breadth
						Sensor_Length =data.Sensor_Length 
						Sensor_Axle = data.Sensor_Axle
						Vehicle_Type=data.Vehicle_Type
	
						
						date=Datetime.now().strftime("%Y-%m-%d")
						current_page=Datetime.now()
								
						
						''' claculate LADEN WEIGHT '''
						ladden=Weight-Unladen_Weight
						
						'''
							COLOR VALIDATION [green or red] sensor details compare with RTO details 
						'''
						
						
							
						if Sensor_Height<=die_h:
							color4="green"
						else:
							color4="red"
							
						if Sensor_Length <=die_l:
							color5="green"
						else:
							color5="red"
						if Sensor_Breadth<=die_b:
							color6="green"
						else:
							color6="red"
						if Sensor_Axle<=Axle:
							color="green"
						else:
							color="red"
							
						''' 
							COLOR VALIDATION [green or red]VALIDITY DATE compare with CURRENT DATE 
						
						'''
						if date<=str(Per_va) : 
							color1="green"
						else:
							color1="red"
						
						if date<=str(pollut):
							color2="green"
						else:
							color2="red"
						if date<=str(Authorization):
							color3="green"
						else:
							color3="red"
						
						
						if date<=str(national):
							color7="green"
						else:
							color7="red"
						if date<=str(Fitness):
							color8="green"
						else:
							color8="red"
						if date<=str(tax):
							color9="green"
						else:
							color9="red"
						if date<=str(insurance):
							color10="green"
						else:
							color10="red"
							
						''' 
							SENSOR DAETILS value lesser than rto print value [0] else print [+value]
						
						'''
	
						height = Sensor_Height - die_h
						height_h = "+" + str(height)
						if height <=0:
							h = 0
						else:
							h = height_h
	
						length = Sensor_Length - die_l
						length_l = "+" + str(length)
						if length <=0:
							l = 0
						else:
							l = length_l
						width = Sensor_Breadth - die_b
						width_w = "+" + str(width)
						if width <=0:
							w = 0
						else:
							w = width_w
	
						axle = Sensor_Axle - Axle
						Axle_a = "+" + str(axle)
						if axle <=0:
							a = 0
						else:
							a = Axle_a
							
						clas = ""
						'''
							BARCODE GENERATED FOR OFFICER
						'''
						tran =  Number
						filenames=tran+".png" 
						path = os.getcwd() +r'//media_san//barcode//'+tran
						
						from barcode.writer import ImageWriter
						ean = barcode.get('code39', tran , writer=ImageWriter())
						filename= ean.save(path)
						
						
						
						return render_to_response('Officer/officer.html',{"clas":clas,"direction":direction,"comm":comm,"ok_status":ok_status,"permit_status":permit_status,"loc":loc,"a":a,"w":w,"l":l,"h":h,"color1":color1,"color2":color2,"color3":color3,"amount":amount,
											"current_date":current_page,"filenames":filenames,"ladden":ladden,"Unladen_Weight":Unladen_Weight,"Sensor_Axle":Sensor_Axle,
											"Vehicle_Number":veh_no,"RTO":User_Name,"Timestamp":Time,"Axle_Count":Axle,"Pollution_va":pollut,
											"Fitness_va":Fitness,"registration":regis,"chassis":chassis,"Tollbooth_user":user,"Transaction_ID":Trans,
											"lane_N":lane,"Permit":Per_va,"Weight":Weight,"Diemension_h":die_h,"engine":engine,"fuel":fuel,"cubic":cubic,
											"color":color,"national":national,"insurance":insurance,"Authorization":Authorization,"tax":tax,"Diemension_b":die_b,
											"Diemension_l":die_l,"address":add,"Vehicle_Type":Vehicle_Type,"Vehicle_class":veh_class,"sensor_h":Sensor_Height,
											"sensor_b":Sensor_Breadth,"sensor_le":Sensor_Length ,"color4":color4,"color5":color5,"color6":color6,"color7":color7,
											"color8":color8,"color9":color9,"color10":color10,"tran":tran,"User_Name":User_Name,"trans_id":Number,"Password":password})
		
			else:
				msg="Please Enter Valid Vehicle Transaction ID"
				lo = Signup.objects.filter(User_Name = User_Name)
				for i in lo:
					loc = i.Location
				clas = "center"
				return render_to_response("Officer/officer.html",{"flag":msg,"clas":clas,"loc":loc,"User_Name":User_Name})
		
		except:
			msg="your session is been closed"
			clas = "center"
			return render_to_response("Login/login.html",{"flag":msg,"clas":clas})
	else:
		return redirect("/")



#@nano_login_required

def save_edit_property(request):
		
	if request.session.has_key('User_Name'):
		
		try:
			'''
				this method used for extension of permit validity and fine amount collecting will be update to our local database,
				comments(permit,crime related comment) and barcode also generated.
			'''
			User_Name=request.session["User_Name"]
			lo = Signup.objects.filter(User_Name = User_Name)
			for i in lo:
				loc = i.Location
			
			password=request.POST['Password']
			
			''' 
				UPDATE DETAILS FROM OFFICER GUI 
			'''
			
			Permit=request.POST["Permit"]
			
			amount=request.POST["amount"]
			
			
			Vehicle_Number=request.POST["Vehicle_Number"]
			
			comments=request.POST["comments"]
			
			tran=request.POST["transaction"]
			
			
			permission = request.POST.get("permission")
			
			status=request.POST.get("status")
			
			vehicle_class=request.POST.get("class")
			
			
			
			
			''' 
				FILTER BY TRANSACTION ID  and UPDATE  all the edited avlues to MAIN TABLE 
			'''
			
			
			
			Main.objects.filter(Transaction_Id=tran).update(Status = permission, Permit=Permit,Fine_Amount=amount,Comment=comments,Vehicle_Status=status)
			
			filt = Main.objects.filter(Transaction_Id=tran)
			for x in filt:
				
				Per_va=x.Permit
				amount=x.Fine_Amount
				veh_no=x.Vehicle_Number
				die_l=x.Dimension_Length
				die_b=x.Dimension_Breadth
				die_h=x.Dimension_Height
				chassis=x.Chassis_Number
				engine=x.Engine_Number
				national=x.National_Permit
				insurance=x.Insurance
				tax=x.Tax
				
				ladden=x.Laden_Weight
				Unladen_Weight=x.Unladen_Weight
				comments=x.Comment
				regis=x.Registration_Date
				cubic=x.Engine_Cubic_Capacity
				add=x.Location
				fuel=x.Vehicle_Fuel_Type
				Weight=x.Weight
				office=x.Officer_Name
				Time=x.Timestamp
				Axle=x.Axle
				pollut=x.Pollution
				Fitness=x.Fitness
				user=x.User_Name
				Transaction=x.Transaction_Id
				lane=x.Lane_Number
				Authorization=x.Authorization
				Sensor_Height=x.Sensor_Height
				Sensor_Breadth=x.Sensor_Breadth
				Sensor_Length =x.Sensor_Length
				Sensor_Axle = x.Sensor_Axle
				veh_class=x.Vehicle_Class
				Direction=x.Direction
				vehicle_type=x.Vehicle_Type
				ok_status = x.Vehicle_Status
				permit_status = x.Status
			
			current_date=Datetime.now()
			
			
			''' calcute ladden weight '''
			
			ladden=Weight-Unladen_Weight
			
			''' 
				current date is calcute to check the rto validity date
			'''
			
			date=Datetime.now().strftime("%Y-%m-%d")
						
			
			
			'''
				COLOR VALIDATION [green or red] sensor details compare with RTO details 
			'''
			

			if Sensor_Height<=die_h:
				color4="green"
			else:
				color4="red"
			if Sensor_Length <=die_l:
				color5="green"
			else:
				color5="red"
			if Sensor_Breadth<=die_b:
				color6="green"
			else:
				color6="red"
			if Sensor_Axle<=Axle:
				color="green"
			else:
				color="red"	

			''' 
				COLOR VALIDATION [green or red]VALIDITY DATE compare with CURRENT DATE 
						
			'''			
			
			if date<=str(Per_va) : 
				color1="green"
			else:
				color1="red"
			
			if date<=str(pollut):
				color2="green"
			else:
				color2="red"
			if date<=str(Authorization):
				color3="green"
			else:
				color3="red"
		
			if date<=str(national):
				color7="green"
			else:
				color7="red"
			if date<=str(Fitness):
				color8="green"
			else:
				color8="red"
			if date<=str(tax):
				color9="green"
			else:
				color9="red"
			if date<=str(insurance):
				color10="green"
			else:
				color10="red"
				
			''' 
				SENSOR DAETILS value lesser than rto print value [0] else print [+value]
						
			'''	

			height = Sensor_Height - die_h
			height_h = "+" + str(height)
			if height <=0:
				h = 0
			else:
				h = height_h

			length = Sensor_Length  - die_l
			length_l = "+" + str(length)
			if length <=0:
				l = 0
			else:
				l = length_l
				
			width = Sensor_Breadth - die_b
			width_w = "+" + str(width)
			if width <=0:
				w = 0
			else:
				w = width_w

			axle = Sensor_Axle - Axle
			Axle_a = "+" + str(axle)
			if axle <=0:
				a = 0
			else:
				a = Axle_a

			'''
				BARCODE GENERATED FOR OFFICER
			'''
			tran=str(Transaction)
			filenames=tran+".png" 
			path = os.getcwd() +r'//media_san//barcode//'+tran
			
			from barcode.writer import ImageWriter
			ean = barcode.get('code39', tran , writer=ImageWriter())
			filename= ean.save(path)
			
			
			success = " Successfully Updated !!!!!! "
			color_success = "success"
			
			
			return render_to_response("Officer/officer.html",{'success':success,'color_success':color_success,"current_date":current_date,"permit_status":permit_status,"comm":comments,"ok_status":ok_status,"loc":loc,"a":a,"w":w,"l":l,"h":h,
														"color":color,"color1":color1,"color2":color2,"color3":color3,"color4":color4,"color5":color5,"color6":color6,"color7":color7,
														"color8":color8,"color9":color9,"color10":color10,"comments":comments,"amount":amount,"filenames":filenames,"ladden":ladden,"Vehicle_Type":vehicle_type,
														"Unladen_Weight":Unladen_Weight,"Vehicle_Number":veh_no,"RTO":office,"Timestamp":Time,"Axle_Count":Axle,
														"Pollution_va":pollut,"Fitness_va":Fitness,"registration":regis,"chassis":chassis,"Tollbooth_user":user,
														"trans_id":Transaction,"lane_N":lane,"Permit":Per_va,"Weight":Weight,"Diemension_h":die_h,"engine":engine,
														"fuel":fuel,"cubic":cubic,"national":national,"insurance":insurance,"Authorization":Authorization,"tax":tax,
														"Diemension_b":die_b,"Diemension_l":die_l,"address":add,"Vehicle_class":veh_class,"sensor_h":Sensor_Height,
														"sensor_b":Sensor_Breadth,"sensor_le":Sensor_Length ,"direction":Direction,"tran":tran,"User_Name":User_Name,"Password":password,})


		except:
			msg="Your values are not been updated Properly Please enter only Permit"
			
			return render_to_response("Officer/officer.html",{"flag":msg})
	else:
		return redirect("/")
		
#@nano_login_required
def officer (request):
	if request.session.has_key('User_Name'):
		user = request.session['User_Name']
		loc = Configure.objects.filter(id = 1)
		for ll in loc:
			location = ll.Location
			
		return render_to_response('Officer/officer.html',{"User_Name":user,"loc":location})
	else:
		return redirect("/")
		
# clear_page function for boombarrier
#@nano_login_required
def clear_page(request):
	'''this method is similar to display_homepage because this will be used for the  next vehicle number searching purpose and barrier gate will be opened''' 
	if request.session.has_key('User_Name'):
			
			
			User_Name = request.session['User_Name']		
				
			

			lan = Signup.objects.filter(User_Name = User_Name)
			for u in lan:
				lanee = u.Lane_Number
		
			
			my_data = Edit_Lane.objects.filter(Lane_Number = lanee)

		
			
			
			for i in my_data:
				
				
				toll_number = i.Lane_Number
				toll_dir = i.Direction
				toll_loc = i.Location
				cam=i.Anpr_Ip
				cam1=i.Camera_Ip
				
				
				
			''''	
				RELAY PANEL UPDATE FLAG 1 -> 0 >	
			'''
			if toll_number==1:
				
				a=Relay_Panel.objects.order_by('Lane_1')[0]
				a.Lane_1=False
				a.save()
			if toll_number==2:
				a=Relay_Panel.objects.order_by('Lane_2')[0]
				a.Lane_2=False
				a.save()
			if toll_number==3:
				
				a=Relay_Panel.objects.order_by('Lane_3')[0]
				a.Lane_3=False
				a.save()
			if toll_number==6:
				
				a=Relay_Panel.objects.order_by('Lane_6')[0]
				a.Lane_6=False
				a.save()
				
			
			li=[]
			l1=[]
			my_data1 = Main(User_Name=User_Name,Lane_Number=toll_number,Direction=toll_dir,Location=toll_loc,Pollution=Datetime.now(),Fitness=Datetime.now(),Permit=Datetime.now(),Timestamp=Datetime.now(),Registration_Date=Datetime.now(),Tax=Datetime.now(),Insurance=Datetime.now(),National_Permit=Datetime.now(),Authorization=Datetime.now())
			my_data1.save()
			
			
			response= render_to_response("Tolluser/userpage_first.html",{"lane_N":toll_number,"toll_dir":toll_dir,"toll_loc":toll_loc,"User_Name":User_Name,"cam":cam,"cam1":cam1,})
			response.set_cookie('logged_in_mango_status', User_Name)
			return response	
	else:
		return redirect("/")
		
#@nano_login_required
def report(request):
	'''this method will be for just displaying report details searching page'''
	if request.session.has_key('User_Name'):
		return render_to_response("Transport/report.html")
	else:
		return redirect("/")

def search_reports(request):
	'''this method for the searching vehicle within date range and based on username '''
	if request.session.has_key('User_Name'):
		try:
			
			date1 = request.POST["value1"]
			date2 = request.POST["value2"]
			pre = request.POST["previous"]
			next = request.POST["next"]
			
			
			if pre:
				
				page = pre
			elif next:
				
				page = next
			else:
				
				page = 1
			
			
			start = str(date1)
			end = str(date2)
			
			ca = date1.split('-')
			cb = date2.split('-')
			a = date(int(ca[0]),int(ca[1]),int(ca[2]))
			b = date(int(cb[0]),int(cb[1]),int(cb[2]))
			
			report = []
			data=Main.objects.filter(Timestamp__gte = date1,Timestamp__lte = date2)
			
				
			
			for i in data:
				timestamp=i.Timestamp.strftime("%Y-%m-%d")
				if  date1 <=timestamp<=date2:
						
			#<======= FROM DATE TO DATE ----- FOR LOOP =====================>
			#for dt in rrule(DAILY, dtstart=a, until=b):
			
				#final = dt.strftime("%Y-%m-%d")
				#result = Main.objects.filter(Timestamp__startswith = final).order_by(search)		
						
				#for i in result:
					
					data={}
					
					data['date'] = i.Timestamp
					data['fine']= i.Fine_Amount
					data['Vehicle_Number']= i.Vehicle_Number
					data['Vehicle_Status']= i.Vehicle_Status
					data['User_Name']= i.User_Name
					data['Transaction_Id']= i.Transaction_Id
					data['Lane_Number']= i.Lane_Number
					data['status'] = i.Status
					
					report.append(data)	
			
			''' pagination '''
			contact_list = report
			
			# Show 10 records per page
			paginator = Paginator(contact_list, 10) 
			
			try:
				contacts = paginator.page(page)
				
			except PageNotAnInteger:
				# If page is not an integer, deliver first page.
				contacts = paginator.page(1)
				
			except EmptyPage:
				# If page is out of range (e.g. 9999), deliver last page of results.
				contacts = paginator.page(paginator.num_pages)
				

					
			return render_to_response("Transport/report.html",{"date1":date1,"date2":date2,'contacts': contacts})
		except:
			
			return render_to_response("Transport/report.html")
	else:
		return redirect("/")
	
#@nano_login_required
def revenue(request):
	'''this method for displaying the empty html'''
	return render_to_response("Transport/revenue.html",{})
	
#@nano_login_required
def revenue_report(request):

	'''this method for revenue officer related document displaying based on date ranges within and sort by username,lanenumber like that.'''
	
	date1 = request.POST["value1"]
	date2 = request.POST["value2"]
	lane = request.POST["value3"]
	user = request.POST["value4"]
	
	
	import time
	from datetime import date, timedelta
	
	t=time.strptime(date2,'%Y-%m-%d')
	newdate=date(t.tm_year,t.tm_mon,t.tm_mday)+timedelta(1)
	date3 = newdate.strftime('%Y-%m-%d')
	
	
	
	ca = date1.split('-')
	
	
	cb = date2.split('-')
	gb = []
	report = []
	result = []
	type = []
	
	a = date(int(ca[0]),int(ca[1]),int(ca[2]))
	b = date(int(cb[0]),int(cb[1]),int(cb[2]))
	end  = int(cb[2])+1
	
	
	vehicle_type = Configure.objects.values('Vehicle_Class').order_by('Vehicle_Class').distinct()
	for v in vehicle_type:
		type.append(v['Vehicle_Class'])
		
	
	ty = len(type)
	
	if user == "ALL USER":
		y = Main.objects.filter(Timestamp__gte = date1,Timestamp__lte = date3,Lane_Number = lane).values('User_Name').order_by('User_Name').distinct()
		full_permit1 = Main.objects.filter(Timestamp__gte = date1,Timestamp__lte = date3 ,Lane_Number =lane,Vehicle_Status = "OK",Status = "PERMIT").count()
		
		locale.setlocale(locale.LC_ALL, '')
		full_permit = format(int(full_permit1), "n")
		
		full_ok1 = Main.objects.filter(Timestamp__gte = date1,Timestamp__lte = date3 ,Lane_Number =lane,Vehicle_Status = "OK",Status = "NA").count()
		
		locale.setlocale(locale.LC_ALL, '')
		full_ok = format(int(full_ok1), "n")
		
		full_denied1 = Main.objects.filter(Timestamp__gte = date1,Timestamp__lte = date3 ,Lane_Number =lane,Vehicle_Status = "NOTOK",Status = "DENIED").count()
		locale.setlocale(locale.LC_ALL, '')
		full_denied = format(int(full_denied1), "n")
		
		full_count1 = Main.objects.filter(Timestamp__gte = date1,Timestamp__lte = date3 ,Lane_Number =lane).count()
		locale.setlocale(locale.LC_ALL, '')
		full_count = format(int(full_count1), "n")
	
		
		total = Main.objects.filter(Timestamp__gte = date1,Timestamp__lte = date3 ,Lane_Number =lane).aggregate(Sum('Fine_Amount'))
		total_f = str(total.values()).replace("[","").replace("]","")
		
		if total_f == "None":
			total_fine = total_f
			
			#'''#adding comma in digits'''
		else:
			locale.setlocale(locale.LC_ALL, '')
			total_fine = format(int(total_f), "n")
		
		for i in y:
			result.append(i['User_Name'])
			
	
	else:
		result.append(user)
		full_permit1 = Main.objects.filter(Timestamp__gte = date1,Timestamp__lte = date3 ,Lane_Number =lane,User_Name = user,Vehicle_Status = "OK",Status = "PERMIT").count()
		locale.setlocale(locale.LC_ALL, '')
		full_permit = format(int(full_permit1), "n")
		
		full_ok1 = Main.objects.filter(Timestamp__gte = date1,Timestamp__lte = date3 ,Lane_Number =lane,User_Name = user,Vehicle_Status = "OK",Status = "NA").count()
		locale.setlocale(locale.LC_ALL, '')
		full_ok = format(int(full_ok1), "n")
		
		full_denied1 = Main.objects.filter(Timestamp__gte = date1,Timestamp__lte = date3 ,Lane_Number =lane,User_Name = user,Vehicle_Status = "NOTOK",Status = "DENIED").count()
		locale.setlocale(locale.LC_ALL, '')
		full_denied = format(int(full_denied1), "n")
		
		full_count1 = Main.objects.filter(Timestamp__gte = date1,Timestamp__lte = date3 ,Lane_Number =lane,User_Name = user).count()
		locale.setlocale(locale.LC_ALL, '')
		full_count = format(int(full_count1), "n")
		
		total = Main.objects.filter(Timestamp__gte = date1,Timestamp__lte = date3 ,Lane_Number =lane,User_Name = user).aggregate(Sum('Fine_Amount'))
		total_f = str(total.values()).replace("[","").replace("]","")
	
		
		if total_f == "None":
			total_fine = total_f
			
		#adding comma in digits
		else:
			locale.setlocale(locale.LC_ALL, '')
			total_fine = format(int(total_f), "n")
		
		
			
	for dt in rrule(DAILY, dtstart=a, until=b):
		
		final = dt.strftime("%Y-%m-%d")
			
		
		
			
		a = len(result)
	
		for u in range(0,a):
			result[u]
			
			
			
			for v in range(0,ty):
				type[v]
				
				data = {}
				
	
				bb = Main.objects.filter(Timestamp__startswith = final,Lane_Number =lane ,User_Name = result[u],Vehicle_Class = type[v],Vehicle_Status = "OK").count()
				aa = Main.objects.filter(Timestamp__startswith = final,Lane_Number =lane ,User_Name = result[u],Vehicle_Class = type[v],Vehicle_Status = "OK",Status = "PERMIT").count()
				cc = Main.objects.filter(Timestamp__startswith = final,Lane_Number =lane ,User_Name = result[u],Vehicle_Class = type[v],Vehicle_Status = "NOTOK",Status = "DENIED").count()
				jj = Main.objects.filter(Timestamp__startswith = final,Lane_Number =lane ,User_Name = result[u],Vehicle_Class = type[v]).count()
				ltv_fine = Main.objects.filter(Timestamp__startswith = final,Lane_Number =lane ,User_Name = result[u],Vehicle_Class = type[v]).aggregate(Sum('Fine_Amount'))
				f1 = str(ltv_fine.values()).replace("[","").replace("]","")
				
				if f1 == 'None':
					fine1 = f1
				else:
					
					locale.setlocale(locale.LC_ALL, '')
					fine1 = format(int(f1), "n")
			
				mm = Main.objects.filter(Timestamp__startswith = final,Lane_Number =lane ,User_Name = result[u]).aggregate(Sum('Fine_Amount'))
				f2 = str(mm.values()).replace("[","").replace("]","")
				
				if f2 == 'None':
					fine2 = f2
				else:
					
					locale.setlocale(locale.LC_ALL, '')
					fine2 = format(int(f2), "n")

				
				
				total_vehicle_count = Main.objects.filter(Timestamp__startswith = final,Lane_Number = lane,User_Name = result[u]).count()
				
				total_permit_con = Main.objects.filter(Timestamp__startswith = final,Lane_Number = lane,User_Name = result[u],Vehicle_Status = "OK",Status = "PERMIT").count()
				total_denied = Main.objects.filter(Timestamp__startswith = final,Lane_Number = lane,User_Name = result[u],Vehicle_Status = "NOTOK",Status = "DENIED").count()
				total_permit = total_permit_con - total_denied
				
				
				data['permit_lmvtr'] = aa
				data['ok_lmvtr'] = bb-aa
				data['notok_lmvtr'] = cc
				
				data['lmvtr'] =jj
				
				data['fine'] = fine2
				data['lane'] = lane
				data['user'] = result[u]
				data['type'] = type[v]
				
				data['date'] = final
				data['ltv_fine'] = fine1
				
				
				data['total_permit_con'] = total_permit_con
				data['total_denied'] = total_denied
				data['total_permit'] = total_permit
				data['total_vehicle_count'] = total_vehicle_count
				
				
				report.append(data)
				
	
		
		
		
			
	first = type[0]
	last = ty + 1
	
	return render_to_response("Transport/revenue.html",{'first':first,'last':last,'report':report,'date1':date1,'date2':date2,'lane':lane,'user':user,'full_permit':full_permit,'full_denied':full_denied,'full_ok':full_ok,'full_count':full_count,'total_fine':total_fine})
		
	
#@nano_login_required
def search(request):
	'''displaying the chart report of vehicle,tolluser details etc.'''
	return render_to_response("Transport/chart.html",{})
	
	
#@nano_login_required
def chart(request):
	#'''this method for the displaying chart related like graph format showed in html'''
	#try:
		
		date1=request.POST["value1"]
		date2=request.POST["value2"]
		
		
		vaues=str(date1)
		vaues1=str(date2)


		data=Main.objects.order_by('Timestamp')
	
		full = []
		ca = date1.split('-')
		cb = date2.split('-')
		
		n = Edit_Lane.objects.all()
		for l in n:
			lan = l.Lane_Number
			
				
			data = {}
			fine = Main.objects.filter(Timestamp__gte = datetime.date(int(ca[0]),int(ca[1]),int(ca[2])),Timestamp__lte = datetime.date(int(cb[0]),int(cb[1]),int(cb[2])),Lane_Number = lan).aggregate(Sum('Fine_Amount'))
			#convert fine amount to readable string
			lane_fine = str(fine.values()).replace("[","").replace("]","")
			
			# adding comma between digits
			if lane_fine == "None":
				fine_amount = lane_fine
			else:
				
				locale.setlocale(locale.LC_ALL, '')
				fine_amount = format(int(lane_fine), "n")
			permit = Main.objects.filter(Timestamp__gte = datetime.date(int(ca[0]),int(ca[1]),int(ca[2])),Timestamp__lte = datetime.date(int(cb[0]),int(cb[1]),int(cb[2])),Vehicle_Status = "OK",Lane_Number = lan).count()
			
			denied = Main.objects.filter(Timestamp__gte = datetime.date(int(ca[0]),int(ca[1]),int(ca[2])),Timestamp__lte = datetime.date(int(cb[0]),int(cb[1]),int(cb[2])),Vehicle_Status = "NOTOK",Lane_Number = lan).count()
			
			total = permit+denied
			if total == 0:
				lanep = 0
				laned = 0
			else:
				lanep = (float(permit)/ (total)) * 100
				laned = (float(denied)/ (total)) * 100
			
			lanepp = int(round(lanep))
			lanedd = int(round(laned))
			
			data["laneno"] = lan
			data["permit"] = lanepp
			data["denied"] = lanedd
			data["fine"] = fine_amount
			full.append(data)
		
		
		return render_to_response("Transport/chart.html",{"full":full,"date1":date1,"date2":date2})	
	
	#except:
		#return redirect("/")

	


#@nano_login_required
def index(request):
	'''this for the displaying what are the users currently in the tollbooth user'''
	lane = Edit_Lane.objects.all()
	users = Signup.objects.all()
	context = { 'lane':lane,'users':users}
    	return render(request,'Admin/addfield.html', context)
		
#@nano_login_required
def create(request):
	'''this for the creation of new user with valid username and password,user lane number,user type'''
	create = Edit_Lane(Lane_Number=request.POST['lane'],Direction=request.POST['direction'])
	create.save()
	mon = Monitor(Lane_Number=request.POST['lane'],Direction=request.POST['direction'])
	mon.save()
	return redirect('/index')
	
#@nano_login_required
def edit(request, id):
	'''this method for the changing the user name or editing'''
	edit = Edit_Lane.objects.get(id = id)
	context = {'edit':edit}
	return render(request,'Admin/editfield.html', context)
	
#@nano_login_required
def update(request, id):
	'''this for the updation of username in our database'''
	lane = request.POST['lane']
	update = Edit_Lane.objects.get(id = id)
	update.Lane_Number = request.POST['lane']
	update.User_Name = request.POST['user']
	update.Direction = request.POST['direction']
	
	update.save()
	monn = Monitor.objects.get(Lane_Number = lane)
	monn.Lane_Number = request.POST['lane']
	monn.Direction = request.POST['direction']
	monn.save()
	return redirect('/index')
	
	
#@nano_login_required
def destroy(request, id):
	'''this method for the destroying or deleting the records from the database'''
	des = Edit_Lane.objects.get(id = id)
	lane = des.Lane_Number 
	des.delete()
	dest = Monitor.objects.get(Lane_Number = lane)
	dest.delete()
	return redirect('/index')
	
	
#@nano_login_required
def search_image(request):
	try:
		#'''this method for the searching of vehicle along with snap shot of particular vehicle image will be displayed to user.
		#this snapshot will be generated at the time vehicle entering into border and snapshot will be stored in our local database.'''
		
		w=request.POST["searchfilter"]
		x = request.POST["value1"]
		pre = request.POST["previous"]
		next = request.POST["next"]
		
		
		if pre:
			
			page = pre
		elif next:
			
			page = next
		else:
			
			page = 1
				
		if w=="vehicle":
			search= Main.objects.filter(Vehicle_Number = x)
			
			
		elif w=="transaction":
			search= Main.objects.filter( Transaction_Id = x)
			
		else:
			msg= "error"
			return render_to_response("Admin/Admin.html",{"flag":msg})		
			
		''' paginations '''
		contact_list = search
		paginator = Paginator(contact_list, 10) # Show 10 records per page
		
		
		
		
		try:
			contacts = paginator.page(page)
			
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			contacts = paginator.page(1)
			
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			contacts = paginator.page(paginator.num_pages)
		return render_to_response("Admin/Admin.html",{'search':search,'x':x,'w':w})
		

	except:
		return render_to_response("Admin/Admin.html")
		
	
	#return render_to_response("Admin/Admin.html",{"flag":msg})

#@nano_login_required
def index_cam(request):
	''' this method for the displaying normal camera and anpr camera ip address,barrier gate,sensor address.'''
	cam = Edit_Lane.objects.all()
	context = { 'cam':cam}
    	return render(request,'Admin/addcamera.html', context)
		
#@nano_login_required
def create_cam(request):
	'''this method for the creation of new camera ip address adding'''
	la = request.POST['Lane']
	
	if la < 11:
		direction = "IN"
	else:
		direction = "OUT"
	
	c = Edit_Lane(Lane_Number=request.POST['Lane'],Direction = direction,Weighbridge_Ip = request.POST['Weighbridge'],Boombarrier_Ip = request.POST['Boombarrier'],Profiler_Ip = request.POST['Profiler'],Anpr_Ip=request.POST['Anpr'],Camera_Ip=request.POST['Camera'],User_Ip = request.POST['User'])
	c.save()
	
	d = Monitor(Lane_Number=request.POST['Lane'],Direction = direction,Weighbridge = request.POST['Weighbridge'],Boombarrier = request.POST['Boombarrier'],Profiler = request.POST['Profiler'],Anpr =request.POST['Anpr'],Camera =request.POST['Camera'],Tolluser = request.POST['User'])
	d.save()
	return redirect('/index_cam')
	
	
#@nano_login_required
def edit_cam(request, id):
	'''edit camera ip address used for the editing the details for just displaying'''
	edit = Edit_Lane.objects.get(id = id)
	context = {'edit':edit}
	return render(request,'Admin/editcamera.html', context)
	
#@nano_login_required
def update_cam(request, id):
	'''this method for the updation of camera like new ip address adding'''
	lane = request.POST['Lane']
	la = int(lane)
	
	
	if la < 11:
		direction = "IN"
		
	else:
		direction = "OUT" 
		
		
	update = Edit_Lane.objects.get(id = id)
	update.Lane_Number = request.POST['Lane']
	update.Anpr_Ip = request.POST['Anpr']
	update.Camera_Ip = request.POST['Camera']
	update.User_Ip = request.POST['User']
	update.Profiler_Ip = request.POST['Profiler']
	update.Boombarrier_Ip = request.POST['Boombarrier']
	update.Weighbridge_Ip = request.POST['Weighbridge']
	update.Direction = direction
	update.save()

	upmon = Monitor.objects.get(Lane_Number = lane)
	upmon.Lane_Number = request.POST['Lane']
	upmon.Anpr = request.POST['Anpr']
	upmon.Camer = request.POST['Camera']
	upmon.Tolluser = request.POST['User']
	upmon.Profiler = request.POST['Profiler']
	upmon.Boombarrier = request.POST['Boombarrier']
	upmon.Weighbridge = request.POST['Weighbridge']
	upmon.Direction = direction

	upmon.save()
	return redirect('/index_cam')
	
	
#@nano_login_required
def destroy_cam(request, id):
	''' this method for deleting of camera ip address only accessed by the admin member '''
	des = Edit_Lane.objects.get(id = id)
	lan = des.Lane_Number 
	des.delete()

	mon = Monitor.objects.get(Lane_Number = lan)
	mon.delete()
	return redirect('/index_cam')	
	
	
#@nano_login_required
def index_user(request):
	'''displaying the tollbooth users list'''
	user = Signup.objects.all()
	context = { 'user':user}
    	return render(request,'Admin/adduser.html', context)
		
		
#@nano_login_required
def create_user(request):
	'''this method for the creation of new user purpose'''
	t = Datetime.now()
	c = Signup(Created_Time = t,Lane_Number=request.POST['lane'],User_Name = request.POST['user'],First_Name = request.POST['first'],Last_Name = request.POST['last'],User_Type = request.POST['type'],Password = request.POST['pass'])
	c.save()
	return redirect('/index_user')

#@nano_login_required	
def edit_user(request, id):
	''' edit user is used for editing username,password,lane normal
		(Resting password also perform here)	'''
	edit = Signup.objects.get(id = id)
	context = {'edit':edit}
	return render(request,'Admin/edituser.html', context)
	
	
#@nano_login_required
def update_user(request, id):
	'''this method for updation of new use shifting one lane to another lane'''
	tt = Datetime.now()
	update = Signup.objects.get(id = id)
	update.Lane_Number = request.POST['lane']
	update.User_Name = request.POST['user']
	update.First_Name = request.POST['first']
	update.Last_Name = request.POST['last']
	update.User_Type = request.POST['type']
	update.Password = request.POST['pass']
	update.Updated_Time = tt
	update.save()
	
	return redirect('/index_user')
	
	
#@nano_login_required
def destroy_user(request, id):
	'''this method for complete deletion of user from  our database'''
	des = Signup.objects.get(id = id)
	des.delete()
	return redirect('/index_user')	

	
#@nano_login_required	
def display(request):
	if request.session.has_key('User_Name'):    
		
			mon = Ping.objects.all()
			t = Datetime.now()
			
			return render_to_response('Monitor/monitor.html',{"t":t,"mon":mon})
	else:
		msg = "session is closed"
		return render_to_response('Login/login.html',{"flag":msg})
		
		
		
		
#<=======================================================end==============================================================================>
	
	
	
	#<======================================== extra function=================================================================>
	
		
	
def go(request):
	#if request.session.has_key('User_Name'):
		if request.POST:
			User_Name = request.POST['User_Name']		
			password=request.POST["Password"]
			Number=request.POST["Vehicle"]	
			
			my_data = Edit_Lane.objects.filter(User_Name=User_Name)
			
			for i in my_data:
				toll_name = i.User_Name
				
				toll_number = i.Lane_Number
				toll_dir = i.Direction
				toll_loc = i.Location
			ancam = Edit_Lane.objects.filter(Lane_Number = toll_number)
			for a in ancam:
				cam=a.Camera1
				cam1=a.Camera2

			data=Relay_Panel.objects.filter(id=toll_number)[0]
			if toll_number==1:
				data.Lane_1='False'
				data.save()
			if toll_number==2:
				data.Lane_2='False'
				data.save()
			if toll_number==3:
				data.Lane_3='False'
				data.save()
			return render_to_response("barriergate.html",{'User_Name':User_Name,"Password":password,"lane_N":toll_number,"toll_dir":toll_dir,"toll_loc":toll_loc,"cma":cam,"cam1":cam1,'Vehicle_Number':Number})
	#else:
		#msg="Antharization"
		#return render_to_response("Login/login.html",{'flag':msg})


def signup_data(request):
	#if request.session.has_key('User_Name'):
		if request.method=="POST":
		
			#try:
				User_Name=request.POST["username"]	
				password=request.POST["password"]
				confirmpassword=request.POST["confirm_pass"]
				typeofuser = request.POST["default"]
				firstname=request.POST["firstname"]
				lastname=request.POST["lastname"]
				laneno=request.POST['laneno']
				if 'user'==User_Name:
					import re
					if not re.search("[a-z]",User_Name):
						msg="User name should a-z Characters only!"
						return render(request,"sign.html",{'flag':msg,"User_Name":User_Name,"firstname":firstname,"lastname":lastname,"password":password,"confirm_pass":confirmpassword,"laneno":laneno,"Location":Location})

					elif password !=confirmpassword:
						msg="Password don't match!"
						return render(request,'signup.html',{'flag':msg,"User_Name":User_Name,"firstname":firstname,"lastname":lastname,"password":password,"confirm_pass":confirmpassword,"laneno":laneno,"Location":Location})
					elif Signup.objects.filter(User_Name=User_Name).exists() :
						msg="User_Name already exist!Please login or request for new Password!"
						return render_to_response("sign.html",{'flag':msg})
					elif Edit_Lane.objects.filter(Lane_Number=laneno).exists():
						msg="Lane No already exist Please enter different"
						return render_to_response("sign.html",{'flag':msg})

					else:
						obj=Signup(User_Name=User_Name,Password=password,User_Type=typeofuser)
						obj.save()
						data=Edit_Lane(User_Name=User_Name,Lane_Number=laneno)
						data.save()
						msg="Account has been successfully created.Please login!"
						return render_to_response("sign.html",{'flag':msg})
				else:
					if password !=confirmpassword:
						msg="Password don't match!"
						return render(request,'signup.html',{'flag':msg,"User_Name":User_Name,"firstname":firstname,"lastname":lastname,"password":password,"confirm_pass":confirmpassword,"laneno":laneno,"Location":Location})
					elif Signup.objects.filter(User_Name=User_Name).exists() :
						msg="User_Name already exist!Please login or request for new Password!"
						return render_to_response("sign.html",{'flag':msg})
					else:
						obj=Signup(User_Name=User_Name,Password=password,User_Type=typeofuser)
						obj.save()
						msg="Account has been successfully created.Please login!"
						return render_to_response("sign.html",{'flag':msg})
			#except:
			#	msg="User_Name Not Valid!"
	#else:
		#return redirect("/")
#@login_required(login_url="login/")
def sign_up(request):	
	return render_to_response("sign.html",{})
	
	
def edit_lane(request):
	#if request.session.has_key('User_Name'):
		if request.method=="POST":
			User_Name=request.POST["User_Name"]
			password=request.POST["Password"]
			data=Edit_Lane.objects.all()
			tim1=[]	
			for i in data:
				data={}
				data['Lane_Number']=str(i.Lane_Number)
				data["User_Name"]=str(i.User_Name)
				data["Direction"]=str(i.Direction)
				tim1.append(data)
			return render_to_response("edit_lane1.html",{"timesta":tim1,"User_Name":User_Name,"Password":password})
	#else:
		#msg="Your session has been successfully logout!!"
		#return render_to_response("Login/login.html",{})

def edit_lanenumber(request):
	#if request.session.has_key('User_Name'):
		name=request.POST.get("User_Name")
		Lane_Number=request.POST.get("Lane_Number")
		status=request.POST.get("Direction")

		Edit_Lane.objects.filter(User_Name=name).update(Lane_Number=Lane_Number,Direction=status)
		msg="Your values are updated successfully"
		data=Edit_Lane.objects.all()
		tim1=[]
		for i in data:
			data={}
			data['Lane_Number']=str(i.Lane_Number)
			data['User_Name']=str(i.User_Name)
			data['Direction']=str(i.Direction)
			tim1.append(data)
		return render(request,"edit_lane1.html",{'flag':msg,"timesta":tim1})
	#return redirect("/")
def reset_pass(request):
	#if request.session.has_key('User_Name'):
		if request.method=="POST":
			User_Name=request.POST["User_Name"]
			password=REQUEST.post["Password"]

		return render_to_response("reset_password.html",{"User_Name":User_Name,"Password":password})
	#else:
		#msg="Your session has not created!"
		#return render_to_response("Login/login.html",{'flag':msg})

def reset_password(request):
	#if request.session.has_key('User_Name'):
		if request.method=="POST":
			User_Name=request.POST['User_Name']
			existingpass=request.POST['ex_password']
			new=request.POST['new_password']
			if  not Signup.objects.filter(user_name=User_Name).exists():
				msg="User_Name does  not Exist!"
				return render(request,"reset_password.html",{"flag":msg,"User_Name":User_Name,"ex_password":existingpass,"new_password":new})  
			elif not Signup.objects.filter(password=existingpass).exists():
				msg="Password does not match with existing!"
				return render(request,"reset_password.html",{'flag':msg,"User_Name":User_Name,"ex_password":existingpass,"new_password":new})
			else:
				Signup.objects.filter(user_name=User_Name).update(password=new)
				msg="Password Updated Successfully!"
				return  render_to_response("vehicledetails.html",{"flag":msg})
	#else:
		#msg="session will be not created"
		#return render_to_response("Login/login.html",{})


   
   

def monitor(s):
    while True:
        sleep(30)
        
        
        
        m = Monitor.objects.filter(Lane_Number = s)
        for i in m:
            w = i.Webapp
            a = i.Anpr
            p= i.Profiler
            wb = i.Weighbridge 
            b = i.Boombarrier
            t = i.Tolluser 
            c = i.Camera
            u = i.User_Name
            l = i.Location
            st = i.Status
        
            response = os.system("ping -c 1 " +w)
            if response == 0:
                cw = "green"
            else:
                cw = "red"

            response = os.system("ping -c 1 " +a)
            if response == 0:
                ca = "green"
            else:
                ca = "red"
        
            response = os.system("ping -c 1 " +p)
            if response == 0:
                cp = "green"
            else:
                cp = "red"
        
            response = os.system("ping -c 1 " +wb)
            if response == 0:
                cwb = "green"
            else:
                cwb = "red"
        
            response = os.system("ping -c 1 " +b)
            if response == 0:
                cb = "green"
            else:
                cb = "red"
            
            response = os.system("ping -c 1 " +t)
            if response == 0:
                ct = "green"
            else:
                ct = "red"
        
            response = os.system("ping -c 1 " +c)
            if response == 0:
                cc = "green"
            else:
                cc = "red"
            
            
            tt = Datetime.now()
        
            p = Ping(id = s,Lane_Number = s,Webapp = cw,Anpr = ca,Profiler = cp,Weighbridge = cwb,Boombarrier = cb,Tolluser = ct,Camera = cc,User_Name = u,Location = l,Status = st,Timestamp = tt)
            p.save()
            
    
            mon = Ping.objects.all()
            
    return monitor()





#threads = []
#for i in range(1,17):
#    t = threading.Thread(target=monitor, args=(i,))
#    threads.append(t)
#    t.start()

