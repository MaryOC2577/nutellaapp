import time
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from login.models import PassChange


class TestChangePassword(StaticLiveServerTestCase):
    def setUp(self):
        # Set firefox drivers
        self.browser = webdriver.Firefox(executable_path="geckodriver")

    def tearDown(self):
        self.browser.close()

    def test_valid_email(self):
        self.browser.get(self.live_server_url + reverse("passreset"))
        time.sleep(1)
        searchFiled = self.browser.find_element_by_name("usermail").send_keys(
            "test@test.fr"
        )
        time.sleep(1)
        self.assertEquals(searchFiled, "test@test.fr")

    def test_user_resest(self):
        # create new user
        self.browser.get(self.live_server_url + reverse("registration"))
        time.sleep(1)
        self.browser.find_element_by_name("username").send_keys("test")
        time.sleep(1)
        self.browser.find_element_by_name("email").send_keys("test@test.fr")
        time.sleep(1)
        self.browser.find_element_by_name("password1").send_keys("test")
        time.sleep(1)
        self.browser.find_element_by_name("password2").send_keys("test")
        time.sleep(1)
        self.browser.find_element_by_id("LogButton").click()
        time.sleep(5)
        # redirect to password reset page
        self.live_server_url + reverse("passreset")
        self.browser.find_element_by_name("usermail").send_keys("test@test.fr")
        # redirect to change password page
        token = PassChange.objects.get(email="test@test.fr")
        self.live_server_url + reverse(
            f"127.0.0.1:8000/login/password_reset/{token.token}"
        )
        self.browser.find_element_by_name("email").send_keys("test@test.fr")
        time.sleep(1)
        self.browser.find_element_by_name("newpass").send_keys("test1")
        time.sleep(1)
        self.browser.find_element_by_name("newpass2").send_keys("test1")
        time.sleep(1)
