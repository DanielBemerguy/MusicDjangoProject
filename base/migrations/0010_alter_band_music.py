# Generated by Django 4.1.5 on 2023-02-05 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_rename_music_message_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='music',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
