# Generated by Django 5.1.4 on 2025-02-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_writer',
            field=models.BooleanField(default=False),
        ),
    ]
