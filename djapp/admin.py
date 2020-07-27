from django.contrib import admin
from djapp.models import *


class InformationAdmin(admin.ModelAdmin):
    list_display = ['title','company','update_at','status'] 

class Contact_MessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','update_at','status'] 
    # if i do this i cannot edit the customers/users message cuz that is not my information...message is sent to admin panel in read only mode..
    readonly_fields = ('name','email','subject','message','user_ip_address')
    list_filter =['status'] 

admin.site.register(Information,InformationAdmin)

admin.site.register(Contact_Message,Contact_MessageAdmin)