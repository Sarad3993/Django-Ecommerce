from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from djproduct.models import *
from djuser.models import * 
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

# Create your views here.

def signup_form(request):
    category = Category.objects.all()
    context_var = {'category':category}
    return render(request,'signup.html',context_var)


# for login/sign in 
def login_form(request):
    if request.method == 'POST':
        username = request.POST['username'] # receives through form that user types 
        password = request.POST['password']
        user = authenticate(request,username=username,password=password) # checks in the database for authentication; first username comes from user through form and second is of database 
        # Now if authentication is successful; then login is executed by django and redirected to home(/)
        if user is not None:
            login (request, user)
            # for user profile image:
            current_user = request.user # asks for current logged in user's id from auth_user table 
            user_profile = UserProfileInfo.objects.get(user_id=current_user.id) # now since UserProfileInfo has inherited auth_user table ; it contains id of every user as user_id
            request.session['user_image'] = user_profile.image.url # image is displayed within that session 
            return HttpResponseRedirect('/') 
        else:
            messages.warning(request,"Login Error!! Username or Password incorrect")
            return HttpResponseRedirect('/user/login') # redirected to login page 
    category = Category.objects.all()
    context_var = {'category':category}
    return render(request,'login.html',context_var)



# for log out/ sign out:

def logout_function(request):
    logout(request)
    return HttpResponseRedirect('/')