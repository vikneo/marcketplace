from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.text import slugify


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


class Banner(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', db_index=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', db_index=True)
    description = models.TextField(verbose_name='Описание')
    link = models.URLField(max_length=255, verbose_name='Ссылка', blank=True)
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Отредактирована', auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.name = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        db_table = "banners"
        ordering = ["name", "slug"]
        verbose_name = 'banner'
        verbose_name_plural = 'banners'
