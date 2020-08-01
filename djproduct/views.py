from django.shortcuts import render
from django.http import HttpResponse

def cart(request):
    return HttpResponse("This is Cart Page")   


def add_to_cart(request,id):
    url = request.META.get('HTTP_REFERER') # get last accessed url 
    current_user = request.user # access user session information

    product_check = Cart.objects.filter(product_id=id) # check product is in cart or not 
    # if product_check:
    #     check = 1 # product is in cart
    # else:
    #     check = 0 # product is not in cart 

    