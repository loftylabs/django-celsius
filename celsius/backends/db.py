from celsius.backends import CelsiusBackend

from celsius.models import Event


class DatabaseBackend(CelsiusBackend):
    """
    TODO:  This classes' methods should be returning some abstracted object
    that is consistent across backends, rather than QuerySets and Model instances
    """
    
    def create_event(self, key, request=None):
        if request is not None and request.user.is_authenticated:
            user = request.user
        else:
            user = None

        return Event.objects.create(
            event=key,
            user=user
        )

    def create_event_for_object(self, obj, key, request=None):
        if request is not None and request.user.is_authenticated:
            user = request.user
        else:
            user = None

        return Event.objects.create(
            event=key,
            user=user,
            content_object=obj,
        )
