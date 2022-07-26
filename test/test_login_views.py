
from django.test import RequestFactory, TestCase, Client
from login.views import LoginView

class TestLoginViews(TestCase):

    def setUp(self):
        self.client = Client()
    
    
    def test_get(self):
        """views.get_context_data() sets 'name' in context."""
 
        # Setup request and view.
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
