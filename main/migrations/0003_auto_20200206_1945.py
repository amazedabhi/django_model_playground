# Generated by Django 3.0.3 on 2020-02-06 14:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200205_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=100, null=True, validators=[django.core.validators.EmailValidator('Email address is not valid')]),
        ),
    ]
