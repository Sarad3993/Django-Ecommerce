from django.shortcuts import render , redirect 
from django.http import HttpResponse
from djproduct.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

 
@login_required(login_url='/user/login') # check login
def add_to_cart(request,id):
    url = request.META.get('HTTP_REFERER') # get last accessed url from system 
    current_user = request.user # access user session information

    product_check = Cart.objects.filter(product_id=id) # check product is in cart or not 
   
    if product_check:
        # now we create a variable (check) to check whether our product is in cart or not 
        check = 1 # product is in cart
    else:
        check = 0  # product is not in cart 

    if request.method == "POST": # from product detail page 
        form = CartForm(request.POST)
        if form.is_valid():
            if check == 1: # update cart (as there is already that product in cart)
                data = Cart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity'] # add new quantity to existing quantity in cart 
                data.save()
            else: # Insert new items to Cart if check == 0 (no items in cart)
                data = Cart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        
        messages.success(request,"Product added to Cart")
        return redirect(url)

    else: # if there is no POST request (from homepage add to cart)
        if check == 1: # update Cart if there is same product already
            data = Cart.objects.get(product_id=id)
            data.quantity += 1 # just adds one product at a time; cuz this value is not sent through form ; so adding must be done one by one 
            data.save()
        
        else: # insert to Cart if there is no items in cart 
            data = Cart()
            data.user_id = current_user.id
            data.product_id = id 
            data.quantity = 1
            data.save()

        messages.success(request,"Product added to Cart")
        return redirect(url)

    
def cart(request):
    category = Category.objects.all()
    current_user = request.user # access user session information 
    carts = Cart.objects.filter(user_id=current_user.id) # show only current user's items in cart 
    total = 0
    for cart in carts:
        total += cart.product.price * cart.quantity
    context_var = {'category':category,'carts':carts,'total':total}
    return render(request,'cart.html',context_var) 

# to delete items from cart 
@login_required(login_url='/user/login') # Check login
def delete_from_cart(request,id):
    Cart.objects.filter(id=id).delete()
    messages.success(request, "Item has been deleted from Cart!")
    return redirect("/product/cart")

    
            


    