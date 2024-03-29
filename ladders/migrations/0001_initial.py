# Generated by Django 4.2.5 on 2024-02-12 13:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LattersBrands',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('imagen', models.ImageField(null=True, upload_to='ladders/brands/banners/')),
            ],
        ),
        migrations.CreateModel(
            name='LattersMaterials',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LattersStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ladders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='ladders/images/')),
                ('clave', models.CharField(max_length=255)),
                ('modelo', models.CharField(max_length=255)),
                ('agregado', models.DateTimeField(default=django.utils.timezone.now)),
                ('pasos', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ladders.lattersbrands')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ladders.lattersmaterials')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ladders.lattersstatus')),
            ],
        ),
    ]
