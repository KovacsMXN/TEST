# Generated by Django 4.2.5 on 2023-10-31 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0005_alter_equipment_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='imagen',
            field=models.ImageField(null=True, upload_to='equipment/main/'),
        ),
    ]
