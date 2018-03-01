# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from django.db import models

from image_cropping import ImageCroppingMixin

from core.admin import (BaseAttrAdmin, CreateChangeMixinAdmin,
                        PermissionsMixinAdmin)

from .models import PostImage
from .utils import thumb


class ThumbMixinAdmin(ImageCroppingMixin):
    image_field = "thumb_size"

    def thumb(self, image):
        return thumb(image, self.image_field)

    thumb.short_description = 'Thumb'


class FormfieldOverridesMixin:
    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={'rows': 1,
                                            'cols': 50})
        },
    }


class PostImageInline(BaseAttrAdmin, PermissionsMixinAdmin,
                      CreateChangeMixinAdmin, ThumbMixinAdmin,
                      FormfieldOverridesMixin, admin.StackedInline):

    model = PostImage
    classes = ['collapse']
    exclude = ("index", )
    fields = ("src", "post_size", "title", "target", "description",
              "attributes")


class PostImageAdmin(BaseAttrAdmin, PermissionsMixinAdmin,
                     CreateChangeMixinAdmin, FormfieldOverridesMixin,
                     ThumbMixinAdmin, admin.ModelAdmin):

    image_field = "post_size"
    list_display = ('thumb', 'id', 'title')
    list_display_links = ("thumb", "id", "title")
    # raw_id_fields = ("", )
    date_hierarchy = "created_at"
    search_fields = ["title", "id", "description"]


admin.site.register(PostImage, PostImageAdmin)
