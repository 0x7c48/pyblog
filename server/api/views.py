# -*- coding: utf-8 -*-

import json

from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import login as _login
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.cache import never_cache

from user.models import get_profile
from post.models import Post


def format_client(data, status=200, safe=True):
    """Client accept: {"results": data}"""
    return JsonResponse(data, status=status, safe=safe)


@never_cache
def login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    if not email and not password:
        data = json.loads(request.body) or {}
        email = data.get("email")
        password = data.get("password")

    errors = {}
    if not email:
        errors["email"] = "Empty email!"
    if not password:
        errors["password"] = "Empty password!"
    if errors:
        return format_client({
            "errors": errors,
            "is_authenticated": False
        }, 400)

    user = (authenticate(request=request, email=email, password=password) or
            authenticate(request=request, username=email, password=password))
    if user is not None:
        _login(request, user)
        return format_client({
            "is_authenticated": True,
            "username": user.username
        }, 200)
    else:
        errors = {
            "email": "Bad email or password!",
            "password": "Bad email or password!"
        }
        return format_client({
            "is_authenticated": False,
            "errors": errors
        }, 401)


def users_info(request):
    user = request.user
    profile = get_profile(user)
    status = 401
    is_authenticated = user.is_authenticated
    users_info = {
        "is_authenticated": is_authenticated,
        "session": request.COOKIES.get(settings.SESSION_COOKIE_NAME)
    }

    if is_authenticated:
        status = 200
        users_info["username"] = user.username
        users_info["image"] = (profile.image.url
                               if profile and profile.image else "")
    return format_client(users_info, status)


def posts(request):
    import pdb; pdb.set_trace()
    obj_posts = Post.objects.filter().select_related('user').prefetch_related('user__profile', 'post__image').all()
    posts = []
    for p in obj_posts:
        user = model_to_dict(p.user)
        user.pop('password')
        
        post = model_to_dict(p)
        image = model_to_dict(p.image)
        post['user'] = user
        post['image'] = image
        posts.append(post)
    return format_client(posts, 200, safe=False)
