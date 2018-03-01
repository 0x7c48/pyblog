# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

from core.views import IndexView
from user.admin import blogadmin


# Base urls
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

# App urls, order is metter
urlpatterns += [
    path('api/v1/', include("api.urls")),
    path('blogadmin/', blogadmin.urls),
]

# static & media
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Single page app handle all URL via javascript routes.
# Django trailing middleware don't work.
# That way need exclude pattern for this.
# Don't forget exclude pattern here if add new Django URL.

# Must be the last in URL, with exclude pattern
urlpatterns += [
    url(r'^(?!accounts$|admin$|blogadmin$|ckeditor$|api)',
        IndexView.as_view(), name='index'),
]
