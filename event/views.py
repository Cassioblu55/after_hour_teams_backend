from django.shortcuts import render
from rest_framework import generics, status
from . import models as event_models
from rest_framework.response import Response
from . import serializers as event_serializers
from django.shortcuts import get_object_or_404
from call import serializers as call_serializers

# Create your views here.


class EventList(generics.ListCreateAPIView):
    serializer_class = event_serializers.EventSerializer
    queryset = event_models.Event.objects.all()


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = event_serializers.EventSerializer
    queryset = event_models.Event.objects.all()



class PerformCall(generics.CreateAPIView):
    serializer_class = call_serializers.CallSerializer

    def post(self, request, *args, **kwargs):
        event = get_object_or_404(
            event_models.Event, id=request.resolver_match.kwargs.get('event_id'))

        call_created = event.call_team_member()

        if call_created != None:
            return Response(data=self.serializer_class(call_created).data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={
                "details" : "All team members have been contacted for this event"
            })
