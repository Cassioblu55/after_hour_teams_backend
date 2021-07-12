# Generated by Django 3.2.5 on 2021-07-11 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        ('event', '0001_initial'),
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event'),
        ),
        migrations.AddField(
            model_name='call',
            name='team_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.teammember'),
        ),
    ]
