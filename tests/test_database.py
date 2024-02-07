from praktikum.database import Database


class TestDatabase:

    def test_return_available_buns_list(self):
        db = Database()
        actual_result = len(db.available_buns())
        assert actual_result == 3

    def test_return_available_ingredients_list(self):
        db = Database()
        actual_result = len(db.available_ingredients())
        assert actual_result == 6
