from django.shortcuts import render


def contact_me(request):
    return render(request, 'contact_me.html')


def about_me(request):
    return render(request, 'about_me.html')
