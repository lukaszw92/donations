# Generated by Django 3.1.1 on 2020-09-19 14:33

from django.db import migrations, models
import giveaway.models


class Migration(migrations.Migration):

    dependencies = [
        ('giveaway', '0009_auto_20200915_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='quantity',
            field=models.IntegerField(validators=[giveaway.models.positive_validator]),
        ),
    ]
