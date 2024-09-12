from ckeditor.widgets import CKEditorWidget
from django.contrib import admin

from .models import BlogPost, PostCategory

admin.site.register(PostCategory)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_posted')
    formfield_overrides = {
        BlogPost.content: {'widget': CKEditorWidget},
    }
    # search_fields = ('category__category',)
