"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def test_item():
    return Item('Phone', 5000, 10)


def test_correct_datas():
    with pytest.raises(ValueError):
        Item('ddd', 'ddd', 'ddd')


def test_calculate_total_price():
    assert test_item.calculate_total_price() == 50000


def test_apply_discount():
    assert test_item.apply_discount() == 5000

