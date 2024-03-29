from django.core import validators
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField,UserChangeForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import PasswordInput, Widget
from .models import signup



class user_login(AuthenticationForm):
    username=UsernameField(max_length=20,widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(max_length=12,label='PASSWORD',widget=PasswordInput(attrs={'class':'form-control'}))



class hubsign_up(UserCreationForm):
    password2=forms.CharField(label='Confirm Password(again)',
    widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}



#user change form

class Edituserprofileform(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email','first_name':'First Name','last_name':'Last Name'}


# admin profile

class EditAdminprofileform(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields='__all__'
        labels={'email':'Email'}