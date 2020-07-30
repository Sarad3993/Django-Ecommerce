from django.shortcuts import render , redirect 
from django.http import HttpResponse , HttpResponseRedirect 
from djproduct.models import *
from djuser.models import * 
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='/login') # checks for login
def index(request):
    category = Category.objects.all()
    current_user = request.user # access user session information 
    profile = UserProfileInfo.objects.get(user_id=current_user.id)
    context_var = {'category':category, 'profile':profile}
    return render(request,'user_account_info.html',context_var)
# for sign up: 
def signup_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            # Only proceed further if password is validated 
            # Now i have to check whether that username and email exists in my database already or not ; if it exits django will throw an error 
            if User.objects.filter(username=username).exists():
                messages.warning(request,"This username is already taken")
                return HttpResponseRedirect('/user/signup')
                
            elif User.objects.filter(email=email).exists():
                messages.warning(request,"This email is already registered")
                return HttpResponseRedirect('/user/signup')

            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password 
                )
                user.save() # sign up completed 
                messages.success(request,"Your account has been created")
                # Now since the account is created we must redirect the user to homepage 
                return HttpResponseRedirect('/user/login')
        else:
            messages.warning(request,"Passwords do not match")
                
            return HttpResponseRedirect('/user/signup')  

    category = Category.objects.all()
    context_var = {'category':category}
    return render(request,'signup.html',context_var)


# for login/sign in:
def login_form(request):
    if request.method == 'POST':
        username = request.POST['username'] # receives through form that user enters 
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