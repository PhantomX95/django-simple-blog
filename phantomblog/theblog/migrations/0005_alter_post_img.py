# Generated by Django 5.1.4 on 2025-01-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, default='photos/no-image.png', null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
