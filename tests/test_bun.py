from praktikum.bun import Bun


class TestBun:

    def test_get_valid_name_return_correct_name_bun(self):
        bun = Bun("склизская булка", 1001)
        actual_result = bun.get_name()
        assert actual_result == "склизская булка"

    def test_get_valid_price_returned_correct_price_bun(self):
        bun = Bun("вулканическая булка", 999)
        actual_result = bun.get_price()
        assert actual_result == 999
