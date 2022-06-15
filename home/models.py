from django.db import models
from django.core.files import File
# Create your models here.

class UploadVideo(models.Model):
    video_file = models.FileField(upload_to='videos/')
    title = models.CharField(max_length = 200, null = True)


class UploadImage(models.Model):
    image_file = models.FileField(upload_to='images/')
    title = models.CharField(max_length = 400, null = True)

