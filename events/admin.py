from django.contrib import admin
from .models import EventType, Event, Request

# Register your models here.
admin.site.register(EventType)
admin.site.register(Event)
admin.site.register(Request)
