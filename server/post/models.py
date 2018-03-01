# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from core.models import CreateChangeMixin, PermissionsMixin


class Post(PermissionsMixin, CreateChangeMixin):
    TEXT = "TEXT"
    MARKDOWN = "MARKDOWN"
    HTML = "HTML"

    login_required = models.NullBooleanField(
        default=False, help_text=_("Только для зарег. пользователей"))
    password_required = models.NullBooleanField(
        default=False, help_text=_("Только с паролем"))

    start_at = models.DateTimeField(
        default=timezone.now, help_text=_("Опубликовать с даты"))
    finished_at = models.DateTimeField(
        blank=True, null=True, help_text=_("Скрыть с даты"))
    language = models.CharField(
        max_length=255, choices=settings.LANGUAGE_CHOICES, default=settings.RU)

    title = models.CharField(max_length=255, help_text=_("Заголовок"))
    slug = models.TextField(help_text=_("Ссылка"))
    redirect = models.TextField(
        blank=True, null=True, help_text=_("Перенаправить на страницу"))

    template = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(help_text=_("Описание"))

    markdown = models.TextField(
        _("Пост"), blank=True, null=True, help_text=_("Пост"))
    html = models.TextField(
        _("Пост"), blank=True, null=True, help_text=_("Пост"))
    content = models.TextField(blank=True, null=True, help_text=_("Контент"))

    tags = ArrayField(
        models.CharField(max_length=255, blank=True),
        default=list,
        blank=True,
        null=True,
        help_text=_("Через запятую"))

    rating = models.IntegerField(blank=True, null=True, default=0)
    reviews = models.BigIntegerField(blank=True, null=True, default=0)

    related = models.ManyToManyField('self', models.DO_NOTHING, blank=True)
    attributes = JSONField(blank=True, null=True, help_text=_("Атрибуты"))

    class Meta:
        db_table = 'post'
        unique_together = (("slug", "language"))
        verbose_name = "Post"

    def __str__(self):
        return "{}, id={}".format(self.title, self.id)

    def author_info(self):
        return "id{}:{}".format(self.user.id, self.user.email or
                                self.user.get_username())

    @property
    def is_published(self):
        return self.created_at >= timezone.now()

    @property
    def post_type(self):
        if self.html:
            return self.HTML
        elif self.markdown:
            return self.MARKDOWN
        return self.TEXT
