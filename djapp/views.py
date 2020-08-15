from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseRedirect, request 
from djapp.models import *
from djproduct.models import *
from django.contrib import messages
from djapp.forms import *
import json 


def homepage(request):
    info = Information.objects.get(pk=True)
    category = Category.objects.all()
    slider = Product.objects.all().order_by('-id')[:5]
    # if we do -id it means in descending order (i.e products added at last will be displayed at first)..
    # [:5] limits the number of slider to be shown regardless how much we have added in admin panel

    new_products = Product.objects.filter(label='New').order_by('?')[:4] # filter new products 
    top_sells = Product.objects.filter(label__in=['Sale','Hot']).order_by('?')[:4] # filter hot and sale products (use __in[''])
    special_offers = Product.objects.filter(special_offer=True).order_by('?')[:4]  # ? means select product randomly 

    # To show categories panel in homepage only and hide in others page we do as:
    page = "homepage"
    context_var = {'info': info, 'page': page, 'category': category, 'slider': slider,'new_products':new_products,
                   'top_sells': top_sells, 'special_offers': special_offers}
    # context_var is a dictionary in key:value pair form
    # we can now call every fields inside Information model class by using key 'info' wherever required in template
    return render(request, 'index.html', context_var)


def aboutus(request):
    info = Information.objects.get(pk=True)
    category = Category.objects.all()
    context_var = {'info': info, 'category': category}
    return render(request, 'aboutus.html', context_var)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  # check the validation
            # it checks the fields and csrf_token
            # if both present then only allows to submit form
            data = Contact_Message()  # creates relation with model
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            # Sometimes it is important to know the ip address of an user to track his location ; for that we can do as
            data.user_ip_address = request.META.get('REMOTE_ADDR')
            data.save()  # saves to database
            messages.success(request, "Message has been sent Successfully!!!")
            return HttpResponseRedirect('/contact')  # redirect to contact page

    info = Information.objects.get(pk=True)
    category = Category.objects.all()
    form = ContactForm  # for rendering django modelform in template
    context_var = {'info': info, 'form': form, 'category': category}
    return render(request, 'contact.html', context_var)


def category_products(request, id, slug):
    category = Category.objects.filter(id=id)
    products = Product.objects.filter(category_id=id)
    context_var = {'category': category, 'products': products}
    return render(request, 'products.html', context_var)

# for search functionality
def search(request): 
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']  # get input data from form
            # get input data when user clicks certain category
            cat_id = form.cleaned_data['cat_id']

            if cat_id == 0:  # means if there is no any specific category ; represents all categories
                products = Product.objects.filter(title__icontains=query)
                # this query is same as of SQL:  SELECT * FROM product WHERE title =  '%query%'
                # if we use __icontains it means we ignore case sensitivity (meaning user can search in both uppercase and lowercase;still it shows the result)
            else:
                products = Product.objects.filter(
                    title__icontains=query, category_id=cat_id)

            category = Category.objects.all()
            context_var = {'category': category,
                           'products': products, 'query': query}
            return render(request, 'search_products.html', context_var)

    # redirects to Homepage if it doesnot find any POST method
    return HttpResponseRedirect('/')


# for autocompleting the search:
def search_auto_complete(request):
    if request.is_ajax():
        query = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=query)
        results = []
        for pro in products: 
            product_json = {} 
            product_json = pro.title 
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)    


# for single product detail 
def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    special_offers = Product.objects.filter(special_offer=True).order_by('?')[:4]
    images = Images.objects.filter(product_id=id)
    reviews = User_Reviews.objects.filter(product_id=id,status='True') # filter those user reviews of that specific product from database whose status is set to True in admin panel 
    context_var = {'category': category, 'product': product,'images':images,'reviews':reviews,'special_offers':special_offers}
    return render(request,'product_detail.html', context_var)

 
# for product user review:
def addcomment(request,id):
    url = request.META.get('HTTP_REFERER') # return back to the last url(after user submits review we have to return to same product page)
    if request.method == 'POST':
        form = User_ReviewsForm(request.POST)
        if form.is_valid():
            data = User_Reviews() #create relation with model 
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rating = form.cleaned_data['rating']
            data.user_ip_address = request.META.get('REMOTE_ADDR')
            data.product_id = id 
            current_user = request.user  
            data.user_id = current_user.id 
            data.save()
            messages.success(request, "Thank You for your interest !!! Review has been sent")
            return HttpResponseRedirect(url) 
      

    return HttpResponseRedirect(url) # if POST method is not found directly redirects to same product page 


