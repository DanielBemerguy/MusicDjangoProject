# Generated by Django 4.1.5 on 2023-01-22 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_title_author_author_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Title',
        ),
    ]
