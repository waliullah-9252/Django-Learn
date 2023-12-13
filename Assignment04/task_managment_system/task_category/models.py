from django.db import models

# Create your models here.
class TaskCategory(models.Model):
    category_name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.category_name
