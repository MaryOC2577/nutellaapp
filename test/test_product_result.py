import json
from django.test import TestCase, Client

# from search.views import ProductResult
from nutella.models import Product, Category


class TestOneProductView(TestCase):
    def setUp(self):
        self.client = Client()
        cat = Category.objects.create(name="pizza")
        with open("./test/products.json") as l_product:
            data = json.load(l_product)
            for one_product in data:
                if cat == one_product["category"]:
                    Product.objects.create(**one_product)

    def test_get(self):
        """views.get_context_data() sets 'name' in context."""

        # Setup request and view.
        response = self.client.get("/search/result/?expression=pizza")
        # problème redirection à corriger
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "result.html")
