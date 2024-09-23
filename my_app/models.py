from django.db import models

class StaticPage(models.Model):
    slug = models.SlugField(unique=True, help_text="Unique identifier for the page (e.g., 'home', 'about-me', 'contact-me-(email,linkedin,etc)')")
    content = models.TextField(help_text="Content of the page (HTML allowed)")

    def __str__(self):
        return self.slug
