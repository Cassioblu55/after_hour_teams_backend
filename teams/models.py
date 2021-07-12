from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    # Create an ordered set
    CALL_ORDER_BY_ROLE = dict.fromkeys(
        ["First Responder", "Standby Responder", "Supervisor"]).keys()
    
    def get_team_members_in_call_order(self):
        team_members_by_call_order = {}
        for index, role in enumerate(self.CALL_ORDER_BY_ROLE):
            team_members_by_call_order[index] = list(
                map(lambda t: t.id, TeamMember.objects.filter(role__iexact=role, team=self)))

        return team_members_by_call_order



class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    role = models.CharField(max_length=100)
