# Generated by Django 2.0.2 on 2020-10-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_delete_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
