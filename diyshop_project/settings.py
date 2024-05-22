"""
Django settings for diyshop_project project.

Generated by 'django-admin startproject' using Django 3.2.25.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/

=============================================================================
SECURITY WARNING: 
The secret data, that can compromise the production system, should be defined 
locally in BASE_DIR+"/env.py" file for development.
env.py file has the following form:
        from os import environ
        environ["variable_name_1"] = "value_1"
        environ["variable_name_2"] = "value_2"
        :   :

The following lines are the names of the enviromental variables that this website requires.
    "DEVELOPMENT"   --> "True" or "False"
    "SECRET_KEY"    --> example: "9087zxcv98z798bv^=098zxcv098xzcv09*u2dsd2u+&hddf0^^uj"
    "ALLOWED_HOSTS" --> example: "127.0.0.1,localhost, diyshop-1c0dad79f0a0.herokuapp.com"
    "DATABASE_URL"  --> example: "postgres://cmftklgz:gYdAbasasdasdasdsadsad234@dumbo.db.elephantsql.com/cmftklgz"
    "ACCOUNT_EMAIL_VERIFICATION" --> "none" or "mandatory"
    "EMAIL_FROM_DEFAULT" --> example: sales-dep@diyshop.com
    "EMAIL_HOST"    --> example: 'smtp.gmail.com'
    "EMAIL_HOST_USER"   --> example: 'diyshop@gmail.com'
    "EMAIL_HOST_PASSWORD"   --> example: 'asldknlmalsm'     # gmail servers usually do not accept user passwords but application passwords
    "STRIPE_PUBLIC_KEY" --> example "pk_test_51PasdfASDFasdfasDFasdFASDFasdfag$%234weADSfGzdgLg9vUarbSvl1IBriGElYtCE0PIjVDJCkVwCM7v4hascasdcSD43"
    "STRIPE_SECRET_KEY" --> example "sk_test_51PGzdg23re0987asdlkj34ot5245098uwrve09jvlñkwevkjwgSERVWERVwer vwerfQErvñmekfvoieLg9vUarbSvaBPVn0TH8"
    "STRIPE_WH_SECRET"  --> example "whsec_9ff13b16lñknsadvTWsdafvadv299106f445ef6f269b02236aa87180952ecf8387046f2322cee5d28f"
        #to run application in local enironment use stripe cli tool command "$ ./stripe listen --forward-to 127.0.0.1:8000/checkout/wh"

IMPORTANT NOTES: 
    - NEVER allow the env.py file to be pushed to a public development or deployment repositories (Github, GitLab, Bitbucket, etc.)
    - Do not need to difine "DEVELOPMENT" variable in the production system. By default it will be set to "False" 
    - In the production environment, this variables must be defined as environmental varibles at the django server 
        (Heroku, AWS Activate, Google Cloud, etc.)
"""
from pathlib import Path
from os import getenv, path
from django.contrib import messages
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES_DIR = path.join(BASE_DIR, 'templates')

if path.isfile("env.py"):
    import env
    DEPLOYED = False
else:
    DEPLOYED = True


DEBUG = getenv('DEVELOPMENT', False)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = getenv('ALLOWED_HOSTS').split(",")


# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'home',
    'products',
    'django_summernote',
    'bag',
    'checkout',
    'profiles',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'diyshop_project.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_DIR,
            path.join(TEMPLATES_DIR, 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bag.contexts.bag_contents',
                'django.template.context_processors.media',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]            
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

# allauth custom configuration settings
ACCOUNT_EMAIL_REQUIRED = True                       # Mandatory email registration
ACCOUNT_USERNAME_REQUIRED = True                    # Mandatory username registration
ACCOUNT_PRESERVER_USERNAME_CASING = False           # Don't care for username letter case
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'    # Both username and email for identification
ACCOUNT_EMAIL_VERIFICATION = getenv('ACCOUNT_EMAIL_VERIFICATION', 'mandatory')  # Force email verification if not defined otherwise in environment
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True

SITE_ID = 1

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGUT_REDIRECT_URL = '/'     

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


# email configuration settings
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'    # Temporaly for testing
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = getenv('EMAIL_HOST','')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = getenv('EMAIL_HOST_USER','')
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD','')
DEFAULT_FROM_EMAIL = getenv('DEFAULT_FROM_EMAIL','noreplay@')


WSGI_APPLICATION = 'diyshop_project.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(getenv("DATABASE_URL",''))
}

#DATABASES = {
#   'default': {
#       'ENGINE': 'django.db.backends.sqlite3',
#       'NAME': BASE_DIR / 'db.sqlite3',
#   }
#}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [path.join(BASE_DIR, 'static'), ]

MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DIY Shop fees for delivery
FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10


# Stripe
STRIPE_CURRENCY = 'eur' # US Dolar='usd', CCE Euro = 'eur'
STRIPE_PUBLIC_KEY = getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = getenv('STRIPE_WH_SECRET', '')

if DEBUG:
    import django
    print(f"Django Version: {django.get_version()} DEBUG MODE")
