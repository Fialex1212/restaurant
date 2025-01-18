from django.shortcuts import render


def base(request):
    context = {"name": "Alex"}
    return render(request, "base.html", context)

def home(request):
    return render(request, "home.html")

def blog(request):
    return render(request, "blog.html")

def ivents(request):
    return render(request, "ivents.html")

def profile(request):
    context = {"username": "Alex"}
    return render(request, "profile.html", context)

def about(request):
    return render(request, "about.html")