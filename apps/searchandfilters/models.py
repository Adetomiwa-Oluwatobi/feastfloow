from django.db import models
from apps.users.models import UserProfile
# Create your models here.
class SearchQuery(models.Model):
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Query: {self.query} at {self.timestamp}"
class Filter(models.Model):
    name = models.CharField(max_length=100)
    criteria = models.TextField()
    def __str__(self):
        return self.name