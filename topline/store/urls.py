from django.urls import path

from .views import ProductListView, SettingsView

app_name = 'store'

urlpatterns = [
    path('settings/', SettingsView.as_view(), name='settings'),
    path('', ProductListView.as_view(), name='index'),
]
