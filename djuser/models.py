from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe 
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_no = models.CharField(blank=True,max_length=50)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100,blank=True)
    zip_code = models.CharField(max_length=50,blank=True)
    country = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='images/users/',blank=True)
    
    def __str__(self):
        return self.user.username

    # just showing up username in user profile section of admin panel is not enough ; for that we create a separate function to display other user details as well 
    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + '['+self.user.username+']'

    # to show user profile photo in admin panel:
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe(f'<img src="{self.image.url}" height="60"/>')
        else:
            return ""
    image_tag.short_description = 'Profile Image'


