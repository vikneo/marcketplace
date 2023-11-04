from django.urls import path

from.views import add_product_to_cart, CartViewList, del_product_is_cart, delete_product_from_cart, clear_cart

app_name = 'cart'

urlpatterns = [
    path('', CartViewList.as_view(), name='index'),
    path('cart-add/delete/<int:_id>/', delete_product_from_cart, name='cart_delete'),
    path('cart-add/aply/<int:_id>/', del_product_is_cart, name='cart_del'),
    path('cart-add/<slug:slug>/', add_product_to_cart, name='cart_add'),
    path('cart/clear/', clear_cart, name='cart_clear'),
]
