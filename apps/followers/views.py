# apps/users/views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Connection, User

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    if user_to_follow != request.user:
        Connection.objects.get_or_create(follower=request.user, following=user_to_follow)
        messages.success(request, f"You are now following {user_to_follow.username}.")
    else:
        messages.warning(request, "You cannot follow yourself.")
    return redirect('profile', username=username)

@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    follow_relation = Connection.objects.filter(follower=request.user, following=user_to_unfollow)
    if follow_relation.exists():
        follow_relation.delete()
        messages.success(request, f"You have unfollowed {user_to_unfollow.username}.")
    else:
        messages.warning(request, "You are not following this user.")
    return redirect('profile', username=username)


