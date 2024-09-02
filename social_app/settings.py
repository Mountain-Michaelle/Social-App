"""
Django settings for social_app project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', 'mysite.com', 'localhost', '127.0.0.1']


# Application definition
INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'bookmark.apps.BookmarkConfig',
    'images.apps.ImagesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_browser_reload',
    'sass_processor',
    'compressor',
    'social_django',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'social_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'social_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#if DEBUG:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'social_app',
#         'USER': 'postgres',
#         'PASSWORD': '41240075',
#     }
# }
#else:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT')
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
]

SOCIAL_AUTH_FACEBOOK_KEY = '2941809582661342'
SOCIAL_AUTH_FACEBOOK_SECRET = 'cea7bbfdd2045ae13e1baabbb9068907'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOME_VARIABLE = ''

# SOCIAL_AUTH_Google_KEY = '600718779246-6r5kh35kmb5sk2018djusbpt1o8b8j40.apps.googleusercontent.com'
# SOCIAL_AUTH_TWITTER_SECRET = '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'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '600718779246-6r5kh35kmb5sk2018djusbpt1o8b8j40.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_TWITTER_KEY = 'VpNIoUvAfS4tffXMteqzp21eY'
SOCIAL_AUTH_TWITTER_SECRET = 'LBzMxCmt7vz3aZQDNLbtQyYr7UG5qZGlQTA5c8ud1Tcg49EmCF'


SOCIAL_AUTH_PIPELINE = [
'social_core.pipeline.social_auth.social_details',
'social_core.pipeline.social_auth.social_uid',
'social_core.pipeline.social_auth.auth_allowed',
'social_core.pipeline.social_auth.social_user',
'social_core.pipeline.user.get_username',
'social_core.pipeline.user.create_user',
'account.authentication.create_profile',
'social_core.pipeline.social_auth.associate_user',
'social_core.pipeline.social_auth.load_extra_data',
'social_core.pipeline.user.user_details',
]
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR/'static/']
STATIC_ROOT = BASE_DIR /'staticfiles/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
     # other finders..
    'compressor.finders.CompressorFinder',
    'sass_processor.finders.CssFinder',
]


SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(BASE_DIR, 'static/Assets/scss'),
    # os.path.join(PROJECT_PATH, 'node_modules'),
]


SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'

SASS_OUTPUT_STYLE = 'compact'
SASS_PRECISION = 8

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

INTERNAL_IPS = [
    "127.0.0.1",
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
