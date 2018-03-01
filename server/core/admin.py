# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.utils import timezone

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .utils import concat_attrs


def save_changed_date(obj):
    now = timezone.now()
    if not obj.created_at:
        obj.created_at = now
    obj.changed_at = now
    obj.save()


def save_user_perm(obj, user):
    if not obj.created_by:
        obj.created_by = user.id
    if not obj.user_id:
        obj.user = user
    obj.changed_by = user.id
    obj.save()


class ActionMixin:
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False


class QuerySetUserMixin:
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


class BasePermissionsMixinAdmin:
    readonly_fields = ('user', )

    extra_readonly_fields = [
        "create_change_readonly_fields", "permittions_readonly_fields"
    ]

    extra_fieldsets = ["create_change_fieldsets", "permittions_fieldsets"]

    @property
    def get_all_readonly_fields(self):
        return concat_attrs(self, self.extra_readonly_fields)

    @property
    def get_all_fieldsets(self):
        return concat_attrs(self, self.extra_fieldsets)

    def get_readonly_fields(self, request, obj=None):
        fieldsets = super().get_readonly_fields(request, obj)
        return fieldsets + self.get_all_readonly_fields

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        all_fieldsets = self.get_all_fieldsets

        keep_fields = []
        for fs in fieldsets:
            for field in fs[1]['fields']:
                if field not in all_fieldsets[0][1]['fields']:
                    keep_fields.append(field)
            fs[1]['fields'] = keep_fields
            keep_fields = []
        return fieldsets + list(all_fieldsets)

    def save_model(self, request, obj, form, change):
        save_user_perm(obj, request.user)
        save_changed_date(obj)
        super().save_model(request, obj, form, change)


class PermissionsMixinAdmin(BasePermissionsMixinAdmin, ActionMixin,
                            QuerySetUserMixin):

    permittions_readonly_fields = ('created_by', 'changed_by')
    permittions_fieldsets = [
        ('Permittions options', {
            'classes': ('collapse', ),
            'fields': ('created_by', 'changed_by', 'user')
        }),
    ]


class CreateChangeMixinAdmin(BasePermissionsMixinAdmin):

    create_change_readonly_fields = ('created_at', 'changed_at')
    create_change_fieldsets = [
        ('Date options', {
            'classes': ('collapse', ),
            'fields': ('created_at', 'changed_at')
        }),
    ]


class BaseAttrAdmin:
    extra = 0
    view_on_site = True
    show_change_link = True
    date_hierarchy = "start_at"
    exclude = ("index", )


class BlogFlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget': CKEditorUploadingWidget(config_name='default')
        },
    }


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, BlogFlatPageAdmin)
