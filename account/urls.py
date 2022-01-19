from django.urls import path
from .views import ListCreateUser, UserDetail

urlpatterns = [
    path('accounts/', ListCreateUser.as_view()),
    path('accounts/user-account/', UserDetail.as_view()),
]
