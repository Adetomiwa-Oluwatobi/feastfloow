# apps/teams/urls.py

from django.urls import path
from apps.teams.views import TeamInvitationView, TeamDashboardView,CreateTeamView

app_name = 'teams'

urlpatterns = [
    path('invitations/', TeamInvitationView.as_view(), name='team_invitations'),
    path('dashboard/', TeamDashboardView.as_view(), name='team_dashboard'),
    path('create/', CreateTeamView.as_view(), name='create_team'), 
]
