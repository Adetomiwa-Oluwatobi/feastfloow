# apps/followers/urls.py

from django.urls import path


app_name = 'followers'


from . import views

urlpatterns = [
    path('profile/<str:username>/follow/', views.follow_user, name='follow-user'),
    path('profile/<str:username>/unfollow/', views.unfollow_user, name='unfollow-user'),
]
