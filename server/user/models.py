# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from image_cropping import ImageRatioField


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=255)
    data = JSONField(blank=True, null=True)
    image = models.ImageField(upload_to=u'images/')
    image_size = ImageRatioField(
        'image',
        settings.IMAGE_SIZE["post_base"],
        allow_fullsize=True,
        free_crop=True)

    class Meta:
        db_table = "user_profile"


def get_profile(user):
    try:
        return user.profile
    except (AttributeError, Profile.DoesNotExist):
        return
