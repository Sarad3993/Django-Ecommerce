from django.shortcuts import render
from django.http import HttpResponse
from djapp.models import * 

def homepage(request):
    views = {} # create empty dictionary 
    # now we here call the settings for contact we created in models.py as a dictionary value 
    views['website_title'] = Contact_settings.objects.get(pk=1)
    # to show main category in homepage only 
    views['page'] = "homepage"
    # pk means primary key..
    return render(request,'index.html',views)

# def aboutus(request):
#     return HttpResponse("About Us Page")

def aboutus(request):
    views = {} 
    views['website_about'] = Contact_settings.objects.get(pk=1)
 
    return render(request,'aboutus.html',views)


def contact(request):
    views = {} 
    views['website_contact'] = Contact_settings.objects.get(pk=1) 
    return render(request,'contact.html',views)
