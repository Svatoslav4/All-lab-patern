import json
import math

# Клас Port
class Port:
    def __init__(self, id, latitude, longitude):
        """
        Ініціалізує порт з унікальним ID, широтою (latitude) та довготою (longitude).
        Зберігає списки поточних кораблів, історію кораблів та контейнери в порту.
        """
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []  # Контейнери, що знаходяться в порту
        self.history = []      # Історія кораблів, які відвідували порт
        self.current = []      # Кораблі, які наразі знаходяться в порту

    def get_distance(self, other):
        """
        Обчислює географічну відстань між цим портом та іншим портом.
        Використовується формула Евклідової відстані.
        """
        return math.sqrt((self.latitude - other.latitude)**2 + (self.longitude - other.longitude)**2)

    def incoming_ship(self, ship):
        """
        Додає корабель до списку поточних кораблів у порту, якщо його ще немає в списку.
        """
        if ship not in self.current:
            self.current.append(ship)

    def outgoing_ship(self, ship):
        """
        Видаляє корабель з поточного списку кораблів і додає його в історію, якщо він там ще не був.
        """
        if ship in self.current:
            self.current.remove(ship)
            if ship not in self.history:
                self.history.append(ship)


# Клас Ship
class Ship:
    def __init__(self, id, fuel, current_port, total_weight_capacity, max_all_containers,
                 max_heavy_containers, max_refrigerated_containers, max_liquid_containers,
                 fuel_consumption_per_km):
        """
        Ініціалізує корабель з унікальним ID, кількістю палива, поточним портом, максимальною
        вагою контейнерів, кількістю контейнерів різних типів, та витратою палива на км.
        """
        self.id = id
        self.fuel = fuel
        self.current_port = current_port
        self.total_weight_capacity = total_weight_capacity
        self.max_all_containers = max_all_containers
        self.max_heavy_containers = max_heavy_containers
        self.max_refrigerated_containers = max_refrigerated_containers
        self.max_liquid_containers = max_liquid_containers
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.containers = []  # Контейнери на кораблі

    def sail_to(self, destination_port):
        """
        Виконує переміщення корабля до іншого порту, якщо є достатньо палива для подорожі.
        """
        distance = self.current_port.get_distance(destination_port)  # Обчислює відстань до нового порту
        fuel_needed = distance * self.fuel_consumption_per_km  # Підрахунок необхідного палива
        if self.fuel >= fuel_needed:
            # Якщо палива достатньо, корабель вирушає в новий порт
            self.fuel -= fuel_needed
            self.current_port.outgoing_ship(self)  # Видаляємо корабель зі старого порту
            self.current_port = destination_port  # Оновлюємо поточний порт
            destination_port.incoming_ship(self)  # Додаємо корабель до нового порту
            return True
        return False  # Якщо палива недостатньо, подорож не виконується

    def refuel(self, fuel_amount):
        """
        Додає паливо до корабля.
        """
        self.fuel += fuel_amount

    def load(self, container):
        """
        Завантажує контейнер на корабель, якщо кількість контейнерів на кораблі не перевищує ліміт.
        """
        if len(self.containers) < self.max_all_containers:
            self.containers.append(container)
            return True
        return False

    def unload(self, container):
        """
        Розвантажує контейнер з корабля.
        """
        if container in self.containers:
            self.containers.remove(container)
            return True
        return False


# Клас Container та його похідні класи
class Container:
    def __init__(self, id, weight):
        """
        Ініціалізує контейнер з унікальним ID та вагою.
        """
        self.id = id
        self.weight = weight

    def consumption(self):
        """
        Абстрактний метод для підрахунку споживання палива контейнером.
        Повинен бути перевизначений у похідних класах.
        """
        raise NotImplementedError

    def __eq__(self, other):
        """
        Порівнює два контейнери за ID та вагою.
        """
        return self.id == other.id and self.weight == other.weight


class BasicContainer(Container):
    def consumption(self):
        """
        Підраховує споживання палива для базового контейнера.
        """
        return 2.5 * self.weight


class HeavyContainer(Container):
    def consumption(self):
        """
        Підраховує споживання палива для важкого контейнера.
        """
        return 3.0 * self.weight


class RefrigeratedContainer(HeavyContainer):
    def consumption(self):
        """
        Підраховує споживання палива для рефрижераторного контейнера.
        """
        return 5.0 * self.weight


class LiquidContainer(HeavyContainer):
    def consumption(self):
        """
        Підраховує споживання палива для рідкого контейнера.
        """
        return 4.0 * self.weight


# Основна функція
def main():
    """
    Основна функція для симуляції портів, кораблів та контейнерів.
    Виконує завантаження контейнерів на корабель, плавання до іншого порту,
    та виведення результатів у форматі JSON.
    """
    # Створюємо два порти
    port1 = Port(1, 50.0, 30.0)
    port2 = Port(2, 60.0, 40.0)

    # Створюємо корабель і два контейнери
    ship = Ship(1, 1000.0, port1, 5000, 10, 5, 2, 2, 1.5)
    container1 = BasicContainer(1, 2000)
    container2 = RefrigeratedContainer(2, 4000)

    # Завантаження контейнерів на корабель
    ship.load(container1)
    ship.load(container2)

    # Плавання до іншого порту
    if ship.sail_to(port2):
        print(f"Корабель {ship.id} успішно прибув до порту {port2.id}.")
    else:
        print(f"Корабель {ship.id} не має достатньо палива.")

    # Виведення результатів у форматі JSON
    result = {
        "Port": {
            port1.id: {"lat": port1.latitude, "lon": port1.longitude},
            port2.id: {"lat": port2.latitude, "lon": port2.longitude}
        },
        "Ship": {
            ship.id: {
                "fuel_left": ship.fuel,
                "containers": [container.id for container in ship.containers]
            }
        }
    }

    # Записуємо результати в файл output.json
    with open('output.json', 'w') as f:
        json.dump(result, f, indent=4)


# Виклик основної функції
if __name__ == "__main__":
    main()
