# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class ChoiceArrayField(ArrayField):
    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.MultipleChoiceField,
            'choices': self.base_field.choices,
        }
        defaults.update(kwargs)
        return super(ArrayField, self).formfield(**defaults)


class PermissionsMixin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by = models.BigIntegerField()
    changed_by = models.BigIntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return '{}'.format(self.id)


class CreateChangeMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    changed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class StartAtFinishedAtMixin(models.Model):
    start_at = models.DateTimeField(
        default=timezone.now,
        help_text=_("Опубликовать с даты"),
        db_index=True)

    finished_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text=_("Скрыть с даты"),
        db_index=True)

    class Meta:
        abstract = True
