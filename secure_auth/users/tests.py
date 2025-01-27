from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a new user
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword"
        )
        # Obtaining a JWT token
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

    # Test 1: Registration
    def test_user_registration(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword",
        }
        response = self.client.post("/api/register/", data, format="json") 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    # Test 2: Introduction
    def test_user_login(self):
        data = {
            "email": "testuser@example.com",
            "password": "testpassword",
        }
        response = self.client.post("/api/login/", data, format="json") 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    # Test 3: Profile Information
    def test_user_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        response = self.client.get("/api/profile/") 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")
        self.assertEqual(response.data["email"], "testuser@example.com")

    # Test 4: Update Profile Information
    def test_update_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        data = {
            "username": "updateduser",
            "email": "updateduser@example.com",
        }
        response = self.client.put("/api/profile/", data, format="json")  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "updateduser")
        self.assertEqual(response.data["email"], "updateduser@example.com")