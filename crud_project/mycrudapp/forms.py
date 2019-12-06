from django import forms
from mycrudapp.models import Employee
from django.contrib.auth.models import User


class EmployeeForm(forms.ModelForm):
	
	class Meta:
		model = Employee
		fields = '__all__'



class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','email','password')