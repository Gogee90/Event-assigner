from django.urls import path
from .views import ListCreateEvents, EventDetail, ListCreateRequest, ListRequests, RequestsDetail

urlpatterns = [
    path('events/', ListCreateEvents.as_view()),
    path('events/<int:pk>', EventDetail.as_view()),
    path('events/<int:pk>/create-request/', ListCreateRequest.as_view()),
    path('events/requests/', ListRequests.as_view()),
    path('events/requests/<int:pk>', RequestsDetail.as_view()),
]