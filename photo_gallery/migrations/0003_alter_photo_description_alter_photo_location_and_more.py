# Generated by Django 5.1 on 2024-09-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_gallery', '0002_alter_photo_original_image_alter_photo_resized_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
