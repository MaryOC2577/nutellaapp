from django.test import TestCase, Client
from login.authenticate import EmailAuth
from nutella.models import Category, Product, Favorite
from django.contrib.auth import get_user_model


class TestSaveFavorites(TestCase):
    def setUp(self):
        self.auth = EmailAuth()
        self.client = Client()
        self.credentials = {"username": "testuser", "password": "secret"}
        cat = Category.objects.create(name="pizza")
        self.fake_product = Product.objects.create(
            name="pizza1", stores="auchan", nutriscore="C", category=cat
        )
        User = get_user_model()
        self.fake_user = User.objects.create_user(**self.credentials)

        self.auth.authenticate(self.credentials)
        response = self.client.post("/login/", self.credentials, follow=True)
        return response

    def test_save_favorites(self):
        Favorite.objects.create(product=self.fake_product, user=self.fake_user)
        response = self.client.get("/search/savefavorite/1/")
        self.assertEqual(response.status_code, 301)
        self.assertTemplateUsed(response, "product.html")
