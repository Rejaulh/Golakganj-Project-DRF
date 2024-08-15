# Generated by Django 5.0.7 on 2024-07-15 08:10

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_category_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.TextField()),
            ],
        ),
    ]
