# Generated by Django 5.1.4 on 2025-02-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0017_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
