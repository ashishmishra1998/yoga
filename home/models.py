# from xxlimited import Null
from urllib import request
from django.db import models
from django.core.exceptions import ValidationError
from django.core.files import File
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags
from django.contrib import messages
# Create your models here.

class UploadVideo(models.Model):
    video_url = models.CharField(max_length=100, null=True, blank=True)
    title = RichTextField()

    def __str__(self):
         return strip_tags(self.title)

class UploadPost(models.Model):
    image_file = models.FileField(upload_to='images/')
    title = RichTextField()

    def __str__(self):
         return strip_tags(self.title)
       
    

class UploadGallery(models.Model):
    image_file = models.FileField(upload_to='images/')
    title = RichTextField() 

    def __str__(self):
        return strip_tags(self.title)

    class Meta:
        verbose_name_plural = "uploadGallery"
    

class Contact(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=254,null=True, blank=True )
    message = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Customer_reviews(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    message = RichTextField(null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "customer_reviews"


class About_us(models.Model):
    content = RichTextField(null = True)

    def save(self, *args, **kwargs):
        if not self.pk and About_us.objects.exists():
            messages.error(request, 'There can be only 1 About Us')
        return super(About_us, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "about_us"

   

