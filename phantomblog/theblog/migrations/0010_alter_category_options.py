# Generated by Django 5.1.4 on 2025-01-18 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_remove_post_tags_delete_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
