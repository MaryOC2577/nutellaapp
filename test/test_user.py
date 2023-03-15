import time
from django.urls import reverse
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestUser(StaticLiveServerTestCase):
    def setUp(self):
        # Set firefox drivers
        self.browser = webdriver.Firefox(executable_path="geckodriver")

    def tearDown(self):
        self.browser.close()

    def test_valid_registration(self):
        self.browser.get(self.live_server_url + reverse("login"))
        time.sleep(1)
        self.browser.find_element_by_name("username").send_keys("test1")
        time.sleep(1)
        self.browser.find_element_by_name("password").send_keys("test1")
        time.sleep(1)
        self.browser.find_element_by_id("LogButton").click()
        time.sleep(5)
        redirection_url = self.live_server_url + reverse("login")
        self.assertEquals(self.browser.current_url, redirection_url)

    def test_missing_password(self):
        self.browser.get(self.live_server_url + reverse("login"))
        time.sleep(1)
        self.browser.find_element_by_name("username").send_keys("test1")
        time.sleep(1)
        self.browser.find_element_by_id("LogButton").click()
        time.sleep(5)
        self.assertEquals(
            self.browser.current_url, self.live_server_url + reverse("login")
        )

    def test_missing_username(self):
        self.browser.get(self.live_server_url + reverse("login"))
        time.sleep(1)
        self.browser.find_element_by_name("password").send_keys("test1")
        time.sleep(1)
        self.browser.find_element_by_id("LogButton").click()
        time.sleep(5)
        redirection_url = self.live_server_url + reverse("login")
        self.assertEquals(self.browser.current_url, redirection_url)


class TestLoginPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path="geckodriver")
        # self.test_user = User.objects.create(
        #     username="test1",
        #     email="test1@test.fr",
        #     passwword="test1",
        # )
        self.browser.close()

    def test_valid_login(self):
        self.browser.get(self.live_server_url + reverse("login"))
        time.sleep(1)
        self.browser.find_element_by_name("username").send_keys("test1")
        time.sleep(1)
        self.browser.find_element_by_name("password").send_keys("test1")
        time.sleep(1)
        self.browser.find_element_by_id("LogButton").click()
        time.sleep(5)
        redirection_url = self.live_server_url + reverse("login")
        self.assertEquals(self.browser.current_url, redirection_url)
        self.browser.find_element_by_name("username").send_keys("test1")
        time.sleep(1)
        self.browser.find_element_by_name("password").send_keys("test1")
        self.browser.find_element_by_id("LogButton").click()
        time.sleep(5)
        self.assertEquals(self.browser.current_url, self.live_server_url)


class TestSearchPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path="geckodriver")

    def tearDown(self):
        self.browser.close()

    def test_Search_page(self):
        self.browser.get(self.live_server_url + reverse("search"))
        time.sleep(1)
        searchFiled = self.browser.find_element_by_name("SearchField").send_keys(
            "pizza"
        )
        time.sleep(1)
        self.assertEquals(searchFiled, "pizza")
