import os

AUTH_USER_MODEL = 'custom_user.CustomUser'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = [
    'simple_history.tests',
    'simple_history.tests.custom_user',
    'simple_history.tests.external',
    'simple_history.tests.migration_test_app',

    'simple_history',

    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
]

MEDIA_ROOT = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 'test_files')

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'simple_history.tests.urls'

SECRET_KEY = 'mock secret'

STATIC_URL = '/static/'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
}]
