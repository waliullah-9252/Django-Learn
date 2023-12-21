from django.db import models
from brands.models import BrandModel
# Create your models here.

class AdminPost(models.Model):
    image = models.ImageField(upload_to='posts/media/uploads/')
    car_name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(default=None)
    price = models.CharField(max_length=100)
    brand = models.ManyToManyField(BrandModel, null=True, blank=True)

    def __str__(self):
        return self.car_name
    
class Comment(models.Model):
    post = models.ForeignKey(AdminPost, on_delete = models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comments by: {self.name}'

