# Generated by Django 4.2.5 on 2023-12-14 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forklift', '0009_alter_forkliftinspection_des1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='forkliftinspection',
            name='valid',
            field=models.BooleanField(default='1'),
            preserve_default=False,
        ),
    ]