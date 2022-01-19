from rest_framework import serializers

from .models import Request, Event


class RequestSerializer(serializers.ModelSerializer):
    participant = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = ['id', 'participant', 'title',
                  'event', 'attachment', 'created_at']

    def get_participant(self, obj):
        if obj.participant:
            return obj.participant.username

    def get_event(self, obj):
        if obj.event:
            return obj.event.name


class EventSerializer(serializers.ModelSerializer):
    assigner = serializers.SerializerMethodField()
    requests = RequestSerializer(many=True, required=False)

    class Meta:
        model = Event
        fields = ['id', 'assigner', 'event_type', 'name',
                  'created_at', 'event_date', 'requests']

    def get_assigner(self, obj):
        if obj.assigner:
            return obj.assigner.username
