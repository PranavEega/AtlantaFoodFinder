from django.db import models
from django.contrib.auth.models import User


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensures that each favorite is tied to a user
    restaurant_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)  # Ensure the address is stored
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    distance = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.restaurant_name} ({self.address}) - {self.user.username}"
# Create your models here.
