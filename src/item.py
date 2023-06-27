import csv
import os.path


class InstantiateCSVError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = 'Файл item.csv поврежден'

    def __str__(self):
        return self.message


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
        try:
            with open(file, encoding='windows-1251') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    name, price, quantity = row['name'], float(row['price']), int(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        except (TypeError, KeyError):
            raise InstantiateCSVError

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
        self.__name = name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item или дочерние от них')
        return self.quantity + other.quantity


class MixinLanguage:
    __language = 'EN'

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language

