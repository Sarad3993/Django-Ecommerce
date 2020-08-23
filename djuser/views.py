from django.shortcuts import render , redirect 
from django.http import HttpResponse , HttpResponseRedirect 
from djproduct.models import *
from djuser.models import * 
from django.contrib.auth import authenticate, login , logout , update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from djuser.forms import *
from django.contrib.auth.forms import PasswordChangeForm


# for user account / user profile info section:
@login_required(login_url='/user/login') # checks for login
def index(request):
    category = Category.objects.all()
    current_user = request.user # access user session information 
    profile = UserProfileInfo.objects.get(user_id=current_user.id)
    context_var = {'category':category, 'profile':profile}
    return render(request,'user_account_info.html',context_var)


# for sign up: 
def signup_form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            # Only proceed further if password is validated 
            # Now i have to check whether that username and email exists in my database already or not ; if it exits django will throw an error 
            if User.objects.filter(username=username).exists():
                messages.warning(request,"This username is already taken")
                return  redirect('/user/signup')
                
            elif User.objects.filter(email=email).exists():
                messages.warning(request,"This email is already registered")
                return redirect('/user/signup')

            else:
                user = User.objects.create_user(
                    first_name= first_name,
                    last_name = last_name, 
                    username = username,
                    email = email,
                    password = password 
                )
                user.save() # sign up completed 

                user = authenticate(request,username=username,password=password)
                login(request,user) # automatic login for signed up  users

                # To Fetch data of current logged in user from auth_user table to user_profile table automatically 
                current_user = request.user 
                data = UserProfileInfo() 
                data.user_id=current_user.id
                data.image="images/users/user.jpg" # for default image of user profile ; user can change it later while updating his/her profile 
                data.save()  
                # messages.success(request, 'Your account has been created!') 
                return redirect('/') # redirects to home after signup and auto login  
        else:
            messages.warning(request,"Passwords do not match")
            return redirect('/user/signup')  

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
            return redirect('/') 
        else: #return error message if login is not successful 
            messages.warning(request,"Login Error!! Username or Password incorrect")
            return redirect('/user/login') # redirected to login page

    category = Category.objects.all()
    context_var = {'category':category}
    return render(request,'login.html',context_var)


# for log out/ sign out:
def logout_function(request):
    logout(request)
    return redirect('/')


# for user profile update:
@login_required(login_url='/user/login') # checks for login
def user_profile_update(request):
    if request.method == 'POST': 
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user's data sent from form 
        profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofileinfo) # one to one relation of user_profile data with user data 

        if user_form.is_valid() and profile_form.is_valid(): # check validation
            user_form.save() # saves to database 
            profile_form.save()
            messages.success(request, 'Your account has been updated successfully!')
            return redirect('/user') # redirect to user profile page so that user can see the changes made 
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=request.user.userprofileinfo) 
        context_var = {'category': category,'user_form': user_form,'profile_form': profile_form }
        return render(request, 'user_profile_update.html', context_var)


# for user's password change: 
@login_required(login_url='/user/login')
def user_password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST) # we have to import PasswordChangeForm form django auth 
        if form.is_valid(): 
            user = form.save()
            update_session_auth_hash(request, user) # session info is changed after password is changed 
            messages.success(request, 'Your password is successfully updated!')
            return redirect('/user')
        else:
            messages.error(request, 'Please correct the error below: <br>'+ str(form.errors)) 
            return redirect('/user/change_password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        context_var = {'category':category,'form': form}
        return render(request, 'user_password_change.html',context_var) 


