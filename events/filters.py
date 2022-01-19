import django_filters
from .models import Event, Request


class EventFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateFromToRangeFilter()
    event_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Event
        fields = ['assigner', 'name', 'event_type', 'created_at', 'event_date']


class RequestFilter(django_filters.FilterSet):

    class Meta:
        model = Request
        fields = ['participant', 'title', 'event', 'created_at']
