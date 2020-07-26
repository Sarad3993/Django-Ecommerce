from django.contrib import admin

from djproduct.models import *

# Register models here 
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent','status']
    list_filter = ['status']

# manage multiple images in same page in django admin panel
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5 # denotes how many images u want to add
    # can set this value as per your choice 
    # Now 5 images field will be created inside each Product section

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','status','image_tag'] # list is displayed on the basis of above 3 categories 
    list_filter = ['category'] # list is filtered on the basis of this filed category 
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline] 

admin.site.register(Category,CategoryAdmin)

admin.site.register(Product,ProductAdmin)

admin.site.register(Images)

