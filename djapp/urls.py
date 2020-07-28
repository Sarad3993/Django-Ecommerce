from django.urls import path
from djapp.views import *

app_name = 'djapp'

urlpatterns = [
    path('',homepage,name='homepage'),
    path('aboutus/',aboutus,name="aboutus"),
    path('contact/',contact,name="contact"),
    path('category/<int:id>/<slug:slug>',category_products,name="category_products"),
    path('search/',search,name="search"),
    path('search_auto_complete/',search_auto_complete,name="search_auto_complete")

]
 
