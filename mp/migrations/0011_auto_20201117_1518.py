# Generated by Django 3.1.2 on 2020-11-17 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0010_auto_20201111_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='conclusion',
            new_name='status',
        ),
    ]