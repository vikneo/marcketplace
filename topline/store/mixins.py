from django.contrib import admin

from .models import Product, Banner


class ChangeListMixin:
    def get_change_list_admin(self, **kwargs):
        model = Banner
        context = kwargs
        context = dict(list(context.items()) + list(admin.site.each_context(self.request).items()))
        context.update(
            opts=model._meta
        )
        return context
