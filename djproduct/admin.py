from django.contrib import admin
from djproduct.models import *
from mptt.admin import DraggableMPTTAdmin

# Register models here

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'parent', 'status']
#     list_filter = ['status']

# Create a new CategoryAdmin
# First import DraggableMPTTAdmin inside it 
class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title','related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

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


# manage multiple images inside same page: 
# for that we should create a separate model of the fields that we want to attach inside another model
# and then use the inlines attribute and pass the class inside the list 
# note: Tabularinline class ---> like table rows(takes less space) WHILE stackedinline class ---> one row upon another piled up (takes more space)
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5  # denotes how many fields of images u want to add
    # can set this value as per your choice
    # Now 5 images field will be created inside each Product section

    # max_num = 5 (maximum no of extra fields that you need...can't create more than that if we use this attribute)

class ProductAdmin(admin.ModelAdmin):
    # list is displayed on the basis of above 3 categories
    list_display = ['title', 'category','label','items_in_stock','stock','status', 'image_tag'] 
    # list is filtered on the basis of this filed category
    list_filter = ['category','stock','label','status'] # on what basis to filter the list 
    readonly_fields = ('image_tag',) # admin cannot modify fields that are set to read_only 
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)} # for automatic slug creation when we type product name 
    list_editable = ['status','stock','label','items_in_stock'] # provides editing feature directly in products list page 
    # those attributes that you want to edit must be present in list_display 
    search_fields = ['title'] # for searching products inside admin panel(really useful if there are many products)
    
    
class User_ReviewsAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','status','create_at']
    list_filter = ['status']
    readonly_fields = ('product','subject','comment','rating','user','user_ip_address',)
    list_editable = ['status']


class CartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','price','discounted_price','total_price']
    list_filter = ['user']


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product','price','discounted_price','quantity','total_price','items_in_stock')
    can_delete = False
    extra = 0 

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','phone','city','total','status']
    list_display_links = ['first_name','last_name']
    list_filter = ['status']
    readonly_fields = ('first_name', 'last_name','address','city','country','phone','ip_address','code','total')
    exclude = ('user',) # to hide certain field
    can_delete = False 
    inlines = [OrderProductInline]
    list_editable = ['status']


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','price','discounted_price','quantity','total_price','items_in_stock','status']
    list_filter = ['user','status']
    list_editable = ['status']

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user','product']
    list_filter = ['user']

# note: We can also use the decorator to register the models like as:
# @admin.register(Wishlist)
# class WishlistAdmin(admin.ModelAdmin):
#     list_display = ['user','product']
#     list_filter = ['user']


admin.site.register(Category, CategoryAdmin2)

admin.site.register(Product, ProductAdmin)

admin.site.register(User_Reviews,User_ReviewsAdmin)

admin.site.register(Images)

admin.site.register(Cart,CartAdmin)

admin.site.register(Order,OrderAdmin)

admin.site.register(OrderProduct,OrderProductAdmin)

admin.site.register(Wishlist,WishlistAdmin)


