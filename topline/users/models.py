from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    sale = models.IntegerField()
    avatar = models.ImageField()
    name_store = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    viewed_orders = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default='user')

    class Meta:
        db_table = 'Profiles'
        ordering = ['id', 'user']
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        permissions = (
            ('store', 'has offers for sale'),
            ('user', 'all site users'),
            ('buyer', 'only buys goods'),
            ('admin', 'manages the site'),
        )