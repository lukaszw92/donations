from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from giveaway.forms import RegistrationForm, NewUserCreationForm
from giveaway.models import Donation, Institution, Category


class MainPageView(View):
    def get(self, request):
        sacks = Donation.get_total_quantity()
        institutions_number = Institution.get_institutions_number()
        ngos = Institution.objects.filter(type=1)
        locals = Institution.objects.filter(type=2)
        fundations = Institution.objects.filter(type=3)
        context = {'sacks': sacks, 'institutions_number': institutions_number, 'ngos': ngos,
                   'locals': locals, 'fundations': fundations}
        return render(request, 'main.html', context)


# class RegisterView(View):
#     def get(self, request):
#         return render(request, 'registration/register.html')

# def register(request):
#     form = NewUserCreationForm()
#     if request.method == 'POST':
#         form = NewUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     return render(request, 'registration/register.html', {'form': form})

class RegisterView(View):
    def get(self, request):
        form = NewUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registration/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')


# def register(request):
#     form = NewUserCreationForm()
#     if request.method == 'POST':
#         form = NewUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     return render(request, 'registration/register.html', {'form': form})



class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')
