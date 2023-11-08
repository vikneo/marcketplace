from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse

from .cart import CartView
from store.models import Product


class CartListView(generic.TemplateView):
    template_name = 'cart/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'carts': CartView(self.request)
            }
        )
        return context


def add_product_to_cart(request: WSGIRequest, slug: Product) -> HttpResponse:
    """
    Добавление товара в корзину

    :param request:
    :param slug:
    :return:
    """
    cart = CartView(request)
    product = get_object_or_404(Product, slug=slug)
    cart.add_product(product, update=False)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_product(request: WSGIRequest, slug: Product) -> HttpResponseRedirect:
    """
    Добавить одну единицу товара в корзине

    :param request:
    :param slug:
    :return:
    """
    cart = CartView(request)
    cart.add(get_object_or_404(Product, slug=slug))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def take_product(request: WSGIRequest, slug: Product) -> HttpResponseRedirect:
    """
    Убрать одну единицу товара в корзине

    :param _id:
    :param quantity:
    :param request:
    :return:
    """
    cart = CartView(request)
    cart.take(get_object_or_404(Product, slug=slug))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# @require_POST
def delete_product_from_cart(request: WSGIRequest, slug: Product) -> HttpResponseRedirect:
    """
    Удаление продукта из корзины

    :param request:
    :param _id:
    :return:
    """
    cart = CartView(request)
    cart.remove(get_object_or_404(Product, slug=slug))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def clear_cart(request: WSGIRequest) -> HttpResponseRedirect:
    """
    Очистка корзины от всех продуктов

    :param request:
    :return:
    """
    cart = CartView(request)
    cart.clear()
    return redirect('cart:index')

