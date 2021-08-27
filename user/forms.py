
from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm
from .models import *


class User_creation(UserCreationForm):
	class Meta:
		model = User
		fields = [ 'first_name','last_name','email' ,'phone_number', 'password1','password2',]
