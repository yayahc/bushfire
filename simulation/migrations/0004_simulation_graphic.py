# Generated by Django 4.2.5 on 2023-10-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0003_simulation_x_simulation_y'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation',
            name='graphic',
            field=models.ImageField(blank=True, null=True, upload_to='simulations/'),
        ),
    ]