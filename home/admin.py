from django.contrib import admin
from home.models import *

# Register your models here.
class upload(admin.ModelAdmin):
    pass

class uploadimg(admin.ModelAdmin):
    pass

admin.site.register(UploadVideo, upload)
admin.site.register(UploadImage, uploadimg)