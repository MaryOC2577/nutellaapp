from django.test import TestCase, Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from nutella.models import Product, Category
from selenium import webdriver
from django.urls import reverse


class TestOneProductView(StaticLiveServerTestCase):
    def setUp(self):
        self.client = Client()
        cat = Category.objects.create(name="pizza")
        Product.objects.create(
            name="pizza1", stores="auchan", nutriscore="C", category=cat
        )
        # Set firefox drivers
        self.browser = webdriver.Firefox(executable_path="geckodriver")

    def tearDown(self):
        self.browser.close()

    def test_get(self):
        """views.get_context_data() sets 'name' in context."""

        # Setup request and view.
        # response = self.client.get("/search/oneproduct/1/")
        response = self.client.get(reverse("/" + "oneproduct" + "/1/"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "product.html")
