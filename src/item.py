import csv
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        file = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(file, encoding='windows-1251') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                name, price, quantity = row['name'], float(row['price']), int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(stroke):
        return int(float(stroke))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        else:
            self.__name = name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise ValueError('Складывать можно только объекты Item или дочерние от них')
