import pytest

# import os
# from nutella.management.commands import populate_db
# from pytest import MonkeyPatch
from django.core.management import call_command


class MockResponse:
    def json(self):
        return {"products": []}


@pytest.mark.django_db
class TestPopulate:
    def test_populate(self, monkeypatch):
        monkeypatch.setattr("requests.get", lambda url: MockResponse())
        call_command(command_name="populate_db")
        # appel orm faux produit
