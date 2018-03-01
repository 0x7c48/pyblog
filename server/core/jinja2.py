# -*- coding: utf-8 -*-

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.utils import timezone

import jinja2


def environment(**options):
    env = jinja2.Environment(
        extensions=['jinja2.ext.i18n', 'jinja2.ext.with_'], **options)

    env.globals.update({
        'now': timezone.now().year,
        'static': staticfiles_storage.url,
        'url': reverse
    })
    return env
