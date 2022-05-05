from django.test import Client

class TestUrls():

    def setUp(self):
        self.client = Client()
    
    def test_home():
        response = self.client.get('home/')
        self.assertEqual(response.status_code, 200)
    
    def test_login():
        response = self.client.get('login/')
        self.assertEqual(response.status_code, 200)

    def test_logout():
        response = self.client.get('logout/')
        self.assertEqual(response.status_code, 200)

    def test_registration():
        response = self.client.get('registration/')
        self.assertEqual(response.status_code, 200)

    def test_search():
        response = self.client.get('search/')
        self.assertEqual(response.status_code, 200)

    def test_result():
        response = self.client.get('result/')
        self.assertEqual(response.status_code, 200)

    def test_oneproduct():
        response = self.client.get('oneproduct/', kwargs={'pk':1})
        self.assertEqual(response.status_code, 200)

    def test_substitutes():
        response = self.client.get('substitutes/', kwargs={'pk':1})
        self.assertEqual(response.status_code, 200)

    def test_favorites():
        response = self.client.get('favorites/')
        self.assertEqual(response.status_code, 200)

    def test_delete_favorite():
        response = self.client.get('delete/', kwargs={'pk':1})
        self.assertEqual(response.status_code, 200)
    