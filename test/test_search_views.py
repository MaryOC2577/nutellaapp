from django.test import RequestFactory, TestCase, Client
from search.views import ProductResult

class TestSearchViews(TestCase):

    def setUp(self):
        self.client = Client()
    
    
    def test_get(self):
        """views.get_context_data() sets 'name' in context."""
 
        # Setup request and view.
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')