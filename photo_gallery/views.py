from django.shortcuts import render
from .models import Photo, PhotoTag


def photo_gallery_index(request):

    photos = Photo.objects.all()
    context = {'photos': photos}

    return render(request, 'photo_gallery/index.html', context)


def photo_gallery_filter_by_tags(request, tag_pk):

    photos = Photo.objects.filter(tags__pk=tag_pk)
    context = {'photos': photos}

    return render(request, 'photo_gallery/index.html', context)


def photo_gallery_detail(request, pk):

    photo = Photo.objects.get(pk=pk)
    tags = photo.tags.all()
    tags = [tag.tag_name for tag in tags]
    context = {'photo': photo, 'tags': ', '.join(tags)}

    return render(request, 'photo_gallery/detail.html', context)

