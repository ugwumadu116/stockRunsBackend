# import json
# from django.contrib.auth.models import User
# from django.urls import reverse
# from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
# from rest_framework import status


class TestEqualValue(APITestCase):
    def test_equal(self):
        self.assertEqual("test", "test")
