from django import forms
from .models import Signup


class LoginForm(forms.Form):
	#import pdb;pdb.set_trace();
	#username = forms.CharField(label='Username',max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))
	#password = forms.CharField(label='password',widget=forms.TextInput(attrs={'class': 'form-control log-padding', 'placeholder':'Password'}))
	username=forms.CharField(max_length=100,label='Username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','style':'font-size:20px',}),)
	password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','style':'font-size:20px'}),)
	

	
	def clean_password(self):
		password=self.cleaned_data.get('password')
		username=self.cleaned_data.get('username')
		print "passssssssssssss",password
		
		if  not Signup.objects.filter(User_Name=username,Password=password).exists():
			raise forms.ValidationError("Please enter a valid Username Password!")
		return password





'''
def clean_username(self):
		
		#import pdb;pdb.set_trace();
		
		username=self.cleaned_data.get('username')
		print "userrrrrrrrrrr",username
		if not  Signup.objects.filter(User_Name=username).exists():
			raise forms.ValidationError("Please Enter valid User name!")
		return username 
'''

"""
	class Meta:
		model=Signup
		fields=['User_Type' ,'Create_Time','Password','User_Name','First_Name','Last_Name','Lane_Number']
	def clear_data(self):
		User_name=self.cleaned_data.get('User_Name')
		print "User_Nameeeeeeeeeee",User_name
		return User_name

username = forms.CharField(
		label="Username",
		widget=forms.TextInput(
			attrs={
				'class':'form-control logpadding',
				'placeholder':"Username"}),
	)
	password = forms.CharField(
		label="Password", 
		widget = forms.PasswordInput(
			attrs={
				'class': 'form-control logpadding',
                'placeholder': "New Password"}),
	)



"""	