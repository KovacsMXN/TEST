# Generated by Django 4.2.5 on 2023-11-14 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forklift', '0012_forklifts_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='forkliftowners',
            name='address',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forkliftowners',
            name='contact_person',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forkliftowners',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forkliftowners',
            name='phone_number',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forkliftowners',
            name='service_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forkliftowners',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]