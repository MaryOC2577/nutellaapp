from django.test import TestCase, Client

# from favorite.views import ShowFavorites
from django.contrib.auth import get_user_model


class TestFavoriteViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {"username": "testuser", "password": "secret"}
        User = get_user_model()
        User.objects.create_user(**self.credentials)

    def test_get(self):
        """views.get_context_data() sets 'name' in context."""

        # Setup request and view.
        response = self.client.post("/login/", self.credentials, follow=True)
        response = self.client.get("/favorites/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "favorite/favorite_list.html")
