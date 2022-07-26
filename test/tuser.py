import selenium
from selenium import webdriver
import login
from selenium.webdriver.chrome.options import Options

class TestUser():

    # Set firefox drivers
    self.driver = webdriver.Firefox()
    # Create a user
    self.my_user = login.user.objects.create_user(username=USERNAME, email=None, password=PASSWORD)

    def test_user_url(self):
        self.driver.get(self.get_server_url())
        self.assertEqual(self.driver.current_url, 'http://localhost:8000/')

    def test_user(self):
        self.assertEqual(self.my_user.name, "first_name")
        self.assertEqual(self.my_user.email, "email@email.com")
        self.assertEqual(self.my_user.password, "first_name")
         
    def user_login(eelf):
        self.driver.get('http://127.0.0.1:8000/login')
        username.send_keys(self.my_user.username)
        password.send_keys(self.my_user.password)
        self.driver.find_element_by_css_selector('logBtn').click()

    def test_user_login(self):
        self.user_login()
        self.assertEqual(self.drivers.user, self.my_user)

    # User search
    def user_search(self):
        self.driver.get('http://127.0.0.1:8000/search')
    
    # User save favorite

    # User favorite page
    def user_favorites(self):
        self.driver.get('http://127.0.0.1:8000/favorites')

    def tearDown():
        self.driver.quit()


