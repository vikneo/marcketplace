from django.shortcuts import render
from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'store/product_list.html'


class SettingsView(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'admin/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            title="Settings",
            has_permission=True,
        )
        return context
