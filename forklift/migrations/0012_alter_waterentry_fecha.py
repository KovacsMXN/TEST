# Generated by Django 4.2.5 on 2024-01-12 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forklift', '0011_alter_waterentry_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterentry',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
