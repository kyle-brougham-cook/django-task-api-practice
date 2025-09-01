from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

userModel = get_user_model()

class Task(models.Model):
    # user = models.ForeignKey(userModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

