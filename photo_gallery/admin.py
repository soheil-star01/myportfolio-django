from django.contrib import admin
from django import forms
from .models import Photo, PhotoTag


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        widgets = {
            'camera_model': forms.TextInput(attrs={'readonly': 'readonly'}),
            'lens_model': forms.TextInput(attrs={'readonly': 'readonly'}),
            'focal_length': forms.TextInput(attrs={'readonly': 'readonly'}),
            'iso': forms.TextInput(attrs={'readonly': 'readonly'}),
            'aperture': forms.TextInput(attrs={'readonly': 'readonly'}),
            'exposure_time': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


@admin.register(PhotoTag)
class PhotoTagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)
    search_fields = ('tag_name',)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    form = PhotoForm
    readonly_fields = ('camera_model', 'lens_model', 'focal_length', 'iso', 'aperture', 'exposure_time')
    filter_horizontal = ('tags',)


