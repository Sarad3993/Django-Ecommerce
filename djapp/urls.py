from django.urls import path
from djapp.views import *

app_name = 'djapp'

urlpatterns = [
    path('',homepage,name='homepage'),
    path('aboutus/',aboutus,name="aboutus"),
    path('contact/',contact,name="contact")
]

