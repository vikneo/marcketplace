from django.urls import path

from .views import ProductListView

app_name = 'store'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
]
