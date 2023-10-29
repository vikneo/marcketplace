from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', db_index=True)
    is_active = models.BooleanField(default=False, verbose_name='Активность')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'categories'
        ordering = ['name', 'slug']
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', db_index=True)
    description = models.TextField(verbose_name='Описание')
    feature = models.TextField(verbose_name='Характеристики', blank=True)
    photos = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    available = models.BooleanField(default=False, verbose_name='Доступность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self) -> str:
        return f'{self.name}'

    def get_absolute_url(self) -> str:
        return reverse('store:detail', kwargs={'slug': self.slug})

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name = 'product'
        verbose_name_plural = 'products'
