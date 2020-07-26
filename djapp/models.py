from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Contact_settings(models.Model):
    STATUS = (('True', 'True'), ('False', 'False'))
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=100)
    address = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=30)
    email = models.CharField(blank=True,max_length=100)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True,upload_to='images/') 
    facebook = models.CharField(blank=True,max_length=100)
    instagram = models.CharField(blank=True,max_length=100)
    twitter = models.CharField(blank=True,max_length=100)
    youtube = models.CharField(blank=True, max_length=100)
    about_us = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status=models.CharField(max_length=100,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
