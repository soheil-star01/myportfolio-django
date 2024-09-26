# Generated by Django 5.1 on 2024-09-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='original_image',
            field=models.ImageField(upload_to='photo_gallery/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='resized_image',
            field=models.ImageField(editable=False, upload_to='photo_gallery/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='thumbnail_image',
            field=models.ImageField(editable=False, upload_to='photo_gallery/%Y/%m/%d'),
        ),
    ]
