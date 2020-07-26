from django.shortcuts import render
from django.http import HttpResponse
from djapp.models import * 

def homepage(request):
    info = Information.objects.get(pk=1)
    # pk means primary key 

    # To show main category section in homepage only we do as: 
    page = "homepage"
    context_var = {'info':info,'page':page}
     # dictionary in key:value pair form 
     # we can now call every fields inside Information model class by using key 'info' wherever required in template
   
    return render(request,'index.html',context_var)

def aboutus(request):
    info = Information.objects.get(pk=1)
    context_var = {'info':info}
    return render(request,'aboutus.html',context_var)


def contact(request):
    info = Information.objects.get(pk=1)
    context_var = {'info':info} 
    return render(request,'contact.html',context_var)
