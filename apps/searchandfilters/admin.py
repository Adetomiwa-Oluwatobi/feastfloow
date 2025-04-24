from django.contrib import admin
from apps.searchandfilters.models import SearchQuery, Filter

# Customizing the admin display for the SearchQuery model
@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ('query', 'timestamp')
    search_fields = ('query',)
    list_filter = ('timestamp',)
    readonly_fields = ('timestamp',)

    fieldsets = (
        (None, {
            'fields': ('query', 'timestamp'),
        }),
    )

# Customizing the admin display for the Filter model
@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'criteria')

    fieldsets = (
        (None, {
            'fields': ('name', 'criteria'),
        }),
    )

# Registering additional models if necessary
# admin.site.register(OtherModel)
