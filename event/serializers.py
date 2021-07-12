from rest_framework import serializers, status
from . import models as event_models

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event_models.Event
        fields = '__all__'


