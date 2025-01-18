from django.contrib import admin
from .models import (
    BookTabel,
    CategoryOfDish,
    Dish
)

admin.site.register(BookTabel)
admin.site.register(CategoryOfDish)
admin.site.register(Dish)