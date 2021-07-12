from rest_framework import serializers, status
from . import models as call_models



class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = call_models.Call
        fields = '__all__'
