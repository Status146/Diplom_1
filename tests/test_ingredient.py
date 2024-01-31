import pytest

from praktikum import ingredient_types
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'Хрустящие минеральные кольца', 300]
    ])
    def test_return_valid_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        actual_result = ingredient.get_price()
        assert actual_result == price

    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000]
    ])
    def test_return_valid_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        actual_result = ingredient.get_name()
        assert actual_result == name

    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'Сыр с астероидной плесенью', 4142]
    ])
    def test_return_valid_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        actual_result = ingredient.get_type()
        assert actual_result == ingredient_type
