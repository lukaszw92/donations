from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from giveaway.forms import NewUserCreationForm
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


class LoginPageView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, password=password, username=username)

        if user is not None:
            login(request, user)
            return redirect('/')

        return render(request, 'registration/register.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')
