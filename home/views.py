from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Home.html')

def yoga_videos(request):
    return render(request, 'Videos.html')

def yoga_post(request):
    return render(request, 'post.html')

def yoga_gallery(request):
    return render(request, 'gallery.html')

def yoga_review(request):
    return render(request, 'review.html')

def about_us(request):
    return render(request, 'About.html')
