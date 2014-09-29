from os.path import dirname, join

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.sqlite3',
        "NAME": join(dirname(__file__), 'db', 'friendlytagloader.db')
    }
}

INSTALLED_APPS = (
    'testproject',
    'friendlytagloader',
    'django.contrib.webdesign',
)

TEMPLATE_DIRS = (
    join(dirname(__file__), 'templates'),
)

ROOT_URLCONF = 'testproject.urls'

SECRET_KEY = 'AVx7Au7LXpdYTuqSUYaDGf4U'
