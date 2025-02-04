from django.utils.timezone import now
from django.db import models
import uuid


class BookTabel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Name")
    phone = models.CharField(max_length=16, verbose_name="Phone Number")
    date = models.DateField(verbose_name="Date")
    time = models.TimeField(verbose_name="Time")
    guests = models.PositiveIntegerField(verbose_name="Number of Guests")
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
