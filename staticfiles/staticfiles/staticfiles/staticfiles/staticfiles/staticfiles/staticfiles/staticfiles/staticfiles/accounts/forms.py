from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="username", max_length=150)
    password = forms.CharField(label="password", widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="username", max_length=150)
    fname = forms.CharField(label = "fname", max_length=50)
    lname =forms.CharField(label = "lname", max_length=50)
    birth_date = forms.DateField(label = "birth_date")
    email = forms.EmailField()
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

