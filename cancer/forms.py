from django.forms import ModelForm
from cancer.models import *

class PatientForm(ModelForm):
	class Meta:
		model=Patient_complaint
		fields='__all__'
class PatientRegisterForm(ModelForm):
	class Meta:
		model=Patient_Register
		fields='__all__'