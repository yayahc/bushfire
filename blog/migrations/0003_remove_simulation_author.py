# Generated by Django 4.2.5 on 2023-09-30 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_post_simulation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulation',
            name='author',
        ),
    ]
