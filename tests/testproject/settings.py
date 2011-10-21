from os.path import dirname, join

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = join(dirname(__file__), 'db', 'friendlytagloader.db')

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
    join(dirname(__file__), 'templates')
)

ROOT_URLCONF = 'testproject.urls'
