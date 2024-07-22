from django.forms import ModelForm
from .models import *

class employeeForm(ModelForm):
    class Meta:
        model = usr_profile
        fields = '__all__'
        