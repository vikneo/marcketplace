from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, Banner


class ProductAdminInline(admin.TabularInline):
    model = Product
    extra = 0


class ProductAdminStaked(admin.StackedInline):
    model = Product
    extra = 0


class BannerAdmin(admin.ModelAdmin):

    inlines = [
        ProductAdminInline,
        ProductAdminStaked
    ]

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
        print(obj.products_banners.first())
        if obj.products_banners.first().photos:
            return mark_safe(f'<img src="{obj.products_banners.first().photos.url}" width="60">')
        else:
            return 'not url'

    get_html_images.short_description = "Изображение"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active']
    list_filter = ['is_active', ]
    search_fields = ['name', ]
    prepopulated_fields = {'slug': ('name', )}
    list_editable = ['is_active', ]


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
    get_html_photo.allow_tags = True


admin.site.register(Banner, BannerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
