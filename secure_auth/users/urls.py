from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.UserRegistration.as_view(), name="user_register"),
    path("login/", views.UserLogin.as_view(), name="user_login"),
    path("google/", views.GoogleLogin.as_view(), name="google_login"),
    path("profile/", views.UserProfile.as_view(), name="user_profile"),
]