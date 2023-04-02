from django.db import models
from django.utils import timezone
# Create your models here.
class Task(models.Model):
    task_name = models.TextField(max_length=500)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
