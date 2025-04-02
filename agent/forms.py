from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AgentList



class AgentRegisterForm(UserCreationForm):
   
    class Meta:
        model = AgentList
        fields = ['username', 'phone', 'email', 'first_name', 'last_name',]


class AgentUpdateForm(forms.ModelForm):
    class Meta:
        model = AgentList
        fields = [ 'first_name', 'gender', 'state', ]
       