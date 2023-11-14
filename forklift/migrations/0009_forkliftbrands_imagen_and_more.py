# Generated by Django 4.2.5 on 2023-11-13 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forklift', '0008_alter_forkliftowners_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='forkliftbrands',
            name='imagen',
            field=models.ImageField(null=True, upload_to='forklifts/brands/banners/'),
        ),
        migrations.AddField(
            model_name='forkliftserviceproviders',
            name='imagen',
            field=models.ImageField(null=True, upload_to='forklifts/serviceproviders/banners/'),
        ),
    ]
