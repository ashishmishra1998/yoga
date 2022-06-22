from django.db import models
from django.core.files import File
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags
# Create your models here.

class UploadVideo(models.Model):
    video_file = models.FileField(upload_to='videos/')
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
    

class Contact(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=254,null=True, blank=True )
    message = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    
