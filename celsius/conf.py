from django.conf import settings

CELSIUS_BACKEND = getattr(settings, 'CELSIUS_BACKEND', 
    'celsius.backends.db.DatabaseBackend')