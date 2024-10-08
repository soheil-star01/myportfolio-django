# Generated by Django 5.1 on 2024-09-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='original_image',
            field=models.ImageField(upload_to='blog/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='resized_image',
            field=models.ImageField(editable=False, upload_to='blog/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail_image',
            field=models.ImageField(editable=False, upload_to='blog/%Y/%m/%d'),
        ),
    ]
