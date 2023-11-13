from typing import Any
from django.contrib import messages
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import SiteNameForm, CacheSettingForm
from .mixins import ChangeListMixin
from .models import Product
from .configs import settings


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'store/product_list.html'


# Представления для страницы настроек в админ панели

class SettingsView(ChangeListMixin, generic.ListView):
    """
    Класс SettingsView отображает страницу с настройками
    """
    model = Product
    template_name = 'admin/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        change_list = self.get_change_list_admin(title="Settings")
        return dict(list(context.items()) + list(change_list.items()))


class ClearCacheAll(ChangeListMixin, generic.TemplateView):
    """
    Класс ClearCacheAll позволяет очистить весь кеш сайта
    """
    template_name = 'admin/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cache.clear()
        messages.success(self.request, 'Кеш полностью очищен.')  # Добавление сообщения для действия
        change_list = self.get_change_list_admin(title="Settings")
        return dict(list(context.items()) + list(change_list.items()))

    def dispatch(self, request, *args, **kwargs):
        if cache:
            super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy("store:settings"))


class ClearCacheBanner(ChangeListMixin, generic.TemplateView):
    """
    Класс ClearCacheBanner позволяет очистить кеш Баннера
    """
    template_name = 'admin/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cache.delete("banners")
        messages.success(self.request, 'Кеш баннера очищен.')
        change_list = self.get_change_list_admin(title="Settings")
        return dict(list(context.items()) + list(change_list.items()))

    def dispatch(self, request, *args, **kwargs):
        if cache:
            super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy("store:settings"))


class ClearCacheCart(ChangeListMixin, generic.TemplateView):
    """
    Класс ClearCacheCart позволяет очистить кеш Корзины
    """
    template_name = 'admin/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cache.delete("cart")
        messages.success(self.request, 'Кеш корзины очищен.')
        change_list = self.get_change_list_admin(title="Settings")
        return dict(list(context.items()) + list(change_list.items()))

    def dispatch(self, request, *args, **kwargs):
        if cache:
            super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy("store:settings"))


class ClearCacheProductDetail(ChangeListMixin, generic.TemplateView):
    """

    """
    template_name = 'admin/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cache.delete("cart")
        messages.success(self.request, 'Кеш продукта очищен.')
        change_list = self.get_change_list_admin(title="Settings")
        return dict(list(context.items()) + list(change_list.items()))

    def dispatch(self, request, *args, **kwargs):
        if cache:
            super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy("store:settings"))


class SiteName(ChangeListMixin, generic.TemplateView):
    """
    Класс SiteName позволяет задать новое название интернет магазина
    """
    template_name = 'admin/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        messages.success(self.request, 'Название магазина успешно изменено')
        change_list = self.get_change_list_admin(
            title="site name",
        )
        return dict(list(context.items()) + list(change_list.items()))

    def post(self, request):
        title_site = request.POST.get('title_site')
        if title_site:
            settings.set_site_name(title_site)
            messages.success(self.request, 'Название магазина успешно изменено')
        else:
            messages.error(self.request, 'Поле не должно быть пустым')
        return HttpResponseRedirect(reverse_lazy('store:settings'))


class CacheSetupBannerView(ChangeListMixin, generic.TemplateView):
    """
    Класс CacheSetupBannerView позволяет задать или обновить время кеширования Баннера
    """
    template_name = 'admin/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        messages.success(self.request, 'Название магазина успешно изменено')
        change_list = self.get_change_list_admin(
            title="site name",
        )
        return dict(list(context.items()) + list(change_list.items()))

    def post(self, request):
        cache_time_banner = request.POST.get('cache_time_banner')
        if cache_time_banner:
            settings.set_cache_banner(cache_time_banner)
            messages.success(self.request, 'Время кеширование Баннера установлено')
        else:
            messages.error(self.request, 'Поле не должно быть пустым')
        return HttpResponseRedirect(reverse_lazy('store:settings'))
    

class CacheSetupCartView(ChangeListMixin, generic.TemplateView):
    """
    Класс CacheSetupCartView позволяет задать или обновить время кеширования Корзины
    """
    template_name = 'admin/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        messages.success(self.request, 'Название магазина успешно изменено')
        change_list = self.get_change_list_admin(
            title="site name",
        )
        return dict(list(context.items()) + list(change_list.items()))

    def post(self, request):
        cache_time_cart = request.POST.get('cache_time_cart')
        if cache_time_cart:
            settings.set_cache_cart(cache_time_cart)
            messages.success(self.request, 'Время кеширование Корзины установлено')
        else:
            messages.error(self.request, 'Поле не должно быть пустым')
        return HttpResponseRedirect(reverse_lazy('store:settings'))


class CacheSetupBProdDetailView(ChangeListMixin, generic.TemplateView):
    """
    Класс CacheSetupBProdDetailView позволяет задать или обновить время кеширования детальной информации продукта
    """
    template_name = 'admin/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        messages.success(self.request, 'Название магазина успешно изменено')
        change_list = self.get_change_list_admin(
            title="site name",
        )
        return dict(list(context.items()) + list(change_list.items()))

    def post(self, request):
        cache_time_prod_detail = request.POST.get('cache_time_prod_detail')
        if cache_time_prod_detail:
            settings.set_cache_product_detail(cache_time_prod_detail)
            messages.success(self.request, 'Время кеширование детализации продукта установлено')
        else:
            messages.error(self.request, 'Поле не должно быть пустым')
        return HttpResponseRedirect(reverse_lazy('store:settings'))
