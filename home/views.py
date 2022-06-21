from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, 'Home.html')

def yoga_videos(request):
    data = UploadVideo.objects.all()
    return render(request, 'Videos.html',{'data' : data})

def yoga_post(request):
    data = UploadPost.objects.all()
    print('Called')
    print(data)
    return render(request, 'post.html',{'data' : data})
    

def yoga_gallery(request):
    data = UploadGallery.objects.all()
    return render(request, 'gallery.html',{'data' : data})
    
def yoga_review(request):
    return render(request, 'review.html')

@csrf_exempt
def about_us(request): 
    if request.method == "POST":
        print('Called')
        name =  request.POST.get('fname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name,email,message)

    return render(request, 'About.html')
