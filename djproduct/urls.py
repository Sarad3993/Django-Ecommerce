from django.urls import path
from djproduct.views import *

app_name = 'djproduct'

urlpatterns = [
    path('cart/',cart,name="cart"),
    path('add_to_cart/<int:id>',add_to_cart,name="add_to_cart"),
]