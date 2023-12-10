from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'Roll: {self.roll}, Name: {self.name}'
