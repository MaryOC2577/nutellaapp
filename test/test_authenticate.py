import pytest
from unittest import TestCase
from django.contrib.auth import get_user_model
from django.test import Client
from login.authenticate import EmailAuth


@pytest.mark.django_db
class TestExample(TestCase):
    def setUp(self):
        self.auth = EmailAuth()
        self.client = Client()
        self.credentials = {"username": "testuser", "password": "secret"}
        User = get_user_model()
        User.objects.create_user(**self.credentials)

    def test_login(self):
        self.auth.authenticate(self.credentials)
        # send login data
        response = self.client.post("/login/", self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context["user"].is_authenticated)
