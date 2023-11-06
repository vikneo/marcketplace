from urllib.request import Request

from django.http import HttpResponseRedirect, HttpResponse

from cart.models import Cart
from store.models import Product


class CartView(object):

    def __init__(self, request: Request):
        self.cart = Cart.objects
        self.quantity = 1
        self.user = request.user
        self.request = request
        self.current_page = request.META.get('HTTP_REFERER')

    def add(self, slug: Product, quantity: int = 1) -> HttpResponse:
        """
        Добавление товара в корзину

        :param quantity:
        :param slug:
        :return:
        """
        self.cart.filter(user=self.user, product=slug)
        if not self.cart.exists():
            Cart.objects.create(user=self.user, product=slug, quantity=quantity)

    def counting_products(self):
        cart = self.cart.first()
        if 1 <= cart.quantity <= 21:
            if self.plus_product:
                cart.quantity += self.quantity
            elif self.minus_product:
                cart.quantity -= self.quantity
            cart.save()

    def plus_product(self):
        cart = self.cart.first()
        if 1 <= cart.quantity <= 21:
            cart.quantity += self.quantity
            cart.save()

    def minus_product(self, slug: Product):
        cart = self.cart.first()
        if 1 <= cart.quantity < 21:
            cart.quantity += self.quantity
            cart.save()
#
# current_page = request.META.get('HTTP_REFERER')
# user = request.user
# carts = Cart.objects.filter(user=user, id=_id)
#
# cart = carts.first()
# if 1 < cart.quantity < 21:
#     cart.quantity -= quantity
#     cart.save()
#     return HttpResponseRedirect(current_page)
# else:
#     cart.quantity = quantity
#     cart.save()
#     return HttpResponseRedirect(current_page)