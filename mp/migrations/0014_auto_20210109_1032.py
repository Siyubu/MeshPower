# Generated by Django 3.1.2 on 2021-01-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0013_auto_20201221_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='status',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Unfixable', 'Unfixable'), ('In Progress', 'In Progress')], max_length=200, verbose_name='status'),
        ),
    ]
