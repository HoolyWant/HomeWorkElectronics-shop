"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def test_item():
    return Item('Phone', 5000, 10)

@pytest.fixture
def test_item2():
    return Item('Dog', '2', 0)


def test_correct_datas(test_item2):
    with pytest.raises(TypeError):
        test_item2.apply_discount()

def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 50000


def test_apply_discount(test_item):
    test_item.pay_rate = 0.8
    test_item.apply_discount()
    assert test_item.price == 4000

