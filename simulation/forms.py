from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Simulation

UserModel = get_user_model()

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ["username", "email" ,"password1", "password2"]


class SimulationForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        


class UploadSimulationForm(forms.Form):       
    txt_file = forms.FileField(label='Upload TXT File')
