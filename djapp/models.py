from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea

# Lets create a model called Information that contains different fields which can be used wherever required
class Information(models.Model):
    STATUS = (('True', 'True'), ('False', 'False'))
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=100)
    address = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=30)
    email = models.CharField(blank=True,max_length=100)
    icon = models.ImageField(blank=True,upload_to='images/') 
    facebook = models.CharField(blank=True,max_length=100)
    instagram = models.CharField(blank=True,max_length=100)
    twitter = models.CharField(blank=True,max_length=100)
    youtube = models.CharField(blank=True, max_length=100)
    about_us = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    status=models.CharField(max_length=100,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
 
 
# Create models for contact form:

class Contact_Message(models.Model):
    STATUS= (('New','New'),('Read','Read'),('Closed','Closed'))
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=400)
    message = models.TextField()
    status = models.CharField(max_length=100,choices=STATUS, default ="New")
    user_ip_address = models.CharField(max_length=50,blank=True)
    note = models.CharField(max_length=100,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 


# Also lets add a modelform that has relation with above Contact form
# we have many other fields in above model class ; but we want to manage only four fields through the contact form ; for that we have to create a separate class and inherit ModelForm in it.... otherwise there are many fields above and we cannot manage all through front-end contact form so it gives an error...
class ContactForm(ModelForm): # u have to import Modelform first
    class Meta:
        model = Contact_Message # ContactForm has relation with Contact_Message Model 
        fields = ['name', 'email', 'subject','message']
        widgets = {
            'name'   : TextInput(attrs={'class': 'input','placeholder':'Enter your full name'}),
            'email'   : TextInput(attrs={'class': 'input','placeholder':'Enter your email Id  '}),
            'subject' : TextInput(attrs={'class': 'input','placeholder':'Enter your subject'}),
            'message' : Textarea(attrs={'class': 'input','placeholder':'Enter your message'}),
        }
