# django-celsius

## Install it

```
pip install -e git@github.com:loftylabs/django-celsius.git

# in settings.py

INSTALLED_APPS = [
    #...
    'celsius',
]
```

## Use the mixin(s)


```
# views.py

from celsius.views.mixins import VisitableObjectMixin
from django.views.generic import DetailView

class MyView(VisitableObjectMixin, DetailView):
    model = MyModel
    # ...

```


## Or the low-level API

```
#Get and instantiate the backend

from celsius.backends import get_backend

backend = get_backend()

backend.create_event('signup', request=request)
```
