from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.contrib import messages
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

def sendmail(request, email, name, message):
    email = email
    print(email)
    ctx = {
        'name': name,
        'email' : email,
        'message' : message 
    }
    message = get_template('contact_mail.html').render(ctx)
    msg = EmailMessage(
        'Contact Inquiry!',
         message,
        'ashishsharad007@gmail.com',
        [email],
    )
    msg.content_subtype ="html"# Main content is now text/html
    msg.send()
    

@csrf_exempt
def about_us(request): 
    if request.method == "POST":
        print('Called')
        name =  request.POST.get('fname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        sendmail(request, email, name,message)
        data = Contact.objects.create(name=name, email=email ,message=message)
        data.save()
        messages.success(request, 'Thank You')

    return render(request, 'About.html')
