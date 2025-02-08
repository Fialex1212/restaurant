from django.contrib import admin
from .models import (
    BookTabel,
    CategoryOfDish,
    Dish,
    Order,
    OrderItem, 
    ContactUs
)

admin.site.register(BookTabel)
admin.site.register(CategoryOfDish)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ContactUs)