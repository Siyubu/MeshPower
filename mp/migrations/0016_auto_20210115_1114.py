# Generated by Django 3.1.2 on 2021-01-15 09:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0015_auto_20210115_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='serial_number',
            field=models.CharField(default='', max_length=12, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]*$')]),
        ),
    ]
