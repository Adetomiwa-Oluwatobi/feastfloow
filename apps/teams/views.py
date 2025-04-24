# apps/teams/views.py

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import*
# Team Invitations View
class TeamInvitationView(LoginRequiredMixin, TemplateView):
    template_name = 'teams/team_invitation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['invitations'] = self.request.user.team_invitations.all()  # Assuming a team invitations model
        return context

# Team Dashboard View
class TeamDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'teams/team_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = self.request.user.teams.all()  # User's teams
        return context


@method_decorator(login_required, name='dispatch')
class CreateTeamView(TemplateView):
    template_name = 'teams/create_team.html'

    def get(self, request):
        # Render the team creation form
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')

        # Create the new team
        team = Team.objects.create(name=name, description=description)
        # Add the user as a member of the team (if needed)
        team.members.add(request.user)

        return redirect('teams:team_dashboard')  # Redirect to the team dashboard