from django.contrib import admin
from .models import StaticPage

# Register your models here.


@admin.register(StaticPage)
class StaticContentAdmin(admin.ModelAdmin):
    pass
