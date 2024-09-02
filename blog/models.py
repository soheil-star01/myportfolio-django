from PIL import Image
from django.db import models
from utils import resize_image


class PostCategory(models.Model):
    category = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.category


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    date_posted = models.DateTimeField("date published")
    summarized_content = models.TextField()
    original_image = models.ImageField(upload_to="media/blog/%Y/%m/%d")
    resized_image = models.ImageField(upload_to="media/blog/%Y/%m/%d", editable=False)
    thumbnail_image = models.ImageField(upload_to="media/blog/%Y/%m/%d", editable=False)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        img = Image.open(self.original_image)

        self.thumbnail_image = resize_image(
            img, f'tmb_{self.original_image.name}', max_width=300, max_height=300
        )
        self.resized_image = resize_image(
            img, f'std_{self.original_image.name}', max_height=700, max_width=700
        )

        super(BlogPost, self).save(*args, **kwargs)
