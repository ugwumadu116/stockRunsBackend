import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


class PhoneStorePost(APITestCase):
    def test_create_phone(self):
        self.assertEqual("test", "test")
