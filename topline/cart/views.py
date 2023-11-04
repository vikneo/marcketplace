from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.decorators.http import require_POST, require_GET
from requests import Request

from .models import Cart
from store.models import Product


@require_GET
def add_product_to_cart(request: Request, slug: Product, quantity: int = 1) -> HttpResponseRedirect:
    """
    Добавление товара в корзину

    :param add:
    :param quantity:
    :param request:
    :param slug:
    :return:
    """
    current_page = request.META.get('HTTP_REFERER')
    user = request.user
    product = Product.objects.get(slug=slug)
    carts = Cart.objects.filter(user=user, product=product)

    if not carts.exists():
        Cart.objects.create(user=user, product=product, quantity=quantity)
        return HttpResponseRedirect(current_page)
    else:
        cart = carts.first()
        cart.quantity += quantity
        cart.save()
        return HttpResponseRedirect(current_page)


def del_product_is_cart(request: Request, _id: Cart, quantity: int = 1) -> HttpResponseRedirect:
    """
    Добавление товара в корзину

    :param _id:
    :param quantity:
    :param request:
    :return:
    """
    current_page = request.META.get('HTTP_REFERER')
    user = request.user
    carts = Cart.objects.filter(user=user, id=_id)

    cart = carts.first()
    if 1 < cart.quantity < 21:
        cart.quantity -= quantity
        cart.save()
        return HttpResponseRedirect(current_page)
    else:
        cart.quantity = quantity
        cart.save()
        return HttpResponseRedirect(current_page)


# @require_POST
def delete_product_from_cart(request: Request, _id: Cart) -> HttpResponseRedirect:
    """

    :param request:
    :param _id:
    :return:
    """
    current_page = request.META.get('HTTP_REFERER')
    user = request.user
    cart = Cart.objects.filter(user=user, id=_id)
    cart.delete()
    return HttpResponseRedirect(current_page)


class CartViewList(generic.ListView):
    model = Cart
    context_object_name = 'carts'
    template_name = 'cart/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        carts = Cart.objects.filter(user=user)
        total_quantity = sum([cart.quantity for cart in carts])
        total_summ = sum([cart.sum() for cart in carts])

        context['total_quantity'] = total_quantity
        context['total_summ'] = total_summ

        return context
