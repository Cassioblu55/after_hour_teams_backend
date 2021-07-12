from django.urls import path
from . import views as call_views

app_name = "call"

urlpatterns = [
    # base url: '/call'
    path('', call_views.CallList.as_view()),
] + [
    # Routes including uuids in the urls
    # **Must be loaded last to avoid routing issues**
    path('<str:pk>', call_views.CallDetail.as_view()),
]
