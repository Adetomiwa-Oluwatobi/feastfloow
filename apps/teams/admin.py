from django.contrib import admin
from apps.teams.models import Team, JobRole, Invitation

# Customizing the admin display for the Team model
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'created_at')
    search_fields = ('name', 'creator__username')
    list_filter = ('created_at',)

    # Organize fields for creating/editing teams
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'creator', 'members'),
        }),
    )

    # Allows for inline management of team members within the admin interface
    filter_horizontal = ('members',)

# Customizing the admin display for the JobRole model
@admin.register(JobRole)
class JobRoleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description'),
        }),
    )

# Customizing the admin display for the Invitation model
@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('team', 'invitee', 'invited_at', 'accepted')
    search_fields = ('team__name', 'invitee__username')
    list_filter = ('accepted', 'invited_at')

    fieldsets = (
        (None, {
            'fields': ('team', 'invitee', 'invited_at', 'accepted'),
        }),
    )

# Registering additional models if necessary
# admin.site.register(OtherModel)
