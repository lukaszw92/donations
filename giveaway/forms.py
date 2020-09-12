from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.forms import Textarea, TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm


class NewUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        # widgets = {
        #     'first_name': TextInput(attrs={'placeholder': 'Imię'}),
        #     'last_name': TextInput(attrs={'placeholder': 'Nazwisko'}),
        #     'email': TextInput(attrs={'placeholder': 'Email'}),
        #     'password1': PasswordInput(attrs={'placeholder': 'Hasło'}),
        #     'password2': PasswordInput(attrs={'placeholder': 'Powtórz hasło'}),
        # }



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Imię'}),
            'last_name': TextInput(attrs={'placeholder': 'Nazwisko'}),
            'email': TextInput(attrs={'placeholder': 'Email'}),
            'password': TextInput(attrs={'placeholder': 'Hasło'}),
            'password2': TextInput(attrs={'placeholder': 'Powtórz hasło'}),
        }