import pytest
from src.item import Item, InstantiateCSVError


def test_csv_file():
    Item.instantiate_from_csv('test_csv.py')
    assert Item.all == [Item('a', 'b', 'c')]


def test_broken_csv_file():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('test_items_2.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('test_items_3.csv')
