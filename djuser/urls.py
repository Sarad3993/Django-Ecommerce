from django.urls import path 
from djuser.views import * 


app_name = 'djuser'

urlpatterns = [
    path('',index, name='index'),
    path('login/',login_form,name ='login'),
    path('logout/',logout_function,name='logout'),
    path('signup/',signup_form,name='signup'),
    path('update_profile/',user_profile_update,name='update_profile'),
    path('change_password/',user_password_change,name='change_password'),

]

