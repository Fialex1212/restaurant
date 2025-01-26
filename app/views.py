from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CategoryOfDish, BookTabel


def base(request):
    context = {"name": "Alex"}
    return render(request, "base.html", context)

def home(request):
    categories = CategoryOfDish.objects.prefetch_related("dishes").all()
    context = {"categories": categories}
    return render(request, "./home/index.html", context)


def menu(request):
    categories = CategoryOfDish.objects.prefetch_related("dishes").all()
    context = {"categories": categories}
    return render(request, "./menu/index.html", context)


def profile(request):
    context = {"username": "Alex"}
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
