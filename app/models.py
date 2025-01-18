from django.utils.timezone import now
from django.db import models
import uuid


class BookTabel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    comment = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.phone_number}, {self.date}, {self.time}"