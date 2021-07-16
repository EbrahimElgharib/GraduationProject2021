"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n@yf1htcf&qqwmw7s(zuhn(e4amv*qebao9)=1f=b1bsr5vy)i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'virtual-lab-2021.herokuapp.com',
    'https://virtual-lab-2021.herokuapp.com',
    '127.0.0.1',
    'localhost',
]

# Application definition
INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # for allauth pkg - for social
    # The following apps are required:
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin_oauth2',
    # FrontEnd
    # https://pypi.org/project/django-bootstrap4/
    "bootstrap4",
    'crispy_forms',
    # External Packages
    "taggit",  # https://github.com/jazzband/django-taggit
    'django_summernote',  # https://github.com/summernote/django-summernote
    'django_countries',  # https://github.com/SmileyChris/django-countries
    # Apps
    'labs',
    'about',
    'blog',
    'settings',
    'contact',

    'chatbotapp', # chatbot

    "verify_email.apps.VerifyEmailConfig",  # verification
]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },


    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
        ],
    }

}


CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for whitenoist pkg-heroku
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'settings.footer_context_processor.myfooter',  # data in my footer
                'settings.footer_context_processor.subscribe_footer',  # subscribe form
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
# login
LOGIN_URL = '/accounts/login'
# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGOUT_REDIRECT_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/accounts/profile'

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Path of DB File
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static" / "staticroot"  # for heroku
STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/var/www/static/',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Show summernote package
X_FRAME_OPTIONS = 'SAMEORIGIN'
SUMMERNOTE_THEME = 'bs4'  # Show summernote with Bootstrap4

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# send emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ebrahimtest44@gmail.com'
EMAIL_HOST_PASSWORD = 'suctirajajirqwdw'


# recaptch
GOOGLE_RECAPTCHA_SECRET_KEY = '6LfxBoUbAAAAAIsEz2PN5gkXj3Y0d2E2XhaMHjmO'


# for white noise pkg --> heroku
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Newsletter  ### https://app.sendgrid.com/settings/api_keys
FROM_EMAIL = 'ebrahimtest44@gmail.com'
SENDGRID_API_KEY = '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'


# pkg verification
VERIFICATION_SUCCESS_TEMPLATE = None
EXPIRE_AFTER = "1d"
