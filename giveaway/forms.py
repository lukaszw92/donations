from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.forms import Textarea, TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm


class NewUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']


