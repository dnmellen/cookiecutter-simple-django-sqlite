from .base import *

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.file'
