from django.db import models
from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    restaurant_name = models.CharField(max_length=255)
    rating = models.FloatField()
    distance = models.FloatField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.restaurant_name} - {self.user.username}'


# Create your models here.
