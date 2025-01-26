from rest_framework import serializers
from .models import CategoryOfDish, Dish

class CategoryOfDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryOfDish
        fields = ['id', 'title']

class DishSerializer(serializers.ModelSerializer):
    category = CategoryOfDishSerializer()  # Вложенный сериализатор категории

    class Meta:
        model = Dish
        fields = ['id', 'title', 'description', 'price', 'category', 'image']