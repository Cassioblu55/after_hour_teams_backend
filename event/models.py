from django.db import models
from teams import models as teams_models
from annoying.functions import get_object_or_None
from call import models as call_models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField()

    team = models.ForeignKey(teams_models.Team, on_delete=models.CASCADE)

    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def call_team_member(self):
        team_members_by_call_order = self.team.get_team_members_in_call_order()

        for call_order in sorted(team_members_by_call_order.keys()):
            for team_member_id in team_members_by_call_order[call_order]:
                team_member = teams_models.TeamMember.objects.get(
                    id=team_member_id)
                
                call_sent = get_object_or_None(
                    call_models.Call, event=self, team_member=team_member)
                
                if call_sent == None:
                    call = call_models.Call(
                        event=self, team_member=team_member)
                    call.save()

                    return call
        return None
