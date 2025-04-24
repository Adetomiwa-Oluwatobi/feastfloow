# apps/event/urls.py

from django.urls import path
from apps.event.views import EventDetailView

app_name = 'event'

urlpatterns = [
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
]
