
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

ROOT_URLCONF = 'timecode.test.urls'

INSTALLED_APPS = [
    'timecode',
    'timecode.test',
]

SECRET_KEY = 'abcd'
