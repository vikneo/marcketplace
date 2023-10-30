from random import choices

from django.core.cache import caches
from django import template

from ..models import Banner

register = template.Library()


@register.inclusion_tag('banner/banner_tpl_main.html')
def banner_main_page() -> dict:
    """
    Caching of random three banners is created.
    """
    banners = caches.get_or_set('banners', choices(Banner.objects.all(), k=3))

    return {'banners': banners}
