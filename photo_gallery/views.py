from django.shortcuts import render
from .models import Photo, PhotoTag


def photo_gallery_index(request):

    photos = Photo.objects.all()
    context = {'photos': photos}

    return render(request, 'photo_gallery/index.html', context)


def photo_gallery_filter_by_tags(request, tag_pk):

    photos = Photo.objects.filter(tags__pk=tag_pk)
    tag_name = PhotoTag.objects.get(pk=tag_pk).tag_name
    context = {'photos': photos, 'tag_name': tag_name}

    return render(request, 'photo_gallery/index.html', context)


def photo_gallery_detail(request, pk):

    photo = Photo.objects.get(pk=pk)
    tags = photo.tags.all()
    context = {'photo': photo, 'tags': tags}

    return render(request, 'photo_gallery/detail.html', context)

