import time
import login
import selenium

from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.firefox import options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestUser(StaticLiveServerTestCase):

    def setUp(self):
        # Set firefox drivers
        self.browser = webdriver.Firefox(executable_path='geckodriver')
        # Create a user
        # self.my_user = login.user.objects.create_user(username=USERNAME, email=None, password=PASSWORD)

    def tearDown(self):
        self.browser.close()

    def test_valid_registration(self):
        self.browser.get(self.live_server_url + reverse("login"))
        time.sleep(1)
        self.browser.find_element_by_name("username").send_keys("maryline")
        time.sleep(1)
        self.browser.find_element_by_name("password").send_keys("monroe")
        time.sleep(1)
        self.browser.find_element_by_id("logBtn").click()
        time.sleep(5)
        redirection_url = self.live_server_url + reverse("login")
        self.assertEquals(self.browser.current_url, redirection_url)
    # def test_user_url(self):
    #     self.driver.get(self.get_server_url())
    #     self.assertEqual(self.driver.current_url, 'http://localhost:8000/')

    # def test_user(self):
    #     self.assertEqual(self.my_user.name, "first_name")
    #     self.assertEqual(self.my_user.email, "email@email.com")
    #     self.assertEqual(self.my_user.password, "first_name")
         
    # def user_login(eelf):
    #     self.driver.get('http://127.0.0.1:8000/login')
    #     username.send_keys(self.my_user.username)
    #     password.send_keys(self.my_user.password)
    #     self.driver.find_element_by_css_selector('logBtn').click()

    # def test_user_login(self):
    #     self.user_login()
    #     self.assertEqual(self.drivers.user, self.my_user)

    # # User search
    # def user_search(self):
    #     self.driver.get('http://127.0.0.1:8000/search')
    
    # # User save favorite

    # # User favorite page
    # def user_favorites(self):
    #     self.driver.get('http://127.0.0.1:8000/favorites')