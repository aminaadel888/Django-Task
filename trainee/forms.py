from django import forms
from .models import Trainee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ['name', 'email', 'age', 'course', 'mentor']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
