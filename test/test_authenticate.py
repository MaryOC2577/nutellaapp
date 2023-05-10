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

        # Test if user return is get the good email
        u = self.auth.authenticate(
            request=None, email="test@test.te", password="secret"
        )
        self.assertEquals(u.email, "test@test.te")

        # Test to get the user from id
        get_u = self.auth.get_user(u.pk)
        self.assertIsNotNone(get_u)

        # Test if user id doesnt existe => get None
        self.assertIsNone(self.auth.get_user(123456))
