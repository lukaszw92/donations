# Generated by Django 3.1.1 on 2020-09-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveaway', '0004_auto_20200915_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
