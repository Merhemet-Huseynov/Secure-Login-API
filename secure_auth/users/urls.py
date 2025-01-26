from django.urls import path
from .views import UserRegistration, UserLogin, GoogleLogin, UserProfile

urlpatterns = [
    path("auth/register/", UserRegistration.as_view(), name="user_register"),
    path("auth/login/", UserLogin.as_view(), name="user_login"),
    path("auth/google/", GoogleLogin.as_view(), name="google_login"),
    path("auth/profile/", UserProfile.as_view(), name="user_profile"),
]