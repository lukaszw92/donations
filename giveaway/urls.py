from django.urls import path, include
from giveaway import views

urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("add_donation/", views.AddDonationView.as_view(), name="add_donation")

]