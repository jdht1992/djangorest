import environ

ROOT_DIR = environ.Path(__file__) - 2

APPS_DIR = ROOT_DIR.path('apps_content')

#We will use the environ.Env() function that will find a .env file in our project root, then 
env = environ.Env()

# This section added from an update to standards in CookieCutter Django to ensure no errors are encountered at runserver/migrations
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)


if READ_DOT_ENV_FILE:    
    env.read_env(str(ROOT_DIR.path('environ.env')))
    #read_env() reading .env file


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'ii%)^_+(xkgv@pnk)s38+t&u3#inprytp^#9i&ch-=dthoy!h%'
SECRET_KEY = env('SECRET_KEY')

DEBUG = env.bool('DEBUG')



# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',# new
)

THIRD_PARTY_APPS = (
    'allauth',  # new
    'allauth.account',  # new
    'allauth.socialaccount',  # new
    'allauth.socialaccount.providers.google',  # new
    'allauth.socialaccount.providers.github',  # new
    'allauth.socialaccount.providers.facebook',  # new
    'rest_framework',
)

LOCAL_APPS = (
    'apps_content.api',
    'apps_content.biblioteca',
    'apps_content.users',
)

AUTH_USER_MODEL = 'users.CustomUser' # new

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = "none"


SOCIAL_AUTH_FACEBOOK_KEY = env('key')
SOCIAL_AUTH_FACEBOOK_SECRET = env('secret')

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangorest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'apps_content/templates'
        ],
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

WSGI_APPLICATION = 'djangorest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': env.db(),
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#Es la única configuración estática creada de forma predeterminada. Esta es la URL en la que se servirán los archivos estáticos.
STATIC_URL = '/static/'

#Donde se colocarán los archivos estáticos recogidos
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

#carpetas Django buscará archivos estáticos en
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]
#especificaciones sobre qué archivos buscar
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# URL agregada a la URL raíz para servir datos de medios
MEDIA_URL = '/media/'

#Donde se almacenarán los archivos multimedia recolectados
MEDIA_ROOT = str(APPS_DIR('media'))

REST_FRAMEWORK = {
    #'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ], 
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

