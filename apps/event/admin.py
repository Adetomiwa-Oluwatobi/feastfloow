from django.contrib import admin
from apps.event.models import Event, Booking

# Customizing the admin display for the Event model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'organizer', 'created_at')
    search_fields = ('title', 'description', 'location', 'organizer__user__username')
    list_filter = ('date', 'location', 'organizer')
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'date', 'location', 'organizer', 'created_at'),
        }),
    )

# Customizing the admin display for the Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'number_of_guests', 'created_at')
    search_fields = ('event__title', 'user__user__username', 'number_of_guests')
    list_filter = ('event', 'created_at')
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('event', 'user', 'number_of_guests', 'created_at'),
        }),
    )
