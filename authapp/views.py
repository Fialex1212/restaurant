from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


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


@login_required(login_url="/auth/login")
def update_email(request):
    user = request.user
    if request.method == "POST":
        new_email = request.POST["email"]
        if (
            new_email != user.email
            and get_user_model().objects.filter(email=new_email).exists()
        ):
            messages.error(request, "Email already in use.")
        else:
            user.email = new_email
            user.save()
            messages.success(request, "Your email has been updated.")
            return redirect("profile-settings")
    return render(request, "./update_email.html")


@login_required(login_url="/auth/login")
def update_username(request):
    user = request.user
    if request.method == "POST":
        new_username = request.POST["username"]
        if (
            new_username != user.username
            and get_user_model().objects.filter(email=new_username).exists()
        ):
            messages.error(request, "Username already in use.")
        else:
            user.username = new_username
            user.save()
            messages.success(request, "Your username has been updated.")
            return redirect("profile-settings")
    return render(request, "./update_username.html")


@login_required(login_url="/auth/login")
def update_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password has been updated.")
            return redirect("profile-settings")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "./update_password.html")
