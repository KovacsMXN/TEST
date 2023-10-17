# Generated by Django 4.2.5 on 2023-10-01 22:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_alter_storage_locations_add_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupluMX',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('copy', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='storage_locations',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
