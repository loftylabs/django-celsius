from django.contrib import admin

from celsius.models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event', 'event_datetime', 'user', 'content_object']
    list_filter = ['event']