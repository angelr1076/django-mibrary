# Generated by Django 2.0.2 on 2020-10-10 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_auto_20201010_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='name',
            new_name='type',
        ),
    ]
