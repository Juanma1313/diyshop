# Generated by Django 3.2.25 on 2024-05-12 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructions',
            options={'ordering': ['title'], 'verbose_name_plural': 'Instructions'},
        ),
        migrations.AlterModelOptions(
            name='thing',
            options={'ordering': ['created_on'], 'verbose_name': 'DIY Project', 'verbose_name_plural': 'DIY Projects'},
        ),
    ]
