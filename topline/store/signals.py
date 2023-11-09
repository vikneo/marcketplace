from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Banner


@receiver(post_save, sender=Banner)
def cache_delete_banner(sender, instance, **kwargs):
    """ Удаление кеша баннера """
    try:
        cache.delete('banners')
    except AttributeError:
        pass
