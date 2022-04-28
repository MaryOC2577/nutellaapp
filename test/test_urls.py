import pytest
from django.urls import reverse, resolve

def test_home():
    assert path == ""
    assert resolve(path).view_name == "home"

def test_login():
    assert path == "login/"
    assert resolve(path).view_name == "login"

def test_logout():
    assert path == "logout/"
    assert resolve(path).view_name == "logout"

def test_account():
    assert path == "account/"
    assert resolve(path).view_name == "account"

def test_registration():
    assert path == "registration/"
    assert resolve(path).view_name == "registration"

def test_search():
    assert path == "search/"
    assert resolve(path).view_name == "searh"

def test_result():
    assert path == "result/"
    assert resolve(path).view_name == "result"

def test_oneproduct():
    assert path == "oneproduct/<int:pk>/"
    assert resolve(path).view_name == "oneproduct"

def test_substitutes():
    assert path == "substitutes/<int:pk>/"
    assert resolve(path).view_name == "substitutes"

def test_favorites():
    assert path == "favorites/"
    assert resolve(path).view_name == "favorite"

def test_save_favorite():
    assert path == "savefavorite/<int:pk>/"
    assert resolve(path).view_name == "favorite"

def test_delete_favorite():
    assert path == "delete/<int:pk>/"
    assert resolve(path).view_name == "delete"

