from teams import models as team_models
from event import models as event_models
from call import models as call_models
import pytest


@pytest.mark.django_db
def test_call_team_member_should_create_call_in_correct_order():
    team = team_models.Team(name="Mock Team")
    team.save()

    first_team_member = team_models.TeamMember(
        role="First Responder",
        name="Bob",
        team=team
        )

    first_team_member.save()

    second_team_member = team_models.TeamMember(
        role="First Responder",
        name="Rachael",
        team=team
    )
    second_team_member.save()

    third_team_member = team_models.TeamMember(
        role="Standby Responder",
        name="Doug",
        team=team
    )
    third_team_member.save()

    fourth_team_member = team_models.TeamMember(
        role="Supervisor",
        name="Peggy",
        team=team
    )
    fourth_team_member.save()

    event = event_models.Event(
        name="Water main brakeage",
        description="There is water everywhere",
        team=team
    )
    event.save()

    assert len(call_models.Call.objects.all()) is 0

    event.call_team_member()
    event.call_team_member()
    event.call_team_member()
    event.call_team_member()

    calls = call_models.Call.objects.filter(
        event=event).order_by('created_at')

    assert len(calls) is 4

    assert calls[0].team_member == first_team_member
    assert calls[1].team_member == second_team_member
    assert calls[2].team_member == third_team_member
    assert calls[3].team_member == fourth_team_member
