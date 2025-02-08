import json
import logging

from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import CategoryOfDish, Dish, Order, OrderItem
from .forms import CallbackForm, BookingForm

# LOGGER
logger = logging.getLogger("django")


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


@csrf_exempt
@login_required(login_url="/auth/login")
def checkout(request):
    logger.info(
        f"User: {request.user}, Authenticated: {request.user.is_authenticated}, Method: {request.method}"
    )

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            basket = data.get("basket", [])
            total_price = sum(
                float(item["price"]) * int(item["quantity"]) for item in basket
            )
            order = Order.objects.create(
                user=request.user, total_price=total_price, status="Pending"
            )
            for item in basket:
                dish = Dish.objects.get(id=item["id"])
                OrderItem.objects.create(
                    order=order, dish=dish, quantity=item["quantity"], price=dish.price
                )

            logger.info(f"Order created successfully for user {request.user.email}")
            return JsonResponse({"success": True})

        except Exception as e:
            logger.error(f"Error processing checkout: {e}")
            return JsonResponse({"success": False, "error": str(e)})

    logger.warning("Invalid request method received for checkout")
    return JsonResponse({"success": False, "error": "Invalid request method"})


def about(request):
    return render(request, "./about/index.html")


def contacts(request):
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            messages.success(request, "Ваша заявка принята! Мы вам перезвоним.")
            logger.info(f"Callback request received: {name}, {phone}")
            return redirect("contacts")
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
            logger.warning(f"Invalid form submission: {form.errors}")
    else:
        form = CallbackForm()
    return render(request, "./contacts/index.html", {"form": form})


@login_required(login_url="/auth/login")
def profile(request):
    context = {"user": request.user}
    return render(request, "./profile/index.html", context)


@login_required(login_url="/auth/login")
def my_orders(request):
    orders = Order.objects.filter(user=request.user)

    context = {"orders": orders, "user": request.user}

    return render(request, "./profile/orders.html", context)


@login_required(login_url="/auth/login")
def profile_settings(request):

    context = {"user": request.user}

    return render(request, "./profile/settings.html", context)


def delivery_trems(request):
    return render(request, "./profile/delivery_trems.html")


def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been submitted successfully!")
            logger.info(f"Booking submitted by {request.user}: {form.cleaned_data}")
            return JsonResponse(
                {"status": "success", "message": "Booking submitted successfully!"}
            )
        else:
            errors = form.errors.as_json()
            logger.warning(f"Booking form errors: {errors}")
            return JsonResponse({"status": "error", "errors": errors}, status=400)
    else:
        form = BookingForm()
    return render(request, "book_table.html", {"form": form})
