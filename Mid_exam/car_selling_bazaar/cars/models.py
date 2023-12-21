from django.db import models
from django.contrib.auth.models import User
from posts.models import AdminPost

# Create your models here.

class BuyCars(models.Model):
    place_order = models.ForeignKey(User, on_delete=models.CASCADE)
    admin_post = models.ForeignKey(AdminPost, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.SmallIntegerField(default=0)