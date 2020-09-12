from django.contrib import admin
from django.contrib.auth import get_user_model

from giveaway.models import Institution, Donation, Category, User


admin.site.register(Institution)
admin.site.register(Donation)
admin.site.register(Category)
admin.site.register(get_user_model())

