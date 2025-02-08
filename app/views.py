from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.http import HttpResponse
from rest_framework import status
from .models import CategoryOfDish, BookTabel
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CategoryOfDish, Dish
from .serializers import CategoryOfDishSerializer, DishSerializer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CallbackForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import BookingForm



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


def basket(request):
    return render(request, "./basket/index.html")


@login_required(login_url="/auth/login")
def profile(request):
    username = request.user.username
    context = {"username": username}
    return render(request, "./profile/index.html", context)


def about(request):
    return render(request, "./about/index.html")


def contacts(request):
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            # Example: Save to database or send an email
            # CallbackRequest.objects.create(name=name, phone=phone)
            messages.success(request, "Ваша заявка принята! Мы вам перезвоним.")
            return redirect("contacts")
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = CallbackForm()
    return render(request, "./contacts/index.html", {"form": form})


def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базу
            messages.success(request, "Your booking has been submitted successfully!")
            return JsonResponse({'status': 'success', 'message': 'Booking submitted successfully!'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'errors': errors}, status=400)
    else:
        form = BookingForm()


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
