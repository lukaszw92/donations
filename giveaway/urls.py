from django.urls import path, include
from django.views.generic import TemplateView

from giveaway import views

urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("edit_user/", views.EditUserView.as_view(), name="edit_user"),
    #path("edit_password", views.EditPasswordView.as_view(), name="edit_password"),
    path("add_donation/", views.AddDonationView.as_view(), name="add_donation"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path("user_profile/", views.UserProfile.as_view(), name="user_profile"),
    path('confirmation/', TemplateView.as_view(template_name='form-confirmation.html'), name="confirmation"),
    path('confirm_pickup/<int:pk>', views.ConfirmPickupView.as_view(), name='confirm_pickup'),

]