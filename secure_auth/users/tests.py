from django.test import TestCase
from rest_framework.test import APIClient
from .models import CustomUser

class UserTestCase(TestCase):
    def setUp(self):
        # Test üçün APIClient və istifadəçi yaradılır
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email="test@example.com",
            username="testuser", 
            password="testpass"
        )

    def test_user_registration(self):
        # Yeni istifadəçi qeydiyyatı üçün POST sorğusu
        response = self.client.post(
            "/api/auth/users/", 
            {
                "email": "newuser@example.com", 
                "username": "newuser", 
                "password": "newpassword123"
            },
            format='json'
        )

        # Cavabın status kodunu yoxlayırıq
        print(response.data)
        self.assertEqual(response.status_code, 201)