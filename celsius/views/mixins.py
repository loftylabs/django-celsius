from celsius.backends import get_backend
from celsius.models import Event


backend = get_backend()


class VisitableObjectMixin:
    """
    To mixin with DetailView.
    """

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        # Create an event for this view's object
        if self.object:
            backend.create_event_for_object(self.object, 'visit', request)

        return response
