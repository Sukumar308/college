from django import forms
from app.models import *

class User_Form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email','password')


class User_data_Form(forms.ModelForm):
    class Meta:
        model=User_data
        fields=('Admission_Number','Father_name','profile_pic')
