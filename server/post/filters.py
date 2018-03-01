# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils import timezone

from .models import Post


class IsPublishedFieldListFilter(admin.SimpleListFilter):
    title = "is_published"
    parameter_name = "is_published"

    def lookups(self, request, model_admin):
        return (
            ("published", "published"),
            ("draft", "draft"),
        )

    def queryset(self, request, queryset):
        if self.value() == "published":
            return queryset.filter(start_at__gte=timezone.now())
        elif self.value() == "draft":
            return queryset.filter(start_at__lt=timezone.now())


class TagsArrayFieldListFilter(admin.SimpleListFilter):
    """This is a list filter based on the values
    from a model's `keywords` ArrayField. """

    title = 'tags'
    parameter_name = 'tags'

    def lookups(self, request, model_admin):
        keywords = Post.objects.values_list("tags", flat=True)
        keywords = [(kw, kw) for sublist in keywords for kw in sublist if kw]
        keywords = sorted(set(keywords))
        return keywords

    def queryset(self, request, queryset):
        lookup_value = self.value()
        if lookup_value:
            queryset = queryset.filter(tags__contains=[lookup_value])
        return queryset
