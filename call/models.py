from django.db import models
from event import models as event_models
from teams import models as teams_models
# Create your models here.


class Call(models.Model):
    event = models.ForeignKey(event_models.Event, on_delete=models.CASCADE)
    
    team_member = models.ForeignKey(
        teams_models.TeamMember, on_delete=models.CASCADE)

    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(args, kwargs)

        # Perform call logic here