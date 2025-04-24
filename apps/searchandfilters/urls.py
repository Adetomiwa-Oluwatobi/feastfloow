# apps/searchandfilters/urls.py

from django.urls import path
from apps.searchandfilters.views import SearchView

app_name = 'searchandfilters'

urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
]
