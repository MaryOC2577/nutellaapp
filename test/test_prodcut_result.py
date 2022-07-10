from django.test import RequestFactory, TestCase, Client
from search.views import ProductResult
from nutella.models import Product, Category

class TestOneProductView(TestCase):

    def setUp(self):
        self.client = Client()
        cat = Category.objects.create(name="pizza")
        Product.objects.create(name="pizza1", stores="auchan", nutriscore="C", category=cat)
        Product.objects.create(name="pizza2", stores="carrefour", nutriscore="B", category=cat)
        Product.objects.create(name="pizza3", stores="leclerc", nutriscore="A", category=cat)
        Product.objects.create(name="pizza4", stores="super u", nutriscore="A", category=cat)
        Product.objects.create(name="pizza5", stores="aldi", nutriscore="D", category=cat)
    
    
    def test_get(self):
        """views.get_context_data() sets 'name' in context."""
 
        # Setup request and view.
        response = self.client.get('/search/result/?expression=pizza')
        # problème redirection à corriger
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'result.html')