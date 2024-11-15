from django_ckeditor_5.widgets import CKEditor5Widget
from django.contrib import admin

from .models import BlogPost, PostCategory

admin.site.register(PostCategory)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_posted')
    formfield_overrides = {
        BlogPost.content: {'widget': CKEditor5Widget},
    }
