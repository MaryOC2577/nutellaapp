from login.models import PassChange, User
from login.mail import send_reset_password_mail
from login.authenticate import EmailAuth
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from selenium import webdriver
from selenium.webdriver.common.by import By
import uuid
import pytest
from unittest import mock


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

    @mock.patch(
        "login.mail.send_reset_password_mail",
        return_value={
            "message_id": "<202305011333.65333901694@smtp-relay.mailin.fr>",
            "message_ids": None,
        },
    )
    def test_api_response(self, mocker):
        assert send_reset_password_mail(
            email=self.my_user.email, token=self.mytoken, user=self.my_user.username
        )

    @mock.patch("login.mail.send_reset_password_mail")
    def test_mail_subject(self, mocker):
        assert send_reset_password_mail(
            email=self.my_user.email, token=self.mytoken, user=self.my_user.username
        ) != {
            "message_id": "<202305011333.65333901694@smtp-relay.mailin.fr>",
            "message_ids": None,
        }

    def test_setup(self):
        assert isinstance(self.my_user, User)
        assert isinstance(self.passchange, PassChange)
        assert self.mytoken != ""


@pytest.mark.django_db
class TestMail(TestCase):
    def setUp(self):
        self.auth = EmailAuth()
        self.client = Client()
        self.credentials = {"username": "testuser", "password": "secret"}
        User = get_user_model()
        User.objects.create_user(**self.credentials)

    def test_login(self):
        self.auth.authenticate(self.credentials)
        # send login data
        response = self.client.post("/login/", self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context["user"].is_authenticated)
