from django.db import models
from brands.models import Category  # Assuming Brand model is defined in brands app
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200, default='')  # Default empty string for image URL
    car_name = models.CharField(max_length=100, default='Unnamed Car')  # Default car name
    car_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Default price 0.0
    brand = models.ForeignKey(Category, on_delete=models.CASCADE)  # ForeignKey to Brand model
    car_quantity = models.PositiveIntegerField(default=0)  # Default quantity 0
    car_description = models.TextField(default='No description available')  # Default description

    def __str__(self):
        return self.title


class Order(models.Model):
    car = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order #{self.id} - {self.car.car_name} by {self.user.username}"
    
    