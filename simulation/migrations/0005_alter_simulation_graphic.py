# Generated by Django 4.2.5 on 2023-10-01 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0004_simulation_graphic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulation',
            name='graphic',
            field=models.CharField(max_length=1000),
        ),
    ]