from django.urls import path
from . import views as teams_views

app_name = "teams"

urlpatterns = [
    # base url: '/teams'
    path('swap/', teams_views.SwapTeamMemberRoles.as_view()),
    path('member/', teams_views.TeamMemberList.as_view()),
    path('', teams_views.TeamList.as_view()),
] + [
    # Routes including uuids in the urls
    # **Must be loaded last to avoid routing issues**
    path('member/<str:pk>', teams_views.TeamMemberDetail.as_view()),
    path('<str:pk>', teams_views.TeamDetail.as_view()),
]
