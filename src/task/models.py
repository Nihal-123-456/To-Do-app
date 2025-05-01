from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Task(models.Model):
    user = models.ForeignKey(User, related_name='task', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title