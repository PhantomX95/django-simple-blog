# Generated by Django 5.1.4 on 2025-01-10 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, default='photos/default.png', null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
