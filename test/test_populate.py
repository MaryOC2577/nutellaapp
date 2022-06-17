from nutella.management.commands import populate_db

class TestPopulate():

    def get_populate(self):
        return populate_db

    def test_populate():

        def monkey_populate():
            cmd_populate = populate_db
            return cmd_populate

        monkeypatch.setattr(cmd_populate, "pizza", monkey_populate())

        cmd = get_populate()
        assert cmd == cmd_populate