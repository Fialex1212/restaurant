from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Login successful!")
            print("Loggined")
            return redirect("/")
        else:
            print("Error")
            messages.error(request, "Invalid email or password.")
    return render(request, "./auth/login.html")


def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if not get_user_model().objects.filter(email=email).exists():
                user = get_user_model().objects.create_user(
                    username=username, email=email, password=password
                )
                messages.success(request, "Registration successful!")
                return redirect("login")
            else:
                messages.error(request, "Email already exists.")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, "./auth/register.html")

@login_required(login_url="/auth/login")
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")
