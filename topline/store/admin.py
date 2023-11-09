from django.contrib import admin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import path, reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.views.generic import DetailView

from .models import Category, Product, Banner


class ProductAdminInline(admin.StackedInline):
    model = Product
    extra = 0


class BannerAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'get_html_images', 'is_active']
    list_filter = ['is_active', ]
    search_fields = ['name', ]
    prepopulated_fields = {'slug': ('name', )}
    list_editable = ['is_active', ]
    readonly_fields = ('get_html_images', )

    def get_html_images(self, obj: Banner):
        """
        В панели администратора,
        ссылка на изображение отображается в виде картинки размером 60х 60.
        """
        if obj.product:
            return mark_safe(f'<img src="{obj.product.photos.url}" alt=""width="60">')
        else:
            return 'not url'

    get_html_images.short_description = "Изображение"


class CategoryAdmin(admin.ModelAdmin):

    inlines = [
        ProductAdminInline,
    ]
    list_display = ['name', 'slug', 'is_active']
    list_filter = ['is_active', ]
    search_fields = ['name', ]
    prepopulated_fields = {'slug': ('name', )}
    list_editable = ['is_active', ]


class OrderDetailView(PermissionRequiredMixin, DetailView):
    model = 'Order'
    permission_required = "products.view_order"
    template_name = 'store/order_detail.html'


class ProductAdmin(admin.ModelAdmin):

    list_display = ['category', 'name', 'get_html_photo', 'price', 'available', 'created_at', 'updated_at']
    list_display_links = ['name', 'category']
    list_filter = ['category', 'available', ]
    readonly_fields = ('get_html_photo', )
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ['name', ]
    list_editable = ['available', ]

    def get_html_photo(self, obj: Product) -> str:
        if obj.photos:
            return mark_safe(f'<img src="{obj.photos.url}" width="60" alt="{obj.name}">')

    get_html_photo.short_description = 'Изображение'


class OrderAdmin(admin.ModelAdmin):
    pass
    # TODO добавить модель Заказы (Orders)
    # list_display = ['detail']
    #
    # def get_urls(self):
    #     url = super().get_urls()
    #     new_url = [
    #         path(
    #           "<slug:slug>/detail/", self.admin_site.admin_view(ProductDetailView.as_view()), name="product_detail"
    #         ),
    #     ]
    #     return new_url + url
    #
    # def detail(self, obj: Product):
    #     url = reverse('admin:product_detail', args=[obj.slug])
    #     return format_html(f'<a href="{url}">{obj.name}</a>')
    #
    # detail.short_description = 'Детали'


admin.site.register(Banner, BannerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
