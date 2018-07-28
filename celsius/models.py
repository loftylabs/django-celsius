from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Event(models.Model):
    """
    Used by Celsius Datab
    """

    # User (optionally) who performed the event.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, 
        on_delete=models.SET_NULL)

    # Event timing and key
    event_datetime = models.DateTimeField(auto_now_add=True)
    event = models.CharField(max_length=32)

    # Polymorphic relationship for object based events
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
