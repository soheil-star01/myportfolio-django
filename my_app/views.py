from django.shortcuts import render,get_object_or_404
from blog.models import BlogPost
from photo_gallery.models import Photo
from .models import StaticPage

def contact_me(request):
    Email=StaticPage.objects.filter(slug='contact-me-email').first()
    email_content=Email.content if Email else ''
    linkedin=StaticPage.objects.filter(slug='contact-me-linkedin').first()
    linkedin_content=linkedin.content if linkedin else ''
    githup=StaticPage.objects.filter(slug='contact-me-githup').first()
    githup_content =githup.content if githup else ''
    upwork=StaticPage.objects.filter(slug='contact-me-upwork').first()
    upwork_content= upwork.content if upwork else ''


    return render(request, 'contact_me.html',{"Email":email_content,"Linkedin":linkedin_content,"Upwork":upwork_content,"Githup":githup_content})


def about_me(request):
    page = StaticPage.objects.filter(slug='about-me').first()
    content = page.content if page else ''  # Empty string if no page found
    return render(request, 'about_me.html', {'content': content})

def main_index(request):
    page = StaticPage.objects.filter(slug='home').first()
    content = page.content if page else ''  # Empty string if no page found
    last_blog_post = BlogPost.objects.last()
    last_photo_gallery = Photo.objects.last()

    context = {
        'last_blog_post': last_blog_post,
        'last_photo_gallery': last_photo_gallery,
    }

    return render(request, 'index.html', context)
