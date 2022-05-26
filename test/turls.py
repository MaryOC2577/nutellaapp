from django.test import Client


class TestUrls():

    def setUp(self):
        self.client = Client()
    
    def test_home(self):
        response = self.client.get('home/')
        self.assertEqual(response.status_code, 200)
            
    def test_login(self):
        response = self.client.get('login/')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('logout/')
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        response = self.client.get('registration/')
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        response = self.client.get('search/')
        self.assertEqual(response.status_code, 200)

    def test_result(self):
        response = self.client.get('result/')
        self.assertEqual(response.status_code, 200)

    def test_oneproduct(self):
        response = self.client.get('oneproduct/1/')
        self.assertEqual(response.status_code, 200)

    def test_substitutes(self):
        response = self.client.get('substitutes/1/')
        self.assertEqual(response.status_code, 200)

    def test_favorites(self):
        response = self.client.get('favorites/')
        self.assertEqual(response.status_code, 200)

    def test_delete_favorite(self):
        response = self.client.get('delete/1/')
        self.assertEqual(response.status_code, 200)
    