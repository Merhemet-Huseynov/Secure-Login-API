from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from social_django.views import auth as social_auth

class GoogleLogin(APIView):
    def get(self, request):
        return social_auth.process(request, "google-oauth2")

def google_login(request):
    return social_auth(request, "google-oauth2")

class UserProfile(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email
        })

    def put(self, request):
        user = request.user
        user.username = request.data.get("username", user.username)
        user.email = request.data.get("email", user.email)
        user.save()
        return Response({
            "username": user.username,
            "email": user.email
        })