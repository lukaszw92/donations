from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def positive_validator(value):
    if value <= 0:
        raise ValidationError("Wartość musi być pozytywna.")


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Institution(models.Model):
    institution_types = (
        (1, "non-government organisation"),
        (2, "local collection"),
        (3, "foundation"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.IntegerField(choices=institution_types, default=3)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.name}'

    def get_categories_ids(self):
        ids = []
        for category in self.categories.all():
            ids.append(category.id)
        return ids


    @staticmethod
    def get_institutions_number():
        return len(Institution.objects.all())


class Donation(models.Model):
    quantity = models.IntegerField(validators=[positive_validator])
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default='Null', on_delete=models.CASCADE)
    is_taken = models.BooleanField(default=False)
    creation_date = models.DateField(auto_now_add=True)
    confirmation_date = models.DateField(null=True, blank=True)

    def get_confirm_url(self):
        return reverse('confirm_pickup', args=(self.pk,))

    @staticmethod
    def get_total_quantity():
        total = 0
        for donation in Donation.objects.all():
            total += donation.quantity
        return total
