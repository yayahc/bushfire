# Generated by Django 4.2.5 on 2023-10-03 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0012_delete_limiteinitialox_rename_yenr_simulation_yenreg_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chaleurspecfeulbed',
            old_name='chaleur_spec_fuel_bed',
            new_name='chaleur_spec_feul_bed',
        ),
        migrations.RemoveField(
            model_name='simulation',
            name='nbreVegetation',
        ),
    ]
