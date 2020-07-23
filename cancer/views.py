from django.shortcuts import render
from cancer.forms import *
from cancer.models import *
from django.core.mail import send_mail
from disss import settings
from django.http import HttpResponse
# Create your views here.
def index(req):
	return render(req,'cancer/index.html')
def home(req):
	return render(req,'cancer/home.html')
def register(req):
	if req.method=="POST":
		print("step1")
		form=PatientRegisterForm(req.POST,req.FILES)
		print("step2")
		if form.is_valid():
			print("step3")
			sub="registration_configuration"
			body="your registration successfully completed"
			receiver=req.POST['patient_email']
			sender=settings.EMAIL_HOST_USER
			send_mail(sub,body,sender,[receiver])
			form.save()
			return render(req,'cancer/home.html')
		else:
			return render(req,'cancer/register.html')	

	form=PatientRegisterForm()
	return render(req,'cancer/register.html',{'form':form})	
def login(req):
	if req.method=="POST":
		try:
		    data=Patient_Register.objects.get(patient_email=req.POST['username'],patient_password=req.POST['password'])
		    if data.patient_email==req.POST['username']  and data.patient_password==req.POST['password'] :
			    return render(req,"cancer/profile.html",{'data':data})
		    else:
			    return HttpResponse("invalid logins")
		except Patient_Register.DoesNotExist:
		    return HttpResponse("invalid logins")


	

	return render(req,"cancer/login.html")	

def changepassword(req):
	if req.method=="POST":
		oldpassword=req.POST['old']
		newpassword=req.POST['newp']
		confirmpassword=req.POST['conp']
		data=Patient_Register.objects.get(patient_password=oldpassword)
		if data:
			if newpassword==confirmpassword:
				data.patient_password=newpassword
				data.save()
				return HttpResponse("password changed")
			else:
				return HttpResponse("wrong password")
		else:
			return HttpResponse("no data")
	return render(req,'cancer/changepassword.html')				
					


	return render(req,'cancer/changepassword.html')		 
def showpatients(req):
	data=Patient_Register.objects.all()
	return render(req,'cancer/patientdetails.html',{'data':data})
def contact(req):
	if req.method=="POST":
		form=PatientForm(req.POST)
		if form.is_valid():
			sub="confirmation mail"
			body="your complaint taken"
			
			receiver=req.POST['patient_email']
			sender=settings.EMAIL_HOST_USER
			send_mail(sub,body,sender,[receiver])
		form.save()
		return HttpResponse("success")

	form=PatientForm()
	return render(req,'cancer/contact.html',{'form':form})		