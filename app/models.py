from django.utils.timezone import now
from django.db import models
import uuid


class BookTabel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=16)
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
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
