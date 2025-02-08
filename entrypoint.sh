#!/bin/sh

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."
until python -c "import socket; s = socket.socket(); s.connect(('db', 5432))" 2>/dev/null; do
  sleep 1
done
echo "PostgreSQL is up!"

# Apply migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
echo "Creating superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
from app.models import CategoryOfDish, Dish
import os

# Create superuser
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@gmail.com', 'admin1')
    print("Superuser created!")
else:
    print("Superuser already exists.")

# Create default categories if not exist
categories = ["Meet", "Salates", "Soups", "Desserts"]
for category_title in categories:
    if not CategoryOfDish.objects.filter(title=category_title).exists():
        CategoryOfDish.objects.create(title=category_title)
        print(f"Category '{category_title}' created!")

# Create default dishes if not exist
dishes = [
    {
    "title": "МУС З ПРАЛІНЕ З ЛІСОВОГО ГОРІХУ ТА СОЛОНОЮ КАРАМЕЛЛЮ (125г)", 
    "description": "МУС З ПРАЛІНЕ З ЛІСОВОГО ГОРІХУ ТА СОЛОНОЮ КАРАМЕЛЛЮ (125г)", 
    "price": 100, 
    "category": "Desserts", 
    "image": "uploads/dishes/mus.jpg"},
    {
    "title": "ЗЕЛЕНИЙ САЛАТ З ГРЕЙПФРУТОМ ТА ЧИЛІ ПЕРЦЕМ (330г)", 
    "description": "Мікс-салат з цитрусами, гранатом, перцем чилі та горіхами під соусом помело.", 
    "price": 150, 
    "category": "Salates", 
    "image": "uploads/dishes/green_salate.jpg"},
    {
    "title": "ЛАКСА З МОРЕПРОДУКТАМИ І РИСОВОЮ ЛОКШИНОЮ (550г)", 
    "description": "Пікантний суп з морепродуктами на основі бульйону з додаванням яйця та перця чилі.", 
    "price": 200, 
    "category": "Soups", 
    "image": "uploads/dishes/soup.jpg"},
    {
    "title": "ЯПОНСЬКИЙ СТЕЙК ВАГЮ З ОВОЧАМИ ТА ПЮРЕ З ЦВІТНОЇ КАПУСТИ (1шт)", 
    "description": "Японський стейк вагю з овочами та медово-гранатовим соусом.", 
    "price": 300, 
    "category": "Meet", 
    "image": "uploads/dishes/meet.png"}
]

for dish_data in dishes:
    category = CategoryOfDish.objects.get(title=dish_data["category"])
    if not Dish.objects.filter(title=dish_data["title"]).exists():
        Dish.objects.create(
            title=dish_data["title"],
            description=dish_data["description"],
            price=dish_data["price"],
            category=category,
            image=dish_data["image"]
        )
        print(f"Dish '{dish_data['title']}' created!")
    else:
        print(f"Dish '{dish_data['title']}' already exists.")

EOF

# Start Django server
exec "$@"
