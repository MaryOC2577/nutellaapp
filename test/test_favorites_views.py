from django.test import RequestFactory, TestCase, Client
from favorite.views import ShowFavorites

class TestFavoriteViews(TestCase):

    def setUp(self):
        self.client = Client()
    
    
    def test_get(self):
        """views.get_context_data() sets 'name' in context."""
 
        # Setup request and view.
        response = self.client.get('/favorites/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorite_list.html')