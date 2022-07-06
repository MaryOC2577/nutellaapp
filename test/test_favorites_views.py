from django.test import RequestFactory, TestCase, Client
from favorite.views import ShowFavorites

class TestFavoriteViews(TestCase):

    def setUp(self):
        self.client = Client()
    
    
    def test_get(self):
        """views.get_context_data() sets 'name' in context."""
 
        # Setup request and view.
        response = self.client.get('/favorites/')
        print("url : ", response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorite_list.html')

      
    def test_favorites_set_in_context(self):
        request = RequestFactory().get('favorites')
        view = ShowFavorites()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('favorites', context)