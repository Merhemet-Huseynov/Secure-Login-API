from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer, UserProfileSerializer
from social_django.utils import psa

# Registration endpoint
class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login endpoint (using JWT authentication)
class UserLogin(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        # Authenticate the user
        user = authenticate(request, email=email, password=password)
        if not user:
            raise AuthenticationFailed("Email or password is incorrect")

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)


# Google Login endpoint (as defined in previous steps)
class GoogleLogin(APIView):
    def get(self, request):
        backend = 'google-oauth2'
        try:
            # Perform the social authentication process
            user = psa(request.backend).complete(request=request, backend=backend)
            
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Authentication failed."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Response is returned
        return Response({
            "username": request.user.username,
            "email": request.user.email
        }, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        user.username = request.data.get("username", user.username)
        user.email = request.data.get("email", user.email)
        user.save()
        # Response is returned
        return Response({
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_200_OK)
