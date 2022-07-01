import pytest
from unittest import TestCase
from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.test import Client

@pytest.mark.django_db
class TestExample(TestCase):
    # patch("example.logging.info")
    # def test_logging(self, info_mock):
    #     authenticate()
    #     info_mock.assert_called_once_with("Hello, World!")
    
    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User = get_user_model()
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_authenticated)