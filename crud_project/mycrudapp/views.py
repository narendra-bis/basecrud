from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from mycrudapp.models import Employee
from mycrudapp.forms import EmployeeForm, UserForm

from django.contrib.auth import login, authenticate
# Create your views here.


def index(request):
	return HttpResponse('welcome to crud app')

def register(request):
	if request.method =='POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/show')
				# return HttpResponse('form saved successfully')
			except:
				pass
	else:
		form = EmployeeForm()
	return render(request,'register.html', {'form':form})



def show_records(request):
	erecords = Employee.objects.all()
	ecount = Employee.objects.all().count()
	return render(request,'showrecord.html',{'erecords':erecords, 'ecount':ecount})



def edit_record(request,pk):
	employee = Employee.objects.get(id=pk)
	return render(request,'editrecord.html',{'employee':employee})


def update(request, id):
	print('checcckk id ',id)
	employee = Employee.objects.get(id=id)
	if request.method == 'POST':
		form = EmployeeForm(request.POST, instance = employee)

		if form.is_valid():
			try:
				form.save()
				return redirect('/show')
			except:
				pass
	else:
		return render(request,'editrecord.html',{'employee':employee})



def destroy(request,id):
	employee = Employee.objects.get(id=id)

	employee.delete()
	return redirect('/show')



def signup(request):
	if request.method=='POST':
		registered = False
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()

			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			form.save()
			user = authenticate(username=username, password=raw_password)
			login(request,user)
			return redirect('/show')
		else:
			response = 'this user is already exist'
			form = UserForm()
			return render(request, 'signup.html',{'form':form, 'response':response})
	else:
		form = UserForm()
		return render(request, 'signup.html',{'form':form})


			
