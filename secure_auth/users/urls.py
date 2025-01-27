from django.urls import path
from .views import UserRegistration, UserLogin, GoogleLogin, UserProfile

urlpatterns = [
    path("register/", UserRegistration.as_view(), name="user_register"),
    path("login/", UserLogin.as_view(), name="user_login"),
    path("google/", GoogleLogin.as_view(), name="google_login"),
    path("profile/", UserProfile.as_view(), name="user_profile"),
]
