from django.urls import path
from . import views

urlpatterns = [
    path('contact_me/', views.contact_me, name='contact_me'),
    path('about_me/', views.about_me, name='about_me'),
]
