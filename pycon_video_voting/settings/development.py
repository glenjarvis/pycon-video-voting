"""
Django settings for pycon_video_voting project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""



import os

from .common import (
    AUTH_PASSWORD_VALIDATORS, BASE_DIR,
    INSTALLED_APPS, LANGUAGE_CODE, LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL,
    MIDDLEWARE, ROOT_URLCONF, SERVER_EMAIL,
    STATIC_ROOT, STATIC_URL, TEMPLATES, TIME_ZONE,
    USE_I18N, USE_L10N, USE_TZ, WSGI_APPLICATION)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '713s_a1buvv#&ax&-tr#aclu9gol%v3n@@+z(695+o0i@p5%3j'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}

