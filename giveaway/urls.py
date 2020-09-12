from django.urls import path, include
from giveaway import views

urlpatterns = [
    #path("", include('django.contrib.auth.urls')),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("add_donation/", views.AddDonationView.as_view(), name="add_donation"),
    path("login/", views.LoginPageView.as_view(), name="login")
]