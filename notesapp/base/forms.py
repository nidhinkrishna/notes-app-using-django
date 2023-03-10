from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','email','password1','password2']


class AddNotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','description']


class EditProfile(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','email','name','image','bio']
