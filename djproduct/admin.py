from django.contrib import admin
from djproduct.models import *
from mptt.admin import DraggableMPTTAdmin

# Register models here


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['status']

# Create a new CategoryAdmin
# First import DraggableMPTTAdmin inside it 
class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title','related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    # prepopulated_fields = {'slug': ('title',)}
    # inlines = [CategoryLangInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(qs,Product,'category','products_cumulative_count',cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,Product,'category','products_count',cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products(in tree)'


# manage multiple images in same page in django admin panel

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5  # denotes how many images u want to add
    # can set this value as per your choice
    # Now 5 images field will be created inside each Product section


class ProductAdmin(admin.ModelAdmin):
    # list is displayed on the basis of above 3 categories
    list_display = ['title', 'category', 'status', 'image_tag']
    # list is filtered on the basis of this filed category
    list_filter = ['category'] # on what basis to filter the list 
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]


admin.site.register(Category, CategoryAdmin2)

admin.site.register(Product, ProductAdmin)

admin.site.register(Images)