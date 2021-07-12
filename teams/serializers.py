from rest_framework import serializers
from . import models as teams_models

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = teams_models.Team
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = teams_models.TeamMember
        fields = '__all__'


class SwapTeamMemberRolesSerializer(serializers.Serializer):
    team_member_one = serializers.IntegerField()

    team_member_two = serializers.IntegerField()
