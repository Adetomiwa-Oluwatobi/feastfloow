from django.shortcuts import render, redirect, get_object_or_404
from apps.users.models import UserProfile
from .forms import ReviewForm
from .models import Review


def add_review(request, user_id):
    user_profile = get_object_or_404(UserProfile, id=user_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer = request.user.profile  # Link to the logged-in user's UserProfile
            review.reviewed_user = user_profile
            review.save()
            return redirect('users:profile', username=user_profile.user.username)  # Redirect to the profile page
    else:
        review_form = ReviewForm()

    return render(request, 'ratingsandreviews/add_review.html', {
        'user_profile': user_profile,
        'review_form': review_form,
    })
