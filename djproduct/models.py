from django.db import models

# model for category 
class Category(models.Model):
    STATUS = (('True', 'True'),('False', 'False'))
    parent = models.ForeignKey('self',blank=True, null=True,related_name='children', on_delete=models.CASCADE)

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
    details=models.TextField()
    slug = models.SlugField()
    status=models.CharField(max_length=100,choices=STATUS) 
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

