from django.utils.timezone import now
from django.db import models
import uuid
from authapp.models import CustomUser


class BookTabel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Name")
    phone = models.CharField(max_length=16, verbose_name="Phone Number", default=None)
    date = models.DateField(verbose_name="Date")
    time = models.TimeField(verbose_name="Time")
    guests = models.PositiveIntegerField(verbose_name="Number of Guests", default=1)
    comment = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.phone_number}, {self.date}, {self.time}"


class CategoryOfDish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Dish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(
        CategoryOfDish, on_delete=models.CASCADE, related_name="dishes"
    )
    image = models.ImageField(upload_to="uploads/dishes")

    def __str__(self):
        return f"{self.title}, {self.price}"
    

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[("Pending", "Pending"), ("In progress", "In progress"), ("Completed", "Completed")], default="Pending")
    
    def __str__(self):
        return f"Order {self.id} - {self.status}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.dish.title} x {self.quantity}"