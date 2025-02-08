from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('update_email/', views.update_email, name='update_email'),
    path('update_username/', views.update_username, name='update_username'),
    path('update_password/', views.update_password, name='update_password'),
]