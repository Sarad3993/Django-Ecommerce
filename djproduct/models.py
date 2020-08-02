from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.urls import reverse 
from django.contrib.auth.models import User 
from django.forms import ModelForm ,TextInput, Textarea


# Model for category 
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

    def get_category_url(self):
        return reverse('category_detail',kwargs={'slug':self.slug})

# Add this script to separate category and subcategory in admin panel dropdown menu: 
    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1]) # category and subcategory are separated by / 


# Model for products/items  
class Product(models.Model):
    STATUS = (('True', 'True'),('False', 'False'))
    LABEL = (('Hot', 'Hot'), ('Sale', 'Sale'), ('New', 'New'))
    STOCK = (('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock'))

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    image=models.ImageField(upload_to='images/', blank=True) 
    brand = models.CharField(max_length=200,blank=True)
    price = models.FloatField()
    items_in_stock = models.IntegerField(default=0)  
    discounted_price = models.FloatField(blank=True)
    details= RichTextUploadingField()
    slug = models.SlugField(unique=True,null=False)
    status=models.CharField(max_length=100,choices=STATUS) 
    label = models.CharField(max_length=100,choices=LABEL,blank=True)
    stock = models.CharField(max_length=100,choices=STOCK,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # method to create a fake table  in read only mode
    # for this we have to import mark_safe which is done above 
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe(f'<img src="{self.image.url}" height="55"/>')
        else:
            return ""
    image_tag.short_description = 'Image' # title for images in admin products section  

# Model for products image gallery: 
class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)# creates relation between Product table and Image table 
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.title


# Model for User reviews/comments:
class User_Reviews(models.Model):
    STATUS= (('New','New'),('Read','Read'),('True','True')) 
    product = models.ForeignKey(Product,on_delete=models.CASCADE) # we have relation with Product model 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=400,blank=True)
    comment = models.TextField()
    rating = models.IntegerField(default=1)
    user_ip_address = models.CharField(max_length=50,blank=True)
    status=models.CharField(max_length=100,choices=STATUS,default="New")
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


# for user review/comments input form: 
class User_ReviewsForm(ModelForm):
    class Meta:
        model = User_Reviews
        fields = ['subject','comment','rating']



# for shop cart create a new model:
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    # for showing price in admin panel
    @property
    def price(self):
        return self.product.price

    # for showing discounted price:
    @property
    def discounted_price(self):
        return self.product.discounted_price

    # for total price (with/without discount)
    @property 
    def total_price(self):
        if self.product.discounted_price:
            return self.quantity * self.product.discounted_price
        else:
            return self.quantity * self.product.price

# for adding quantity inside Quantity field in product details page 
class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']