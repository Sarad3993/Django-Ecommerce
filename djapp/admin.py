from django.contrib import admin
from djapp.models import *
from django.contrib.auth.models import Group


class InformationAdmin(admin.ModelAdmin):
    list_display = ['title','company','update_at','status'] 

class Contact_MessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','update_at','status'] 
    # if i do this i cannot edit the customers/users message cuz that is not my information...message is sent to admin panel in read only mode..
    readonly_fields = ('name','email','subject','message','user_ip_address')
    list_filter =['status'] 
    list_editable = ['status'] # for editing directly in list display page of admin panel 


admin.site.register(Information,InformationAdmin)

admin.site.register(Contact_Message,Contact_MessageAdmin)


# for removing unnecessary app in django dashboard: 
admin.site.unregister(Group)