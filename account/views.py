from django.contrib.auth import login
from rest_framework.generics import ListCreateAPIView, ListAPIView
from django_filters import rest_framework as filters

from .filters import UserFilter

from .models import User
from .serializers import UserSerializer
from utils.permissions import CustomDjangoObjectPermissions


# Create your views here.
class ListCreateUser(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter

    def perform_create(self, serializer):
        username = self.request.data["username"]
        email = self.request.data["email"]
        password = self.request.data["password"]
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.groups.set(self.request.data["groups"])
        login(self.request, user, backend="django.contrib.auth.backends.ModelBackend")


class UserDetail(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        CustomDjangoObjectPermissions,
    ]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)
