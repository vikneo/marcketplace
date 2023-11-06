from django.contrib.auth.models import User
from django.db import models

from store.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'Корзина {self.user} | Продукт {self.product}'

    def sum(self):
        return self.quantity * self.product.price

    class Meta:
        db_table = 'cart'
        ordering = ['-created_at']
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
