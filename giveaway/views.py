from datetime import date

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
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


class AddDonationView(LoginRequiredMixin, View):

    def get(self, request):
        categories = Category.objects.all()
        organisations = Institution.objects.all()
        context = {'categories': categories, 'organisations': organisations}
        return render(request, 'form.html', context)

    def post(self, request):
        bags = request.POST.get('bags')
        organisation = request.POST.get('organization')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        date = request.POST.get('data')
        time = request.POST.get('time')
        more_info = request.POST.get('more_info')
        full_address = f'{city}, {address}'
        new_donation = Donation.objects.create(quantity=bags, institution_id=organisation, address=full_address,
                                zip_code=postcode, pick_up_date=date, pick_up_time=time,
                                phone_number=phone, pick_up_comment=more_info, user=request.user)

        categories = request.POST.getlist('categories')
        new_donation.categories.set(categories)

        return redirect(reverse('landing_page'))

class UserProfile(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        donations = Donation.objects.filter(user=user.id, pick_up_date__lte=date.today())
        future_donations = Donation.objects.filter(user=user.id, pick_up_date__gt=date.today())
        context = {'user': user, 'donations': donations, 'future_donations': future_donations}
        return render(request, 'user_profile.html', context)











