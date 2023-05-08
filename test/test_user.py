import time
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from login.models import User
from django.test import Client


class TestUser(StaticLiveServerTestCase):
    def setUp(self):
        # Set firefox drivers
        self.browser = webdriver.Firefox(executable_path="geckodriver")

    def tearDown(self):
        self.browser.close()

    def test_valid_registration(self):
        self.browser.get(self.live_server_url + reverse("login"))
        time.sleep(1)
        self.browser.find_element(By.NAME, "username").send_keys("test1")
        time.sleep(1)
        self.browser.find_element(By.NAME, "password").send_keys("test1")
        time.sleep(1)
        self.browser.find_element(By.ID, "LogButton").click()
        time.sleep(5)
        redirection_url = self.live_server_url + reverse("login")
        self.assertEqual(self.browser.current_url, redirection_url)

    def test_missing_password(self):
        self.browser.get(self.live_server_url + reverse("login"))
        time.sleep(1)
        self.browser.find_element(By.NAME, "username").send_keys("test1")
        time.sleep(1)
        self.browser.find_element(By.ID, "LogButton").click()
        time.sleep(5)
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("login")
        )

    def test_missing_username(self):
        self.browser.get(self.live_server_url + reverse("login"))
        time.sleep(1)
        self.browser.find_element(By.NAME, "password").send_keys("test1")
        time.sleep(1)
        self.browser.find_element(By.ID, "LogButton").click()
        time.sleep(5)
        redirection_url = self.live_server_url + reverse("login")
        self.assertEqual(self.browser.current_url, redirection_url)


class TestLoginPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path="geckodriver")
        self.test_user = User.objects.create(
            username="test1",
            email="test1@test.fr",
            password="test1",
        )

    def tearDown(self):
        self.browser.close()

    def test_valid_login(self):
        self.client = Client()
        response = self.client.get("/login/")
        self.browser.get(self.live_server_url + reverse("login"))
        time.sleep(1)
        self.browser.find_element(By.NAME, "username").send_keys("test1")
        time.sleep(1)
        self.browser.find_element(By.NAME, "password").send_keys("test1")
        time.sleep(1)
        self.browser.find_element(By.ID, "LogButton").click()
        time.sleep(5)
        redirection_url = self.live_server_url + reverse("login")
        self.assertEqual(self.browser.current_url, redirection_url)
        self.browser.find_element(By.NAME, "username").send_keys("test1")
        time.sleep(1)
        self.browser.find_element(By.NAME, "password").send_keys("test1")
        self.browser.find_element(By.ID, "LogButton").click()
        time.sleep(5)
        self.assertTemplateUsed(response, "login.html")


class TestSearchPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path="geckodriver")

    def tearDown(self):
        self.browser.close()

    def test_Search_page(self):
        self.browser.get(self.live_server_url + reverse("search"))
        searchFiled = self.browser.find_element(By.NAME, "SearchField").send_keys(
            "pizza"
        )
        self.browser.find_element(By.ID, "ValidSearch").click()
        self.assertEqual(searchFiled, "pizza")
