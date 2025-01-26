from django.urls import path, include
from . import views

urlpatterns = [
    path("base/", views.base, name="base"),
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("profile/", views.profile, name="profile"),
    path("submit-booking", views.book_table, name="submit_booking"),
    path("auth/", include("authapp.urls"))
    
]

