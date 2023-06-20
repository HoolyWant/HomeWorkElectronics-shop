"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone
from src.keyboard import KeyBoard
import pytest


@pytest.fixture
def test_item():
    a = Item('Phone', 5000, 10)
    return a


@pytest.fixture
def test_phone():
    a = Phone('iPhone 14', 120000, 5, 2)
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
    test_item3 = Item('BigGun', 1000000, 1)
    with pytest.raises(Exception):
        test_item3.name('BigFuckingGun')
    test_item3.name = 'IggyPop'
    assert test_item3.name == 'IggyPop'


def test_set_number_of_sim():
    a = Phone('iPhone 14', 120000, 5, 2)
    with pytest.raises(ValueError):
        a.number_of_sim = -1
    with pytest.raises(ValueError):
        a.number_of_sim = 0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_repr_str_add():
    test_item4 = Item('Freezer', 20000, 15)
    test_phone = Phone('iPhone 14', 120000, 5, 2)
    assert repr(test_item4) == "Item('Freezer', 20000, 15)"
    assert str(test_item4) == 'Freezer'
    assert repr(test_phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert str(test_phone) == 'iPhone 14'
    assert test_item4 + test_phone == 20
    assert test_phone + test_phone == 10
    assert test_item4 + test_item4 == 30

def test_keyboard():
    test_kb = KeyBoard("Logitech 777", 10000, 16)
    assert test_kb.language == 'EN'
    test_kb.change_lang()
    assert test_kb.language == 'RU'

    with pytest.raises(AttributeError):
        test_kb.language = 'UA'

    assert str(test_kb) == "Logitech 777"
    assert repr(test_kb) == "KeyBoard('Logitech 777', 10000, 16)"
