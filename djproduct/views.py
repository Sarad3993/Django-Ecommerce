from django.shortcuts import render , redirect 
from django.http import HttpResponse , HttpResponseRedirect 
from djproduct.models import *
from djuser.models import * 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string 


# to add products into cart 
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


# for displaying all cart items 
def cart(request):
    category = Category.objects.all()
    current_user = request.user # access user session information 
    carts = Cart.objects.filter(user_id=current_user.id) # show only current user's items in cart 
    total = 0 
    for tot in carts:
        if tot.discounted_price:
            total += tot.product.discounted_price * tot.quantity
        else:
            total += tot.product.price * tot.quantity
    context_var = {'category':category,'carts':carts, 'total':total}
    return render(request,'cart.html',context_var) 


# to delete items from cart:
@login_required(login_url='/user/login') # Check login
def delete_from_cart(request,id):
    Cart.objects.filter(id=id).delete()
    messages.success(request, "Item has been deleted from Cart!")
    return redirect("/product/cart")


# for order:
def order_product(request):
    category = Category.objects.all() # category section is present in all pages so we include here too
    current_user = request.user # Access current user's session information 
    carts = Cart.objects.filter(user_id=current_user.id)
    total = 0                            
    for tot in carts:
        if tot.discounted_price:
            total += tot.product.discounted_price * tot.quantity 
        else:
            total += tot.product.price * tot.quantity 

    if request.method == 'POST': # for data entry through form 
        form = OrderForm(request.POST)
        if form.is_valid():

            data = Order()
            data.first_name = form.cleaned_data['first_name'] 
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.phone = form.cleaned_data['phone']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            # data.user_id = current_user.id
            data.total = total 
            data.ip_address = request.META.get('REMOTE_ADDR') 
            order_code= get_random_string(10).upper() # generate 10 digits random code in uppercase 
            data.code =  order_code 
            data.save() 

            # Move cart items to Order Product itn=ems 
            carts = Cart.objects.filter(user_id=current_user.id)
            for cart in carts: 
                detail = OrderProduct()
                detail.order_id= data.id  
                detail.product_id= cart.product_id
                detail.user_id = current_user.id
                detail.quantity = cart.quantity
                detail.price = cart.product.price 
                detail.items_in_stock = cart.product.items_in_stock
                detail.save()                

                # Reduce quantity of each products from items_in_stock field if products are already sold 
                product = Product.objects.get(id=cart.product_id)
                product.items_in_stock -= cart.quantity
                product.save()
              
 
            Cart.objects.filter(user_id=current_user.id).delete() # Clear & Delete Cart after placing order 
            request.session['cart_items']= 0 
            messages.success(request, "Your Order has been completed. Thank you!! ")
            return render(request, 'order_completed.html',{'order_code':order_code,'category': category}) 
        else:
            messages.warning(request, form.errors)
            return redirect("/product/order_product")

    form= OrderForm()
    profile = UserProfileInfo.objects.get(user_id=current_user.id)
    context_var = {'carts': carts, 'category': category,  'total': total, 'form': form, 'profile': profile }
    return render(request, 'order_products.html', context_var)


