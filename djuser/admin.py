from django.contrib import admin
from djuser.models import * 

# Register your models here.


class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ['user_name','address','phone_no','city','zip_code','country','image_tag']


admin.site.register(UserProfileInfo,UserProfileInfoAdmin)