from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

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

class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('/')
    template_name = "registration/register.html"


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')