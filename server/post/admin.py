# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

import jinja2
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from core.admin import (BaseAttrAdmin, CreateChangeMixinAdmin,
                        PermissionsMixinAdmin, save_changed_date,
                        save_user_perm)
from multimedia.admin import PostImageInline
from multimedia.utils import thumb

from .filters import IsPublishedFieldListFilter, TagsArrayFieldListFilter
from .models import Post


class PostAdminForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 1,
               'cols': 120}))
    slug = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 1,
               'cols': 120}))
    redirect = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 1,
                                                     'cols': 120}))

    template = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 1,
                                                     'cols': 120}))

    html = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='default'), required=False)

    markdown = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 40,
                                                     'cols': 120}))
    content = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 40,
                                                     'cols': 120}))
    description = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 4,
                                                     'cols': 120}))
    meta_description = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 5,
                                                     'cols': 50}))

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'tags': forms.Textarea(attrs={'rows': 10,
                                          'cols': 100}),
        }


class PostAdmin(BaseAttrAdmin, PermissionsMixinAdmin, CreateChangeMixinAdmin,
                admin.ModelAdmin):

    form = PostAdminForm
    image_field = "post_size"

    fieldsets = [
        (None, {
            'fields': ('title', 'slug', 'redirect', 'language', 'template',
                       'description', 'start_at', 'finished_at', 'related', )
        }),
        ('Content Markdown', {
            'classes': ('collapse', ),
            'fields': ("markdown", )
        }),
        ('Content HTML', {
            'classes': ('collapse', ),
            'fields': ("html", )
        }),
        ('Content TEXT', {
            'classes': ('collapse', ),
            'fields': ("content", )
        }),
        ('User auth', {
            'classes': ('collapse', ),
            'fields': ('login_required', 'password_required')
        }),
        ('Tags', {
            'classes': ('collapse', ),
            'fields': ('tags', )
        }),
        ('Seo options', {
            'classes': ('collapse', ),
            'fields': ('meta_description', )
        }),
        ('Attributes', {
            'classes': ('collapse', ),
            'fields': ('attributes', )
        }),
        ('Statistics', {
            'classes': ('collapse', ),
            'fields': ('rating', 'reviews')
        }),
    ]

    list_display = ("thumb", "id", "slug", 'title', 'start_at', 'finished_at',
                    "author_info", "post_type", 'language', 'is_published', )
    list_display_links = ("thumb", "id", "slug")

    list_filter = ('language', IsPublishedFieldListFilter,
                   TagsArrayFieldListFilter)

    search_fields = [
        'user__email', 'slug', 'title', 'start_at', 'finished_at',
        'description', "content"
    ]

    prepopulated_fields = {"slug": ("title", )}
    raw_id_fields = ("related", )

    inlines = [
        PostImageInline,
    ]

    def get_readonly_fields(self, request, obj=None):
        fieldsets = super().get_readonly_fields(request, obj)
        return fieldsets + ("rating", "reviews")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if form.is_valid():
            ctx = ""
            if "html" in form.changed_data:
                ctx = form.cleaned_data["html"]
            elif "markdown" in form.changed_data:
                ctx = form.cleaned_data["markdown"]
            elif "content" in form.changed_data:
                ctx = form.cleaned_data["content"]

            text = jinja2.filters.do_striptags(ctx)
            if ctx:
                obj.content = text
                obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            save_user_perm(instance, request.user)
            save_changed_date(instance)
        formset.save_m2m()

    def thumb(self, s):
        html = []
        for im in s.images.all():
            html.append(thumb(im, self.image_field))
            break
        return mark_safe(''.join(html))

    thumb.short_description = "Thumbnail"

    def is_published(self, p):
        return p.is_published

    is_published.short_description = "is_published"
    is_published.allow_tags = True

    def post_type(self, p):
        return p.post_type

    post_type.short_description = "post_type"
    post_type.allow_tags = True


admin.site.register(Post, PostAdmin)
