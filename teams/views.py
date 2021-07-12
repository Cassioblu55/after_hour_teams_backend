from rest_framework import generics
from . import models as teams_models
from rest_framework.response import Response
from . import serializers as teams_serializers
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ValidationError

# Create your views here.


class TeamList(generics.ListCreateAPIView):
    serializer_class = teams_serializers.TeamSerializer
    queryset = teams_models.Team.objects.all()


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = teams_serializers.TeamSerializer
    queryset = teams_models.Team.objects.all()

    def get(self, request, *args, **kwargs):
        team = get_object_or_404(
            teams_models.Team, id=request.resolver_match.kwargs.get('pk'))

        team_info = self.serializer_class(team).data

        team_info['members'] = []
        for member in teams_models.TeamMember.objects.filter(team=team):
            member_info = teams_serializers.TeamMemberSerializer(member).data
            
            del member_info['team']
            
            team_info['members'].append(member_info)

        return Response(data=team_info)


class TeamMemberList(generics.ListCreateAPIView):
    serializer_class = teams_serializers.TeamMemberSerializer
    queryset = teams_models.TeamMember.objects.all()


class TeamMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = teams_serializers.TeamMemberSerializer
    queryset = teams_models.TeamMember.objects.all()


class SwapTeamMemberRoles(generics.CreateAPIView):
    serializer_class = teams_serializers.SwapTeamMemberRolesSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data)

        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        team_member_one = get_object_or_404(
            teams_models.TeamMember, id=validated_data['team_member_one'])

        team_member_two = get_object_or_404(
            teams_models.TeamMember, id=validated_data['team_member_two'])

        if team_member_one.team != team_member_two.team:
            raise ValidationError({"details" : "Team members must be on the same team"})

        role_one = team_member_one.role

        team_member_one.role = team_member_two.role
        team_member_one.save()

        team_member_two.role = role_one
        team_member_two.save()

        return Response(
            data = {
                "team_member_one": teams_serializers.TeamMemberSerializer(team_member_one).data,
                "team_member_two": teams_serializers.TeamMemberSerializer(team_member_two).data,
            }
        )
