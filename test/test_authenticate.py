from unittest import TestCase
from unittest.mock import patch
from django.contrib.auth.models import User

class TestExample(TestCase):
    # patch("example.logging.info")
    # def test_logging(self, info_mock):
    #     authenticate()
    #     info_mock.assert_called_once_with("Hello, World!")
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_authenticated)