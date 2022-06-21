from django.db import models
from django.core.files import File
from ckeditor.fields import RichTextField
# Create your models here.

class UploadVideo(models.Model):
    video_file = models.FileField(upload_to='videos/')
    # title = models.CharField(max_length = 200, null = True)
    title = RichTextField()

class UploadPost(models.Model):
    image_file = models.FileField(upload_to='images/')
    title = RichTextField()

class UploadGallery(models.Model):
    image_file = models.FileField(upload_to='images/')
    title = RichTextField() 

class Contact(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=254,null=True, blank=True )
    message = models.CharField(max_length=500, null=True, blank=True)
