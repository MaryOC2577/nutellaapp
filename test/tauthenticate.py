from unittest import TestCase
from unittest.mock import patch
from login.authenticate.EmailAuth import authenticate

class TestExample(TestCase):
    patch("example.logging.info")
    def test_logging(self, info_mock):
        authenticate()
        info_mock.assert_called_once_with("Hello, World!")