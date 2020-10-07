from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')
