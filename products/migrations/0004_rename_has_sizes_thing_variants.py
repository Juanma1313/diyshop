# Generated by Django 3.2.25 on 2024-05-21 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240513_1129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thing',
            old_name='has_sizes',
            new_name='variants',
        ),
    ]
