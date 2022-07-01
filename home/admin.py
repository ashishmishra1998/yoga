from django.contrib import admin
from home.models import *

# Register your models here.
class upload(admin.ModelAdmin):
    pass

class uploadimg(admin.ModelAdmin):
    pass

class uploadgallery(admin.ModelAdmin):
    pass

class contact(admin.ModelAdmin):
    pass

class customer_review(admin.ModelAdmin):
    pass

class about_us(admin.ModelAdmin):
    pass


admin.site.register(UploadVideo, upload)
admin.site.register(UploadPost, uploadimg)
admin.site.register(Contact, contact)
admin.site.register(UploadGallery, uploadgallery)
admin.site.register(About_us, about_us)
admin.site.register(Customer_reviews, customer_review)