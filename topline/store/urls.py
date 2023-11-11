from django.urls import path

from .views import ProductListView, SettingsView
from .views import ClearCacheAll, ClearCacheBanner, ClearCacheCart, SiteName,site_name

app_name = 'store'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('clear-all/', ClearCacheAll.as_view(), name='clear_all_cache'),
    path('clear-banner/', ClearCacheBanner.as_view(), name='clear_banner_cache'),
    path('clear-cart/', ClearCacheCart.as_view(), name='clear_cart_cache'),
    path('site-name/', site_name, name='site_name'),
]
