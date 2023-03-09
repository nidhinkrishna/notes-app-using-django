from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','email','password1','password2']
