# Generated by Django 2.0.2 on 2020-10-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_book_book_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/book/'),
        ),
    ]
