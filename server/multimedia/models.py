# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from image_cropping import ImageRatioField

from core.models import CreateChangeMixin, PermissionsMixin


class ImageAbstract(PermissionsMixin, CreateChangeMixin):
    id = models.BigAutoField(primary_key=True)
    src = models.ImageField(upload_to=u'images/')
    title = models.CharField(_("title"), max_length=255)
    target = models.TextField(
        _("target url"), max_length=255, blank=True, null=True)
    description = models.TextField(
        _("description"), max_length=255, blank=True, null=True)
    attributes = JSONField(blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ("-index", "-id")


class PostImage(ImageAbstract):
    post_size = ImageRatioField(
        'src',
        settings.IMAGE_SIZE["post_base"],
        allow_fullsize=True,
        free_crop=True)
    post = models.ForeignKey(
        "post.Post", on_delete=models.CASCADE, related_name="images")

    class Meta:
        db_table = "post_image"
