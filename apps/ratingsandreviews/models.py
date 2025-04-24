from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.users.models import UserProfile

from django.db import models
from apps.users.models import UserProfile

class Review(models.Model):
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="reviews_given")
    reviewed_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="reviews_received")
    rating = models.IntegerField()
    review_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
