from datetime import date

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect, reverse
from django.views import View

from giveaway.forms import NewUserCreationForm, NewUserEditForm
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


class EditUserView(View):

    def get(self, request):
        form = NewUserEditForm(instance=request.user)
        return render(request, 'registration/user_edit.html', {'form': form})

    def post(self, request):
        wrong_password = "Podaj poprawne hasło"
        password = request.POST.get('password')
        form = NewUserEditForm(request.POST, instance=request.user)
        user = authenticate(request, password=password, email=request.user.email)

        if user is None:
            return render(request, 'registration/user_edit.html', {'form': form, "wrong_password": wrong_password})

        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'registration/user_edit.html', {'form': form})


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

    login_url = "/donations/login/"

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

        return redirect(reverse('confirmation'))


class UserProfile(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        pending_donations = Donation.objects.filter(user=user.id, pick_up_date__lte=date.today(), is_taken=False)
        taken_donations = Donation.objects.filter(user=user.id, pick_up_date__lte=date.today(),
                                                  is_taken=True).order_by('pick_up_date')
        future_donations = Donation.objects.filter(user=user.id, pick_up_date__gt=date.today()).order_by('creation_date')
        context = {'user': user, 'pending_donations': pending_donations,
                   'future_donations': future_donations,
                   'taken_donations': taken_donations}
        return render(request, 'user_profile.html', context)


class ConfirmPickupView(View):
    def get(self, request, pk):
        donation = Donation.objects.get(pk=pk)
        return render(request, 'confirm_pickup.html', {'donation': donation})

    def post(self, request, pk):
        donation = Donation.objects.get(pk=pk)
        if request.POST.get('confirmation') == 'Potwierdzam':
            donation.is_taken = True
            donation.confirmation_date = date.today()
            donation.save()
            return redirect(reverse('user_profile'))













