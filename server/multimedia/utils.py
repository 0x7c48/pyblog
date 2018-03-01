# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from image_cropping.utils import get_backend


def thumb(image, size_field, site=False):
    """Admin thumb"""
    image_url = get_backend().get_thumbnail_url(image.src, {
        'size': (100, 100),
        'box':
        getattr(image, size_field),
        'crop':
        True,
        'detail':
        True
    })
    if site:
        return "%%s" % (settings.SITE_DOMAIN, image_url)
    return mark_safe(format_html('<img src="{0}" />', image_url))
