from django.urls import path 
from djuser.views import * 


app_name = 'djuser'

urlpatterns = [
    path('',index, name='index'),
    path('login/',login_form,name ='login'),
    path('logout/',logout_function,name='logout'),
    path('signup/',signup_form,name='signup'),
    
]

