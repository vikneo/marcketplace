from typing import Any

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.views.decorators.http import require_POST, require_GET
from requests import Request

from .models import Cart
from store.models import Product


def get_object_cart(request: Request, _id: Cart):
    carts = Cart.objects.filter(user=request.user, id=_id)
    return carts


def add_product_to_cart(request: Request, slug: Product, quantity: int = 1) -> HttpResponse:
    """
    Добавление товара в корзину

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
        if 1 <= cart.quantity < 21:
            cart.quantity += quantity
            cart.save()
    return HttpResponseRedirect(current_page)


def take_product_is_cart(request: Request, _id: Cart, quantity: int = 1) -> HttpResponseRedirect:
    """
    Добавление товара в корзину

    :param _id:
    :param quantity:
    :param request:
    :return:
    """
    cart = get_object_cart(request, _id).first()

    if 1 < cart.quantity <= 21:
        cart.quantity -= quantity
    else:
        cart.quantity = quantity
    cart.save()
    return redirect('cart:index')


# @require_POST
def delete_product_from_cart(request: Request, _id: Cart) -> HttpResponseRedirect:
    """
    Удаление продукта из корзины

    :param request:
    :param _id:
    :return:
    """
    cart = get_object_cart(request, _id)
    cart.delete()
    return redirect('cart:index')


def clear_cart(request: Request) -> HttpResponseRedirect:
    """
    Очистка корзины от всех продуктов

    :param request:
    :return:
    """
    carts = Cart.objects.filter(user=request.user)
    carts.all().delete()
    return redirect('cart:index')


class CartViewList(generic.ListView):
    """
    Отображение списка корзины
    """
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
