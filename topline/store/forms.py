from django import forms


class SiteNameForm(forms.Form):
    """
    
    """
    title_site = forms.CharField(max_length=100, help_text="Название", label='Новое название')


class CacheSettingForm(forms.Form):
    """
    Класс представляет форму для, установки или обновления времени кеширования:
        время кеширования детализации продукта,
        время кеширования содержание корзины,
        время кеширования отображение баннера.
    """
    cache_time_banner = forms.IntegerField(label='Время кеширование Баннера')
    cache_time_cart = forms.IntegerField(label='Время кеширование Корзины')
    cache_time_product_detail = forms.IntegerField(label='Время кеширование страницы продукта')
