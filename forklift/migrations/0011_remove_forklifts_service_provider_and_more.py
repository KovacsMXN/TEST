# Generated by Django 4.2.5 on 2023-11-13 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forklift', '0010_alter_forklifts_service_provider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forklifts',
            name='service_provider',
        ),
        migrations.AddField(
            model_name='forklifts',
            name='service_provider',
            field=models.ManyToManyField(blank=True, null=True, to='forklift.forkliftserviceproviders'),
        ),
    ]