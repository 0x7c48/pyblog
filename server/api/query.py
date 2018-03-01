# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import Q
from django.utils import timezone


def fetch_all(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def fetch_one(cursor):
    "Return one row from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, cursor.fetchone()))


class PageManager(models.Manager):
    def get_queryset(self):
        return super(PageManager, self).get_queryset()

    def published(self):
        now = timezone.now().replace(second=0, microsecond=0)
        return (self.get_queryset()
                .filter(is_published=True)
                .exclude(publication_end_date__lte=now)
                .select_related(
                    'user',
                    'image')
                .prefetch_related(
                    'images',
                    'images__src',
                    'images__user',
        )
            .order_by('-publication_date'))

    def admin_q(self, q):
        qs = self.get_queryset()
        if q:
            qs = qs.filter(
                Q(title__istartswith=q) |
                Q(slug__istartswith=q))
        return qs

    def get_slug_lang(self, slug, language):
        return self.get_queryset().get(slug=slug, language=language)


class MenuPageManager(PageManager):
    def get_queryset(self):
        return (super(MenuPageManager, self)
                .get_queryset()
                .filter(type=self.model.MENU_PAGE)
                .order_by("-publication_date"))


class BlogPageManager(PageManager):
    def get_queryset(self):
        return (super(BlogPageManager, self)
                .get_queryset()
                .filter(type=self.model.BLOG_PAGE)
                .order_by("-publication_date"))
