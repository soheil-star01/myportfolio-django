from django.shortcuts import render
from .models import Photo


def photo_gallery_index(request):
    photos = Photo.objects.all()
    context = {'photos': photos}

    return render(request, 'photo_gallery/index.html', context)


def photo_gallery_detail(request, pk):
    photo = Photo.objects.get(pk=pk)
    context = {'photo': photo}
    return render(request, 'photo_gallery/detail.html', context)

