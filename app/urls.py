from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("menu/", views.menu, name="menu"),
    path("menu/<str:category>/", views.menu, name="menu_by_category"),
    path("dish_detail/<str:id>", views.dish_detail, name="dish_detail"),
    path("basket/", views.basket, name="basket"),
    path('api/checkout/', views.checkout, name="chekout"),

    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),

    path("profile/", views.profile, name="profile"),
    path("profile/orders", views.my_orders, name="my_orders"),
    path("profile/settings", views.profile_settings, name="profile-settings"),
    path('profile/settings/update_email/', views.update_email, name='update_email'),
    path('profile/settings/update_username/', views.update_username, name='update_username'),
    path('profile/settings/update_password/', views.update_password, name='update_password'),
    path("delivery_trems/", views.delivery_trems, name="delivery_trems"),

    path("submit-booking", views.book_table, name="submit_booking"),
    path("auth/", include("authapp.urls")),
]

