from django.db import models
from django.utils import timezone

# Create your models here.

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

