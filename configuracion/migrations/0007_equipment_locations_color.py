# Generated by Django 4.2.5 on 2023-11-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0006_alter_equipment_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment_locations',
            name='color',
            field=models.CharField(default='10162d', max_length=10),
        ),
    ]
