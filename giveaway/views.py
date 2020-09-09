from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView


class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')