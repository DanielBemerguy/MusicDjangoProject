# Generated by Django 4.1.5 on 2023-01-22 03:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_rename_curiosity_author_about_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='title',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='room',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='curiosity',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curiosity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.curiosity')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
