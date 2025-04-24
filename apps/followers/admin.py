from django.contrib import admin
from apps.followers.models import Connection, ConnectionRequest

# Customizing the admin display for the Connection model
@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'created_at')
    search_fields = ('follower__username', 'following__username')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('follower', 'following', 'created_at'),
        }),
    )

# Customizing the admin display for the ConnectionRequest model
@admin.register(ConnectionRequest)
class ConnectionRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'accepted', 'created_at')
    search_fields = ('sender__username', 'receiver__username', 'message')
    list_filter = ('accepted', 'created_at')
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('sender', 'receiver', 'message', 'accepted', 'created_at'),
        }),
    )
