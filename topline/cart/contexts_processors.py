from .cart import CartView


def cart(request):
    return {'cart': CartView(request)}
