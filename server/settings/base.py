# Base settings

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '8&1d3wytmciarcxf7**@d=-opr7bqn-m!1iv)eff)0yuhi@0%n'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0:8080']

# Application definition

INSTALLED_APPS_BEFORE = []

INSTALLED_APPS_BASE = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
]

INSTALLED_APPS_DISTR = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "easy_thumbnails",
    "image_cropping",
    "ckeditor",
    "ckeditor_uploader",
]

INSTALLED_APPS_PROJECT = [
    'core.apps.CoreConfig',
    'user.apps.UserConfig',
    'post.apps.PageConfig',
    'multimedia.apps.MultiMediaConfig'
]

INSTALLED_APPS = (
    INSTALLED_APPS_BEFORE
    + INSTALLED_APPS_BASE
    + INSTALLED_APPS_DISTR
    + INSTALLED_APPS_PROJECT
)

MIDDLEWARE = [
    # must be first in the list
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # must be last
    # 'django.middleware.cache.FetchFromCacheMiddleware'
]

SESSION_COOKIE_HTTPONLY = False

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND':
        'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            os.path.join(BASE_DIR, "templates", "jinja2"),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS':
        True,
        'OPTIONS': {
            'environment': 'core.jinja2.environment',
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates", "django"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = u'%s' % os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [os.path.join(BASE_DIR, "assets")]

MEDIA_URL = '/media/'
MEDIA_ROOT = u'%s' % os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend'
)

SITE_ID = 1

RU = u'RU'
EN = u'EN'
LANGUAGE_CHOICES = ((RU, ('RU')), (EN, ('EN')), )

MANAGERS = [('Manager', 'manager@gmail.com')]

# APP settings

# http://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

AUTHENTICATED_LOGIN_REDIRECTS = False

ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

SIGNUP_EMAIL_ENTER_TWICE = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

ACCOUNT_SIGNUP_FORM_CLASS = "core.forms.SignupForm"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# API settings

FILER_ENABLE_PERMISSIONS = True

# https://github.com/django-ckeditor/django-ckeditor
CKEDITOR_IMAGE_BACK = 'pillow'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = 'uploads'

CKEDITOR_CONFIGS = {
    'default': {
        'skin':
        'moono-lisa',
        'toolbar_Basic': [['Source', '-', 'Bold', 'Italic']],
        'toolbar_YouCustomToolbarConfig': [
            {
                'name':
                'document',
                'items': [
                    'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-',
                    'Templates'
                ]
            },
            {
                'name':
                'clipboard',
                'items': [
                    'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-',
                    'Undo', 'Redo'
                ]
            },
            {
                'name': 'editing',
                'items': ['Find', 'Replace', '-', 'SelectAll']
            },
            {
                'name':
                'forms',
                'items': [
                    'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea',
                    'Select', 'Button', 'ImageButton', 'HiddenField'
                ]
            },
            '/',
            {
                'name':
                'basicstyles',
                'items': [
                    'Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                    'Superscript', '-', 'RemoveFormat'
                ]
            },
            {
                'name':
                'paragraph',
                'items': [
                    'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent',
                    '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft',
                    'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-',
                    'BidiLtr', 'BidiRtl', 'Language'
                ]
            },
            {
                'name': 'links',
                'items': ['Link', 'Unlink', 'Anchor']
            },
            {
                'name':
                'insert',
                'items': [
                    'Image', 'CodeSnippet', 'Flash', 'Table', 'HorizontalRule',
                    'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'
                ]
            },
            '/',
            {
                'name': 'styles',
                'items': ['Styles', 'Format', 'Font', 'FontSize']
            },
            {
                'name': 'colors',
                'items': ['TextColor', 'BGColor']
            },
            {
                'name': 'tools',
                'items': ['Maximize', 'ShowBlocks']
            },
            '/',  # put this to force next toolbar on new line
            {
                'name':
                'youcustomtools',
                'items': [
                    # put the name of your editor.ui.addButton here
                    '',
                    '',
                ]
            },
        ],
        'toolbar':
        'YouCustomToolbarConfig',  # put selected toolbar config here
        'toolbarGroups': [
            {
                'name': 'document',
                'groups': ['mode', 'document', 'doctools']
            },
            {
                'name': 'tools'
            },
            {
                'name': 'links'
            },
            {
                'name': 'basicstyles',
                'groups': ['basicstyles', 'cleanup']
            },
            {
                'name': 'paragraph',
                'groups': ['list', 'indent', 'blocks', 'align', 'bidi']
            },
            {
                'name': 'styles'
            },
            {
                'name': 'others'
            },
        ],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        'mathJaxLib':
        '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces':
        4,
        'extraPlugins':
        ','.join([
            # Extra plugins here
            'div',
            'devtools',
            'dialog',
            'dialogui',
            'elementspath',
            'a11yhelp',
            'adobeair',
            'ajax',
            'autoembed',
            'autolink',
            'clipboard',
            'codesnippet',
            'colordialog',
            'docprops',
            'embed',
            'embedbase',
            'embedsemantic',
            'filetools',
            'find',
            'flash',
            'forms',
            'iframe',
            'iframedialog',
            'image',
            'image2',
            'language',
            'lineutils',
            'link',
            'liststyle',
            'magicline',
            'mathjax',
            'menubutton',
            'notification',
            'notificationaggregator',
            'pagebreak',
            'pastefromword',
            'placeholder',
            'preview',
            'scayt',
            'sharedspace',
            'showblocks',
            'smiley',
            'sourcedialog',
            'specialchar',
            'stylesheetparser',
            'table',
            'tableresize',
            'tabletools',
            'templates',
            'uicolor',
            'uploadwidget',
            'widget',
            'wsc',
            'xml',
            'uploadimage',
        ]),
    }
}

# django-image-cropping
from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    ('image_cropping.thumbnail_processors.crop_corners',)
    + thumbnail_settings.THUMBNAIL_PROCESSORS
)

IMAGE_CROPPING_THUMB_SIZE = (300, 300)
IMAGE_CROPPING_JQUERY_URL = 'js/jquery/jquery.js'
THUMBNAIL_DEBUG = True

# Image cropping
IMAGE_SIZE = {"post_base": "450x550"}

SITE_DOMAIN = "http://localhost"
