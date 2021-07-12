from rest_framework import generics
from . import models as call_models
from . import serializers as call_serializers

# Create your views here.


class CallList(generics.ListAPIView):
    serializer_class = call_serializers.CallSerializer
    queryset = call_models.Call.objects.all()


class CallDetail(generics.RetrieveDestroyAPIView):
    serializer_class = call_serializers.CallSerializer
    queryset = call_models.Call.objects.all()
