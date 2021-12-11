from os.path import dirname, join

import dj_database_url

DEBUG = True

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://developer:developer@localhost:5432/django_test',
    ),
}

INSTALLED_APPS = (
    'testproject',
    'friendlytagloader',
    'django.contrib.sites',
    'django.contrib.flatpages',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(dirname(__file__), 'templates')],
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

ROOT_URLCONF = 'testproject.urls'

SECRET_KEY = 'AVx7Au7LXpdYTuqSUYaDGf4U'
