from django import forms
from .models import Twix
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TwixForm(forms.ModelForm):
    class Meta:
        model = Twix
        fields = ['twit','image']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')