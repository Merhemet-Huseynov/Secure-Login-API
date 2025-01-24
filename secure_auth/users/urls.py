from django.urls import path, include
from . import views

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("google/", views.google_login, name="google_login"),
    path("profile/", views.UserProfile.as_view(), name="user_profile"),  # Burada .as_view() əlavə olunub
]
