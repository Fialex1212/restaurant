from django.urls import path, include
from . import views

urlpatterns = [
    path("base/", views.base, name="base"),
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("dish_detail/<str:id>", views.dish_detail, name="dish_detail"),
    path("delivery/", views.delivery, name="delivery"),
    path("profile/", views.profile, name="profile"),
    path("submit-booking", views.book_table, name="submit_booking"),
    path("auth/", include("authapp.urls")),
    path('api/categories/', views.CategoryOfDishList.as_view(), name='category-list'),
    path('api/dishes/', views.DishList.as_view(), name='dish-list'),

]

