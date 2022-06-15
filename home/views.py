from django.shortcuts import render
from .models import UploadVideo
# Create your views here.

def index(request):
    return render(request, 'Home.html')

def yoga_videos(request):
    print('Called')
    data = UploadVideo.objects.all()
    print(data)
    return render(request, 'Videos.html',{'data' : data})

def yoga_post(request):
    return render(request, 'post.html')

def yoga_gallery(request):
    return render(request, 'gallery.html')

def yoga_review(request):
    return render(request, 'review.html')

def about_us(request):
    return render(request, 'About.html')
