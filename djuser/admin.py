from django.contrib import admin
from djuser.models import * 

# Register your models here.


class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ['user_name','address','phone_no','city','zip_code','country','image_tag']


    # to modify fields according to our wish
    # fieldsets attribute us better than fields attribute 
    # here your can manage different fields on the basis of title 
    fieldsets = (
        ("Personal Details", {
            'fields': (
                'user','phone_no','address','city','zip_code','country','image'
            ),
        }),
    )

    readonly_fields = ['user','phone_no','address','city','zip_code','country','image']

admin.site.register(UserProfileInfo,UserProfileInfoAdmin)

# install django suit using below command
# pip install https://github.com/darklow/django-suit/tarball/v2