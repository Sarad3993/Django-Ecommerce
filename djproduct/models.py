from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey



# model for category 
# In django there is a library called MPTT(Modified Preorder Tree Traversal) used for managing hierarchical database tables as a tree structure 
# If we have to work with category and subcategory using MPTT makes it easy 
# for that we first install MPTT, later import it and then inherit inside Category class 
class Category(MPTTModel):
    STATUS = (('True', 'True'),('False', 'False'))
    parent = TreeForeignKey('self',blank=True, null=True,related_name='children', on_delete=models.CASCADE)
# We must define a parent field which is a TreeForeignKey to 'self'. A TreeForeignKey is just a regular ForeignKey that renders form fields differently in the admin and a few other places.

    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    image=models.ImageField(upload_to='images/',blank=True)
    status=models.CharField(choices=STATUS,max_length=100)
    slug = models.SlugField(null=False, unique=True)

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']
#That MPTTMeta class adds some tweaks to django-mptt - in this case, just order_insertion_by. This indicates the natural ordering of the data in the tree

# Add this script to separate category and subcategory in admin panel dropdown menu: 
    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path) # category and subcategory are separated by /


# model for products/items  
class Product(models.Model):
    STATUS = (('True', 'True'),('False', 'False'))
    # Many to one relation 
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    image=models.ImageField(upload_to='images/', blank=True) 
    price = models.FloatField()
    amount=models.IntegerField()
    min_amount=models.IntegerField()
    details= RichTextUploadingField()
    slug = models.SlugField(unique=True,null=False)
    status=models.CharField(max_length=100,choices=STATUS) 
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # method to create a fake table  in read only mode
    # for this we have to import mark_safe which is done above 
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return "" 

# Models for products image gallery: 
class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)# creates relation between Product table and Image table 
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.title


