# # -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth.views import logout

from api import views


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', logout),
    url(r'^users/$', views.users_info, name='user_info'),
    url(r'^posts/$', views.posts, name='posts')
]
