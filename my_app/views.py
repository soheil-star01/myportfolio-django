from django.shortcuts import render
from blog.models import BlogPost
from photo_gallery.models import Photo


def contact_me(request):
    return render(request, 'contact_me.html')


def about_me(request):
    return render(request, 'about_me.html')


def main_index(request):

    last_blog_post = BlogPost.objects.last()
    last_photo_gallery = Photo.objects.last()

    context = {
        'last_blog_post': last_blog_post,
        'last_photo_gallery': last_photo_gallery,
    }

    return render(request, 'index.html', context)
