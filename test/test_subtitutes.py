from django.test import RequestFactory, TestCase, Client
from search.views import Substitutes
from nutella.models import Product, Category

class TestOneProductView(TestCase):

    def setUp(self):
        self.client = Client()
        cat = Category.objects.create(name="pizza")
        Product.objects.create(name="pizza1", stores="auchan", nutriscore="C", category=cat)
    
    
    def test_get(self):
        """views.get_context_data() sets 'name' in context."""
 
        # Setup request and view.
        response = self.client.get('/search/substitutes/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'substitutes.html')