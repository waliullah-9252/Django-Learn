from django.db import models
from task_category.models import TaskCategory

# Create your models here.

class TaskModel(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    category = models.ManyToManyField(TaskCategory, related_name='categories')
    is_complete = models.BooleanField(default=False)
    task_assigned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title