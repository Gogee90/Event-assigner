from rest_framework import serializers
from .models import User
from events.serializers import EventSerializer


class UserSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'groups', 'events']
