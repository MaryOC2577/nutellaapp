from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from login.models import PassChange, User
from django.test import Client
import uuid


class TestChangePassword(StaticLiveServerTestCase):
    def setUp(self):
        # Set firefox drivers
        self.browser = webdriver.Firefox(executable_path="geckodriver")
        self.mytoken = uuid.uuid4()
        # Create user
        self.my_user = User.objects.create(
            **{
                "username": "azerty",
                "email": "marybot@free.fr",
                "password": "test_test",
            }
        )
        self.passchange = PassChange.objects.create(
            **{
                "email": "marybot@free.fr",
                "token": self.mytoken,
            }
        )

    def tearDown(self):
        self.browser.close()

    def test_password_reset_page(self):
        response = self.client.get(reverse("passreset"))
        self.assertEqual(response.status_code, 200)

    def test_template_reset_page(self):
        response = self.client.get(reverse("passreset"))
        self.assertTemplateUsed(response, "change_password.html")

    def test_password_done_page(self):
        response = self.client.get(reverse("passdone"))
        self.assertEqual(response.status_code, 200)

    def test_template_done_page(self):
        response = self.client.get(reverse("passdone"))
        self.assertTemplateUsed(response, "password_done.html")

    def test_new_user(self):
        # create new user
        self.browser.get(self.live_server_url + reverse("registration"))
        self.browser.find_element(By.NAME, value="username").send_keys(
            self.my_user.username
        )
        self.browser.find_element(By.NAME, value="email").send_keys(self.my_user.email)
        self.browser.find_element(By.NAME, value="password1").send_keys(
            self.my_user.password
        )
        self.browser.find_element(By.NAME, value="password2").send_keys(
            self.my_user.password
        )
        self.browser.find_element(By.ID, value="valButton").click()
        passchange_user = PassChange()
        print("passchange_user.email : ", passchange_user.email)
        print("self.my_user.email : ", self.my_user.email)
        self.assertEquals(passchange_user.email, self.my_user.email)

    def test_valid_email(self):
        self.browser.get(self.live_server_url + reverse("passreset"))
        self.browser.find_element(By.NAME, value="email").send_keys(self.my_user.email)
        self.browser.find_element(By.NAME, "valbutton").click()
        # Check if email user is in passchange
        self.assertEqual(self.passchange.email, self.my_user.email)

    def test_valid_token(self):
        myclient = Client()
        myurl = f"http://127.0.0.1:8000/login/password_reset/{str(self.mytoken)}"
        response = myclient.get(myurl)
        self.assertEqual(response.status_code, 200)

    def test_email_builder(self):
        


