from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse
from rest_framework import status
from .models import CategoryOfDish, BookTabel
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CategoryOfDish, Dish
from .serializers import CategoryOfDishSerializer, DishSerializer
from django.contrib.auth.decorators import login_required


def base(request):
    context = {"name": "Alex"}
    return render(request, "base.html", context)


def home(request):
    categories = CategoryOfDish.objects.prefetch_related("dishes").all()
    context = {"categories": categories}
    return render(request, "./home/index.html", context)


def menu(request, category=None):
    categories = CategoryOfDish.objects.prefetch_related("dishes").all()

    if category:
        dishes = get_list_or_404(Dish, category__title=category)
    else:
        dishes = Dish.objects.all()

    context = {"categories": categories, "dishes": dishes}
    return render(request, "./menu/index.html", context)


def dish_detail(request, id):
    dish = get_object_or_404(Dish, id=id)
    return render(request, "./dish_detail/index.html", {"dish": dish})


def delivery(request):
    return render(request, "./delivery/index.html")


@login_required(login_url="/auth/login")
def profile(request):
    username = request.user.username
    context = {"username": username}
    return render(request, "./profile/index.html", context)


def book_table(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone_number = request.POST["phone"]
        number_of_guests = request.POST["guests"]
        date = request.POST["date"]
        time = request.POST["time"]
        comment = request.POST.get("comment", "")

        BookTabel.objects.create(
            name=name,
            phone_number=phone_number,
            number_of_guests=number_of_guests,
            date=date,
            time=time,
            comment=comment,
        )

        return HttpResponse("succesfully created")


class CategoryOfDishList(APIView):
    def get(self, request):
        categories = CategoryOfDish.objects.all()
        serializer = CategoryOfDishSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DishList(APIView):
    def get(self, request):
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)
