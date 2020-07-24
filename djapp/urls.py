from django.urls import path
from djapp.views import *

app_name = 'djapp'

urlpatterns = [
    path('',homepage,name='homepage'),
]

