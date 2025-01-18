from django.urls import path
from .views import (
    base,
    home,
    blog,
    ivents,
    profile,
    about,
    book_table
)

urlpatterns = [
    path("base/", base, name="base"),
    path("", home, name="home"),
    path("blog/", blog, name="blog"),
    path("ivents/", ivents, name="ivents"),
    path("profile/", profile, name="profile"),
    path("about/", about, name="about"),
    path('submit-booking', book_table, name='submit_booking'),
]
