from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cart


class CartAdmin(admin.ModelAdmin):
    """
    Отображение корзины в админ панели
    """
    list_display = ('user', 'product', 'quantity', 'get_photo')
    list_filter = ('user', 'product')
    search_fields = ('user', 'product')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('quantity',)

    def get_photo(self, obj: Cart):
        if obj.product.photos:
            return mark_safe(f'<img src="{obj.product.photos.url}" alt="{obj.product.name}" width="60">')

    get_photo.short_description = 'Миниатюра'


admin.site.register(Cart, CartAdmin)
