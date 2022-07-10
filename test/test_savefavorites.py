from django.test import RequestFactory, TestCase, Client
from search.views import SaveFavorites
from login.authenticate import EmailAuth
from nutella.models import Category, Product
from django.contrib.auth import get_user_model

class TestSaveFavorites(TestCase):

    def setUp(self):
        self.auth = EmailAuth()
        self.client = Client()
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        cat = Category.objects.create(name="pizza")
        Product.objects.create(name="pizza1", stores="auchan", nutriscore="C", category=cat)
        User = get_user_model()
        User.objects.create_user(**self.credentials)
        self.auth.authenticate(self.credentials)
        response = self.client.post('/login/', self.credentials, follow=True)

    def test_save_favorites(self):
        response = self.client.get('/search/savefavorite/1/')
        self.assertEqual(response.status_code, 301)
        self.assertTemplateUsed(response, 'product.html')