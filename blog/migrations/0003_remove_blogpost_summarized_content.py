# Generated by Django 5.1 on 2024-09-28 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_original_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='summarized_content',
        ),
    ]
