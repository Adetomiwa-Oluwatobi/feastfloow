# apps/users/views.py
from apps.ratingsandreviews.models import Review
from apps.ratingsandreviews.forms import ReviewForm  # 
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, UserProfile
from .forms import *
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, UserLoginForm 
from django.db.models import Avg

# User Profile View
"""class UserProfileView(LoginRequiredMixin,DetailView):
    model = UserProfile
    template_name = 'users/profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))"""

# User Dashboard View
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'users/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = self.request.user.teams.all()  # Example: User's teams
        context['posts'] = self.request.user.post_set.all() # Example: User's posts
        return context

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')  # Redirect to login after successful registration
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('posts:newsfeed')  # Redirect to home after successful login
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


"""def profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    reviews = Review.objects.filter(reviewed_user=user).order_by('-created_at')
    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.reviewed_user = user
            review.save()
            return redirect('users:profile', pk=user.pk)

    return render(request, 'users/profile.html', {'user': user, 'reviews': reviews, 'form': form})"""

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    reviews = Review.objects.filter(reviewed_user=user_profile)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    teams = user_profile.user.teams.all()  # Assuming 'user_profile.user' is the related User
    posts = user_profile.user.post_set.all()  # Assuming posts are related to the User model
    
    
    
    return render(request, 'users/profile.html', {
        'user_profile': user_profile,
        'reviews': reviews,
        'average_rating': average_rating,
        'teams': teams,
        'posts': posts,
    })
    
    
class EditProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'users/profile_edit.html'
    form_class = UserProfileForm

    def get_object(self):
        return self.request.user.userprofile  # Fetch the UserProfile, not the User

    def get_success_url(self):
        return reverse('users:profile', kwargs={'username': self.request.user.username})  # Correct keyword

"""@login_required
def edit_profile_view(request):
    user = request.user  # Get the currently logged-in user

    if request.method == 'POST':
        # Assuming you have a form for editing the user profile
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = user.username  # Assign or validate the username
            profile.save()
            messages.success(request, "Your profile was updated successfully!")
            return redirect('profile', username=user.username)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'users/profile_edit.html', {'form': form})"""
    
@login_required
def followers_list(request, username):
    user = get_object_or_404(User, username=username)
    followers = user.followers.all()
    return render(request, 'users/followers_list.html', {'user': user, 'followers': followers})

@login_required
def following_list(request, username):
    user = get_object_or_404(User, username=username)
    following = user.following.all()
    return render(request, 'users/following_list.html', {'user': user, 'following': following})
