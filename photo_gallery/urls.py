from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_gallery_index, name='photo_gallery_index'),
    path('photo/<int:pk>/', views.photo_gallery_detail, name='photo_gallery_detail'),
    path('tag/<int:tag_pk>/', views.photo_gallery_filter_by_tags, name='photo_gallery_filter_by_tags'),
]
