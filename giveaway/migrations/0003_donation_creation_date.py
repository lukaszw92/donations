# Generated by Django 3.1.1 on 2020-09-15 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveaway', '0002_donation_is_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='creation_date',
            field=models.DateField(default=datetime.date(2020, 9, 15)),
        ),
    ]
