# Generated by Django 4.1.5 on 2023-01-22 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_rename_comments_comment_rename_curiosity_curiositie_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Curiositie',
            new_name='Curiosity',
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('curiosity', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.author'),
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
