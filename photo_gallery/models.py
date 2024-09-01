import os

from PIL import Image
from django.db import models
from PIL.ExifTags import TAGS

from utils import resize_image


class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=50)
    datetime_posted = models.DateTimeField("date published")
    camera_model = models.CharField(max_length=50)
    lens_model = models.CharField(max_length=50)
    focal_length = models.IntegerField()
    iso = models.IntegerField(default=200)
    aperture = models.FloatField()
    exposure_time = models.FloatField()
    original_image = models.ImageField(upload_to="photo_gallery/%Y/%m/%d")
    resized_image = models.ImageField(upload_to="photo_gallery/%Y/%m/%d", editable=False)
    thumbnail_image = models.ImageField(upload_to="photo_gallery/%Y/%m/%d", editable=False)

    def save(self, *args, **kwargs):
        if self.original_image:
            img = Image.open(self.original_image)
            file_name = os.path.basename(self.original_image.name)
            exif_data = img._getexif()
            self.thumbnail_image = resize_image(
                img, f'tmb_{file_name}', max_width=100, max_height=100
            )
            self.resized_image = resize_image(
                img, f'std_{file_name}', max_height=500, max_width=500
            )

            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    if tag_name == 'Model':
                        self.camera_model = value
                    elif tag_name == 'LensModel':
                        self.lens_model = value
                    elif tag_name == 'FocalLength':
                        self.focal_length = float(value)
                    elif tag_name == 'ISOSpeedRatings':
                        self.iso = int(value)
                    elif tag_name == 'FNumber':
                        self.aperture = int(value)
                    elif tag_name == 'ExposureTime':
                        self.exposure_time = float(value)

        super().save(*args, **kwargs)
