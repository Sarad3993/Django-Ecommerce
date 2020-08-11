from django.urls import path
from djproduct.views import *

app_name = 'djproduct'

urlpatterns = [
    path('cart/',cart,name="cart"),
    path('add_to_cart/<int:id>',add_to_cart,name="add_to_cart"),
    path('delete_from_cart/<int:id>',delete_from_cart,name="delete_from_cart"),
    path('order_product/',order_product, name='order_product'),

]


