""" User model. """

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.TextField(unique=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    password = models.TextField()


class PassChange(models.Model):
    email = models.EmailField(_("email address"))
    token = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
