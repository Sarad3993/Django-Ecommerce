from django.urls import path 
from djuser.views import * 

app_name = 'djuser'

urlpatterns = [
    path('',index,name ='index')
]