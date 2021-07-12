from django.urls import path
from . import views as event_views

app_name = "event"

urlpatterns = [
    # base url: '/event'
    path('', event_views.EventList.as_view()),
] + [
    # Routes including uuids in the urls
    # **Must be loaded last to avoid routing issues**
    path('<str:event_id>/call', event_views.PerformCall.as_view()),
    path('<str:pk>', event_views.EventDetail.as_view()),
]
