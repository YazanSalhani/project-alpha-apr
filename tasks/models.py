from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=timezone.now)
    is_completed = False
    project = models.ForeignKey(
        "projects.Project",
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
