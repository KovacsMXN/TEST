# Generated by Django 4.2.5 on 2024-01-12 03:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forklift', '0010_forkliftinspection_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterentry',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
