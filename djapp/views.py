from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect , request
from djapp.models import * 
from django.contrib import messages

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
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid(): # check the validation
        # it checks the fields and csrf_token 
        # if both present then only allows to submit form
            data = Contact_Message() # creates relation with model 
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            # Sometimes it is important to know the ip address of an user to track his location ; for that we can do as 
            data.user_ip_address = request.META.get('REMOTE_ADDR')
            data.save() # saves to database 
            messages.success(request,"Message has been sent Successfully!!!") # import messages above 
            return HttpResponseRedirect('/contact') # redirect to contact page 

    info = Information.objects.get(pk=1)
    form = ContactForm # for rendering django form in template 
    context_var = {'info':info,'form':form} 
    return render(request,'contact.html',context_var)

