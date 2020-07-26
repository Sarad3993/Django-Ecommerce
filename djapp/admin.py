from django.contrib import admin
from djapp.models import *


class Contact_settingsAdmin(admin.ModelAdmin):
    list_display = ['title','company','update_at','status'] 

admin.site.register(Contact_settings,Contact_settingsAdmin)