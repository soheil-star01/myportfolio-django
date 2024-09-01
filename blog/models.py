from PIL import Image
from django.db import models
from utils import resize_image


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    date_posted = models.DateTimeField("date published")
    summarized_content = models.TextField()
    original_image = models.ImageField(upload_to="blog/%Y/%m/%d")
    resized_image = models.ImageField(upload_to="blog/%Y/%m/%d", editable=False)
    thumbnail_image = models.ImageField(upload_to="blog/%Y/%m/%d", editable=False)

    def save(self, *args, **kwargs):
        img = Image.open(self.original_image)

        self.thumbnail_image = resize_image(
            img, f'tmb_{self.original_image.name}', max_width=100, max_height=100
        )
        self.resized_image = resize_image(
            img, f'std_{self.original_image.name}', max_height=500, max_width=500
        )

        super(BlogPost, self).save(*args, **kwargs)
