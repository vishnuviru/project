from django.shortcuts import render
from django.http import HttpResponse

from Tollapp.models import *
from django.shortcuts import render
from time import time,strftime,gmtime
import datetime
from django.contrib.auth.decorators import login_required

import os
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render_to_response



import MySQLdb


@csrf_exempt
def  mainpage(request):

	return render_to_response('login.html')



@csrf_exempt
@login_required
def display_homepage(request):
			

		#vehicle_number=request.POST['Vehicle_Number']

		#if username==
		
		


		try:

			username_new=str(request.POST["Username"])
			password=request.POST["Password"]
			print "both username and pass",username_new,password
			username=username_new.lower()
		except:
			msg="Username is Not Valid"
			#instance=login.objects.get(user_name=username).password
		#print "instance is ",instance
		#if password==instance :



		try:
			instance=login.objects.get(user_name=username).password
			print  "redddyyyyy",username
			print "instance is",instance
			if  password==instance:
				
				return render_to_response("homepage2.html",{})
			else:
				msg="Password is Invalid!!"
				return render_to_response('login.html',{'flag':msg})
						

		except:
			msg= "Username  is Invalid!!!"
			return render_to_response('login.html',{'flag':msg})
	#else:
	#	msg="Password  is Invalid!!"
	#	return render_to_response('login.html',{'flag':msg})

@login_required
@csrf_exempt
def  get_details(request):



				#try:
				#	Number=request.POST["VehicleNumber"]

				try:
					g=temp_details.objects.order_by('Timestamp')[0]
					x=g.Timestamp
					y=g.lane_Number
					print "hai",y,x
					data=log_details(Timestamp=x,lane_Number=y)
					
					data.save()
				except:
					msg="page is not loaded"






				try:
					Number=request.POST["VehicleNumber"]
					print "haiii",Number
					#g=temp_details.objects.filter('Timestamp'=min('Timestamp')).get()
					

					
					


					data=vehicle.objects.filter(Vehicle_Number=Number).order_by('Timestamp')
					Veh_no=0
					Time=0
					Die_h=0
					Die_l=0
					Die_b=0
					Fit_va=0
					Pol_va=0
					Per_va=0
					Inc=0
					Toll=0
					Veh_cla=0
					Loca=0
					off=0
					AXL=0
					sta=0
					office=0
					submited=0
					Trans=0
					lane=0
					for i in data:
						print i.Vehicle_Number

						#print "Number isss",i.Vehilce_Number
						if i.Vehicle_Number==Number:
							Trans=i.TransactionID
							veh_no=i.Vehicle_Number
							Die_h=i.Diemension_height
							Pol_va=i.Pollution_Validity
							Per_va=i.Permit_validity
							Fit_va=i.Fitness_Validity
							Die_l=i.Diemension_length
							Die_h=i.Diemension_height
							Die_b=i.Diemension_Breadth
							AXL=i.AXLE_Count
							sta=i.Vehicle_status
							office=i.officer_name
							Time=i.Timestamp
							Toll=i.tollbooth_username
							Veh_cla=i.Vehicle_ClassType
							lane=i.lane_Number
							

							print "My dataaa",Time,Die_h,Pol_va,Per_va,Fit_va,Die_l,Die_b,Die_h,AXL,sta,Toll,veh_no
							
							


							return render_to_response('tollsystem2.html',{"Diemension_h":Die_h,"VehicleNum":veh_no,"Pollution_va":Pol_va,"Permit_va":Per_va,"Fitness_va":Fit_va,"Diemension_l":Die_l,"Diemension_b":Die_b,
																			"AXLE_C":AXL,"Vehicle_status":sta,"officer_name":office,"Timestamp":Time,"Tollbooth_user":Toll,"TransactionID":Trans,"Vehicle_class":Veh_cla,"lane_N":lane})
							
							
						else:
							msg="Please enter a valid Vehicle Number!!!!"
							return render_to_response('vehicledetails.html',{'flag':msg})
							return response

				except:
					msg="Please enter a valid Vehicle Number!!"
					return render_to_response('vehicledetails.html',{'flag':msg})
