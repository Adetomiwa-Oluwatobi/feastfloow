# apps/ratingsandreviews/urls.py

# ratingsandreviews/urls.py
from django.urls import path
from . import views

app_name = 'ratingsandreviews'  # This sets the app's namespace

urlpatterns = [
    path('add-review/<int:user_id>/', views.add_review, name='add_review'),
]
