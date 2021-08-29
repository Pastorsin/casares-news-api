import sys
from pathlib import Path

import django_heroku
import environ

env = environ.Env()

# General

BASE_DIR = Path(__file__).parent.parent

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = []

ONLY_DJANGO_APPS = env.bool("ONLY_DJANGO_APPS", default=False)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "casares-news.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "casares-news.wsgi.application"

# Applications
# https://docs.djangoproject.com/en/3.2/ref/applications/

APPS_DIR = BASE_DIR / "apps"
sys.path.append(str(APPS_DIR))

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "push_notifications",
    "rdf_io",
]

OWN_APPS = [
    "news",
    "scrap",
    "notification",
]

INSTALLED_APPS = DJANGO_APPS + (
    [] if ONLY_DJANGO_APPS else THIRD_APPS + OWN_APPS
)

# Telegram bot

TELEGRAM_TOKEN = env.str("TELEGRAM_TOKEN", default=None)
TELEGRAM_CHAT_ID = env.str("TELEGRAM_CHAT_ID", default=None)

# Webpush

PUSH_NOTIFICATIONS_SETTINGS = {
    "WP_PRIVATE_KEY": env.str("WP_PRIVATE_KEY"),
    "WP_CLAIMS": {"sub": "mailto: andressmilla@gmail.com"},
    "UNIQUE_REG_ID": True,
}

# Django REST

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
        "rest_framework.permissions.DjangoModelPermissions",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
}

# Logger
# https://docs.djangoproject.com/en/3.2/topics/logging/

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = "/static/"

# CORS header

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://pastorsin.github.io",
]

# Heroku settings
# https://pypi.org/project/django-heroku/

django_heroku.settings(locals())
