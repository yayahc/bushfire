# Generated by Django 4.2.5 on 2023-10-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0007_alter_simulation_graphic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulation',
            name='graphic',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
