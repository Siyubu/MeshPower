# Generated by Django 3.1.2 on 2020-10-11 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='serial_numbe',
            new_name='serial_number',
        ),
    ]
