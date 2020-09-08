from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)


class Institution(models.Model):
    institution_types = (
        ("1", "non-government organisation"),
        ("2", "local collection"),
        ("3", "foundation"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField
    type = models.CharField(choices=institution_types, default='3', max_length=1)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField
    user = models.ForeignKey(User, null=True, default='Null', on_delete=models.CASCADE)


