from django.shortcuts import render
from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'store/product_list.html'
