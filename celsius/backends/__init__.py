from django.utils.module_loading import import_module


class CelsiusBackend:
    """
    Base class for Celsius stat tracking backend.
    """

    def create_event(self, request=None):
        raise NotImplementedError()
    

    def create_event_for_object(self, obj, request=None):
        raise NotImplementedError()



def _get_backend():
    """
    Returns the currently configured backend
    """
    from celsius.conf import CELSIUS_BACKEND

    parts = CELSIUS_BACKEND.split('.')
    mod = import_module(".".join(parts[:-1]))
    class_name = parts[-1]
    
    return getattr(mod, class_name)
