from django.contrib import admin

from .models import BlogPost, PostCategory

admin.site.register(PostCategory)


@admin.register(BlogPost)
class PhotoTagAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category__category',)
