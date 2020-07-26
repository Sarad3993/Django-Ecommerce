from django.contrib import admin
from djapp.models import *


class InformationAdmin(admin.ModelAdmin):
    list_display = ['title','company','update_at','status'] 

admin.site.register(Information,InformationAdmin)