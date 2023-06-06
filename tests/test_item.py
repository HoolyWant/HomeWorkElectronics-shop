"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def test_item():
    a = Item('Phone', 5000, 10)
    return a


@pytest.fixture
def test_item2():
    a = Item('Dog', '2', 0)
    return a


def test_correct_datas(test_item2):
    with pytest.raises(TypeError):
        test_item2.apply_discount()


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 50000


def test_apply_discount(test_item):
    test_item.pay_rate = 0.8
    test_item.apply_discount()
    assert test_item.price == 4000


def test_string_to_number():
    assert Item.string_to_number('5.111111') == 5
    assert Item.string_to_number('6764') == 6764
    assert Item.string_to_number('6.9999') == 6


def test_set_name():
    with pytest.raises(Exception):
        test_item3 = Item('BigGun', 1000000, 1)
        test_item3.name('BigFuckingGun')


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_repr_str():
    test_item4 = Item('Freezer', 20000, 15)
    assert repr(test_item4) == "Item('Freezer', 20000, 15)"
    assert str(test_item4) == 'Freezer'

