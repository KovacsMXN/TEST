# Generated by Django 4.2.5 on 2023-11-23 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment_brands',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment_Locations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(default='10162d', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fa_number', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('serial', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='equipment/main/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment_brands')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment_locations')),
            ],
        ),
    ]
