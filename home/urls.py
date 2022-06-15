from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="home"),
    path('yoga_videos/', views.index, name="yoga_videos"),
    path('yoga_post/', views.index, name="yoga_post"),
    path('yoga_gallery/', views.index, name="yoga_gallery"),
    path('yoga_review/', views.index, name="yoga_review"),
    path('about_us/', views.index, name="about_us"),
]