from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="home"),
    path('yoga_videos/', views.yoga_videos, name="yoga_videos"),
    path('yoga_post/', views.yoga_post, name="yoga_post"),
    path('yoga_gallery/', views.yoga_gallery, name="yoga_gallery"),
    path('yoga_review/', views.yoga_review, name="yoga_review"),
    path('about_us/', views.about_us, name="about_us"),
]