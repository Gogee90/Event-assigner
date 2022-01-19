from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from django_filters import rest_framework as filters

from utils.permissions import CustomDjangoObjectPermissions
from .models import Event, Request
from .serializers import EventSerializer, RequestSerializer
from .filters import EventFilter, RequestFilter
from utils.email import send_email


class ListCreateEvents(ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [
        CustomDjangoObjectPermissions,
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(assigner=user)


class EventDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [
        CustomDjangoObjectPermissions,
    ]


class ListCreateRequest(ListCreateAPIView):
    serializer_class = RequestSerializer
    permission_classes = [
        CustomDjangoObjectPermissions,
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RequestFilter

    def get_queryset(self):
        event_id = self.kwargs["pk"]
        return Request.objects.filter(event_id=event_id)

    def perform_create(self, serializer):
        event_id = self.kwargs["pk"]
        title = self.request.data["title"]
        attachment = self.request.data["attachment"]
        user = self.request.user
        event = Event.objects.get(id=event_id)
        event_request = serializer.save(
            participant=user, title=title, event_id=event_id, attachment=attachment
        )
        if event.event_type.name == "test_event":
            topic = "Заявка на участие"
            message = f"Пользователь {user.username} оставил заявку на участие в событии {event_request.event.name}."
            send_email(user.username, [event.assigner.email], topic, message)
        if event.event_type.name == "test_event2":
            topic = "Отклик"
            message = f"Пользователь {user.username} оставил отклик на событие {event_request.event.name}."
            send_email(
                user.username,
                [event.assigner.email],
                topic,
                message,
                event_request.attachment,
            )


class ListRequests(ListAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
    permission_classes = [
        CustomDjangoObjectPermissions,
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RequestFilter


class RequestsDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
    permission_classes = [
        CustomDjangoObjectPermissions,
    ]
