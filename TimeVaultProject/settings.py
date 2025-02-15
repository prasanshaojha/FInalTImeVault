"""
Django settings for TimeVaultProject project.

Generated by 'django-admin startproject' using Django 5.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""


from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(&6u8t$^z-it1@&&u84_0#q*th6i497y!g5^p$8!@lesas_^_t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django_light',
    'admin_tools_stats',
    'django_nvd3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
]



EXTERNAL_APPS =[
    'vaultapp',
    
]
INSTALLED_APPS.extend(EXTERNAL_APPS)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TimeVaultProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'TimeVaultProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',  # The database you created
        'USER': 'myuser',  # The user you created
        'PASSWORD': 'mypassword',  # The password for the user
        'HOST': 'localhost',  # Localhost because the MySQL server is on your machine
        'PORT': '3306',  # Default MySQL port
    }
}


 


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'  # This is the correct time zone for Nepal (UTC+05:45)
USE_TZ = True  # Ensure time zone support is enabled


# USE_I18N = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = "/static/"
STATICFILES_DIRS = []

MEDIA_ROOT = BASE_DIR/'media'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#email-section
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# SMTP settings
EMAIL_HOST = 'smtp.gmail.com'  # SMTP server
EMAIL_PORT = 587               # Port for TLS
EMAIL_USE_TLS = True           # Use TLS encryption
EMAIL_HOST_USER = 'yourthoughtsmatter87@gmail.com'       # Your email
EMAIL_HOST_PASSWORD = 'iamb tyxx ivvj zczs'   # Your password or App Password

# Default email for outgoing messages
DEFAULT_FROM_EMAIL = 'yourthoughtsmatter87@gmail.com'

# Admin email for error notifications
ADMINS = [('aurablog', 'yourthoughtsmatter87@gmail.com')]

# Email for system errors (like 500 Internal Server Error emails)
SERVER_EMAIL = 'yourthoughtsmatter87@gmail.com'
# # settings.py
# LOGIN_URL = '/signin/'  # Custom login URL
# # settings.py
# LOGIN_REDIRECT_URL = '/'  # This will redirect them to the home page after login
