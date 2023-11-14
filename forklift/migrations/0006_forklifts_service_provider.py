# Generated by Django 4.2.5 on 2023-11-12 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forklift', '0005_forklifts_clave'),
    ]

    operations = [
        migrations.AddField(
            model_name='forklifts',
            name='service_provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='forklifts', to='forklift.forkliftserviceproviders'),
        ),
    ]