from django.db import models

class Patient_complaint(models.Model):
	Patient_name = models.CharField(max_length=30)
	patient_email = models.EmailField()
	patient_aadhar = models.IntegerField()
	patient_complaint = models.TextField()

	def __str__(self):
		return self.patient_name
class Patient_Register(models.Model):
	patient_name=models.CharField(max_length=100)		
	patient_email=models.EmailField()
	patient_aadhar=models.IntegerField()
	patient_image=models.ImageField(upload_to='user/')
	patient_password=models.CharField(max_length=30)
	def __str__(self):
		return self.patient_name 