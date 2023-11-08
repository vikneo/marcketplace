from django.urls import path

from.views import add_product_to_cart, CartListView, add_product, take_product, delete_product_from_cart, clear_cart

app_name = 'cart'

urlpatterns = [
    path('', CartListView.as_view(), name='index'),
    path('<slug:slug>/', add_product_to_cart, name='cart_add_product'),
    path('take/<slug:slug>/', take_product, name='cart_take'),
    path('add/<slug:slug>/', add_product, name='cart_add'),
    path('delete/<slug:slug>/', delete_product_from_cart, name='cart_delete'),
    path('cart/clear/', clear_cart, name='cart_clear'),
]
