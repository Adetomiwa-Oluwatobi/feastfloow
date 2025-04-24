from django.contrib import admin
from apps.users.models import UserProfile

# Customizing the admin display for the UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_role', 'verified')
    search_fields = ('user__username', 'job_role')
    list_filter = ('verified',)

    # Optional: Customize fields when editing or adding a profile
    fieldsets = (
        (None, {
            'fields': ('user', 'picture', 'bio', 'job_role', 'verified'),
        }),
    )

    # Optional: Automatically populate some fields or readonly fields
    readonly_fields = ('user',)

# Register any other models if necessary
# admin.site.register(YourOtherModel)
