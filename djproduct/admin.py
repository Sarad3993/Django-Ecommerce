from django.contrib import admin

from djproduct.models import *

# Register models here 
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent','status']
    list_filter = ['status']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','status'] # list is displayed on the basis of above 3 categories 
    list_filter = ['category'] # list is filtered on the basis of this filed category 

admin.site.register(Category,CategoryAdmin)

admin.site.register(Product,ProductAdmin)