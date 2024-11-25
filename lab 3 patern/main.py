from abc import ABC, abstractmethod
import unittest
from unittest.mock import MagicMock

# Абстрактний клас Item для визначення загальних властивостей контейнерів
class Item(ABC):
    def __init__(self, item_id, weight, count, container_id):
        # Ідентифікатор товару
        self.item_id = item_id
        # Вага одного контейнера
        self.weight = weight
        # Кількість контейнерів
        self.count = count
        # Ідентифікатор контейнера
        self.container_id = container_id

    # Абстрактний метод для підрахунку загальної ваги контейнерів
    @abstractmethod
    def get_total_weight(self):
        pass


# Реалізація конкретного класу для маленьких контейнерів
class SmallItem(Item):
    # Метод для підрахунку загальної ваги маленьких контейнерів
    def get_total_weight(self):
        return self.weight * self.count


# Реалізація класу для важких контейнерів
class HeavyItem(Item):
    def get_total_weight(self):
        return self.weight * self.count


# Реалізація класу для охолоджуваних контейнерів
class RefrigeratedItem(Item):
    def get_total_weight(self):
        return self.weight * self.count


# Реалізація класу для рідких контейнерів
class LiquidItem(Item):
    def get_total_weight(self):
        return self.weight * self.count


# Фабрика для створення контейнерів
class ItemFactory:
    # Метод для створення контейнера на основі його типу
    @staticmethod
    def create_item(item_type, item_id, weight, count, container_id):
        if item_type == "small":
            return SmallItem(item_id, weight, count, container_id)
        elif item_type == "heavy":
            return HeavyItem(item_id, weight, count, container_id)
        elif item_type == "refrigerated":
            return RefrigeratedItem(item_id, weight, count, container_id)
        elif item_type == "liquid":
            return LiquidItem(item_id, weight, count, container_id)
        else:
            # Якщо тип контейнера невідомий, викликається помилка
            raise ValueError("Невідомий тип контейнера")


# Абстрактний клас для кораблів
class Ship(ABC):
    def __init__(self, ship_id, max_weight, fuel_capacity):
        # Ідентифікатор корабля
        self.ship_id = ship_id
        # Максимальна вага, яку може нести корабель
        self.max_weight = max_weight
        # Ємність паливного бака
        self.fuel_capacity = fuel_capacity
        # Список контейнерів на борту
        self.containers = []

    # Метод для завантаження контейнерів на корабель
    def load_container(self, item):
        # Підрахунок загальної ваги з новим контейнером
        total_weight = sum([c.get_total_weight() for c in self.containers]) + item.get_total_weight()
        if total_weight <= self.max_weight:
            # Якщо вага в межах допустимого, контейнер додається на корабель
            self.containers.append(item)
        else:
            # Інакше виводиться повідомлення про перевищення ваги
            print("Завантаження не можливе, перевищено вагу")

    # Метод для вивантаження контейнерів з корабля
    def unload_container(self):
        if self.containers:
            # Вивантажується перший контейнер зі списку
            return self.containers.pop(0)
        else:
            # Якщо контейнерів немає, виводиться відповідне повідомлення
            print("Немає контейнерів для вивантаження")


# Легкий корабель
class LightWeightShip(Ship):
    def __init__(self, ship_id):
        # Встановлюємо вагу та паливну ємність для легкого корабля
        super().__init__(ship_id, max_weight=10000, fuel_capacity=500)


# Середній корабель
class MediumShip(Ship):
    def __init__(self, ship_id):
        super().__init__(ship_id, max_weight=20000, fuel_capacity=1000)


# Важкий корабель
class HeavyShip(Ship):
    def __init__(self, ship_id):
        super().__init__(ship_id, max_weight=50000, fuel_capacity=2000)


# Builder для створення кораблів
class ShipBuilder:
    def __init__(self):
        # Тип корабля, який будується
        self._ship_type = None

    # Встановлення типу корабля (легкий, середній, важкий)
    def set_ship_type(self, ship_type):
        self._ship_type = ship_type
        return self

    # Створення корабля за типом
    def build(self, ship_id):
        if self._ship_type == "lightweight":
            return LightWeightShip(ship_id)
        elif self._ship_type == "medium":
            return MediumShip(ship_id)
        elif self._ship_type == "heavy":
            return HeavyShip(ship_id)
        else:
            raise ValueError("Невідомий тип корабля")


# Приклад використання
if __name__ == "__main__":
    # Створення фабрики для контейнерів
    item_factory = ItemFactory()

    # Створення корабля за допомогою builder
    builder = ShipBuilder()
    ship = builder.set_ship_type("medium").build("Ship_001")

    # Створення контейнерів
    small_item = item_factory.create_item("small", 1, 100, 2, 101)
    heavy_item = item_factory.create_item("heavy", 2, 500, 1, 102)

    # Завантаження контейнерів на корабель
    ship.load_container(small_item)
    ship.load_container(heavy_item)

    # Вивантаження контейнерів з корабля
    ship.unload_container()


# Юніт-тести
class TestShipLoading(unittest.TestCase):
    # Тест завантаження контейнера на корабель
    def test_load_container(self):
        # Створення корабля та контейнера
        ship = MediumShip("Test_Ship")
        item = SmallItem(1, 100, 1, 101)

        # Мок для методу завантаження контейнера
        ship.load_container = MagicMock(return_value=None)
        ship.load_container(item)
        # Перевірка, що метод завантаження викликався
        ship.load_container.assert_called_once_with(item)


# Запуск тестів
if __name__ == "__main__":
    unittest.main()
