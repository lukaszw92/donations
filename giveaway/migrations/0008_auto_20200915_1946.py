# Generated by Django 3.1.1 on 2020-09-15 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giveaway', '0007_auto_20200915_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='confrimation_date',
            new_name='confirmation_date',
        ),
    ]