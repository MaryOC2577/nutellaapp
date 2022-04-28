import pytest
from django.urls import reverse, resolve

def test_home():
    path = reverse("home")
    assert resolve(path).view_name == "home"

def test_login():
    path = reverse("login")
    assert resolve(path).view_name == "login"

def test_logout():
    path = reverse("logout")
    assert resolve(path).view_name == "logout"

def test_account():
    path = reverse("account")
    assert resolve(path).view_name == "account"

def test_registration():
    path = reverse("registration")
    assert resolve(path).view_name == "registration"

def test_search():
    path = reverse("search")
    assert resolve(path).view_name == "search"

def test_result():
    path = reverse("result")
    assert resolve(path).view_name == "result"

def test_oneproduct():
    path = reverse("oneproduct", kwargs={'pk':1})
    path == "search/oneproduct/1/"
    assert resolve(path).view_name == "oneproduct"

# def test_substitutes():
#     path = reverse("substitutes", kwargs={'pk':1)
#     path ==""
#     assert resolve(path).view_name == "substitutes"

def test_favorites():
    path = reverse("favorite")
    assert resolve(path).view_name == "favorite"

def test_delete_favorite():
    path = reverse("delete")
    assert resolve(path).view_name == "delete"

