from django.urls import path

from .views import ProductListView, SettingsView
from .views import (
    ClearCacheAll, 
    ClearCacheBanner, 
    ClearCacheCart, 
    ClearCacheProductDetail, 
    SiteName, 
    CacheSetupBannerView,
    CacheSetupCartView, 
    CacheSetupBProdDetailView
    )

app_name = 'store'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('clear-all/', ClearCacheAll.as_view(), name='clear_all_cache'),
    path('clear-banner/', ClearCacheBanner.as_view(), name='clear_banner_cache'),
    path('clear-cart/', ClearCacheCart.as_view(), name='clear_cart_cache'),
    path('clear-product-detail/', ClearCacheProductDetail.as_view(), name='clear_product_detail'),
    path('site-name/', SiteName.as_view(), name='site_name'),
    path('cache-time-banner/', CacheSetupBannerView.as_view(), name='cache_time_banner'),
    path('cache-time-cart/', CacheSetupCartView.as_view(), name='cache_time_cart'),
    path('cache-time-prod-detail/', CacheSetupBProdDetailView.as_view(), name='cache_time_prod_detail'),
]
