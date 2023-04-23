from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from login.models import PassChange, User
from login import mail
from login.mail import send_reset_password_mail
from django.test import Client
import uuid
import unittest


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

    def test_count_user(self):
        self.assertEqual(User.objects.count(), 1)

    def test_count_passchange(self):
        self.assertEqual(PassChange.objects.count(), 1)

    def test_valid_email(self):
        self.browser.get(self.live_server_url + reverse("passreset"))
        self.browser.find_element(By.NAME, value="email").send_keys(self.my_user.email)
        self.browser.find_element(By.NAME, "valbutton").click()
        # Check if email user is in passchange
        self.assertEqual(self.passchange.email, self.my_user.email)

    def test_token_not_empty(self):
        assert self.mytoken != ""

    def test_valid_token(self):
        myclient = Client()
        myurl = f"http://127.0.0.1:8000/login/password_reset/{str(self.mytoken)}"
        response = myclient.get(myurl)
        self.assertEqual(response.status_code, 200)

    def test_api_response(self, mocker):
        # mocker.patch(send_reset_password_mail, "function_name", return_value=True)
        # expected_value = True
        # assert send_reset_password_mail.function_name() == expected_value

        # return_value = {"sucess": True}
        # mocker.patch.object(send_reset_password_mail, "method_to_mock")
        # self.assertEqual(mocker.result(return_value), return_value)

        mocker.patch("mail.send_reset_password_mail", return_value={"success": True})
        expected_value = {"sucess": True}
        assert mail.send_reset_password_mail() == expected_value

    def test_mail_subject(mocker):
        mocker.patch(
            "mail.send_reset_password_mail",
            return_value="Renouvellement mot de passe Nutella",
        )
        subject = mail.send_reset_password_mail()
        assert subject != ""
