# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from post.admin import PostAdmin
from post.models import Post

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0
    can_delete = False


class BlogUserAdmin(UserAdmin):
    inlines = [ProfileInline]

    def get_list_display(self, request):
        return super().get_list_display(request) + ("date_joined", )


admin.site.unregister(User)
admin.site.register(User, BlogUserAdmin)
admin.site.register(Profile)

## Multi-admin site for users ##


class BlogAdminSite(admin.AdminSite):
    """Multi admin site"""
    site_header = 'Blog administration'


blogadmin = BlogAdminSite(name='bloguseradmin')
blogadmin.register(Post, PostAdmin)
