# apps/users/urls.py

from django.urls import path
from apps.users.views import  EditProfileView, DashboardView,register,user_login,profile_view,followers_list,following_list
from django.conf.urls.static import static
from django.conf import settings


app_name = 'users'

urlpatterns = [
    path('profile/<str:username>/', profile_view, name='profile'),
    path('profile_edit/', EditProfileView.as_view(), name='edit_profile'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/<str:username>/followers/', followers_list, name='followers-list'),
    path('profile/<str:username>/following/', following_list, name='following-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)