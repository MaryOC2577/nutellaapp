from nutella.management.commands import populate_db
from pytest import MonkeyPatch
from django.core.management import call_command

class TestPopulate():
    
    def test_populate(self, monkeypatch):
        monkeypatch.setattr('requests.get', lambda: {"faux produit"})
        call_command("populate_db", "pizza", 1, 1)
        # appel orm faux produit