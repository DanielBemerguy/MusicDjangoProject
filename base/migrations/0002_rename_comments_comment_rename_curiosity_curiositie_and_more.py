# Generated by Django 4.1.5 on 2023-01-22 02:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Curiosity',
            new_name='Curiositie',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='curiosity',
            new_name='curiositie',
        ),
    ]