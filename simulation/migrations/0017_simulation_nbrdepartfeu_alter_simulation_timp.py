# Generated by Django 4.2.5 on 2023-10-03 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0016_simulation_cotesitefeu'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation',
            name='nbrDepartFeu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='timp',
            field=models.IntegerField(default=0),
        ),
    ]