from django.shortcuts import render
from .models import BlogPost


def blog_index(request):

    posts = BlogPost.objects.all().order_by("-date_posted")
    context = {
        "posts": posts,
    }

    return render(request, "blog/index.html", context)


def blog_detail(request, pk):

    post = BlogPost.objects.get(pk=pk)
    context = {
        "post": post
    }

    return render(request, "blog/detail.html", context)
