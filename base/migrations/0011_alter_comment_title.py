# Generated by Django 4.1.5 on 2023-01-22 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_title_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.title'),
        ),
    ]
