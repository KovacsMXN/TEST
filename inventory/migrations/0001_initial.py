# Generated by Django 4.2.5 on 2024-03-05 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MotorsBrands',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('imagen', models.ImageField(null=True, upload_to='inventory/motors/brands/')),
            ],
        ),
        migrations.CreateModel(
            name='Motors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=255)),
                ('volts', models.CharField(max_length=255)),
                ('amps', models.CharField(max_length=255)),
                ('horsepower', models.CharField(max_length=255)),
                ('phase', models.CharField(max_length=255)),
                ('hz', models.CharField(max_length=255)),
                ('maxrpm', models.CharField(max_length=255)),
                ('sf', models.CharField(max_length=255)),
                ('framenumero', models.CharField(max_length=255)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='inventory/motors/')),
                ('nameplate', models.ImageField(blank=True, null=True, upload_to='inventory/motors/nameplates/')),
                ('stock', models.IntegerField()),
                ('stock_target', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.motorsbrands')),
            ],
        ),
    ]
