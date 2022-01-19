import datetime

from django.db import models
from account.models import User

# Create your models here.
class EventType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Event type")

    verbose_name = "Event type"
    verbose_name_plural = "Event types"

    def __str__(self):
        return f"{self.name}"


class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name="Event name")
    assigner = models.ForeignKey(
        User, verbose_name="Assigner", blank=True, null=True, on_delete=models.SET_NULL
    )
    event_type = models.ForeignKey(
        EventType, verbose_name="Event type", null=True, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField(
        verbose_name="Event date", default=datetime.datetime.now
    )

    verbose_name = "Event"
    verbose_name_plural = "Events"

    def __str__(self):
        return f"{self.name}"

    @property
    def requests(self):
        return self.request_set.all()


class Request(models.Model):
    participant = models.ForeignKey(
        User,
        verbose_name="Participant",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    title = models.CharField(max_length=255, verbose_name="Request title")
    event = models.ForeignKey(
        Event, verbose_name="Event name", null=True, on_delete=models.SET_NULL
    )
    attachment = models.FileField(
        verbose_name="Attachment", upload_to="media", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    verbose_name = "Request"
    verbose_name_plural = "Requests"

    def __str__(self):
        return f"{self.title} {self.participant}"
