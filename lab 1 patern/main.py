# Клас Bill (Рахунок) для управління фінансами клієнта
class Bill:
    def __init__(self, limiting_amount):
        # Встановлюємо ліміт витрат і початковий борг (0)
        self.limiting_amount = limiting_amount
        self.current_debt = 0

    # Перевіряє, чи не перевищує нова сума ліміт витрат
    def check(self, amount):
        return self.current_debt + amount <= self.limiting_amount

    # Додає суму до поточного боргу, якщо ліміт не перевищений
    def add(self, amount):
        if self.check(amount):
            self.current_debt += amount

    # Оплачує частину боргу
    def pay(self, amount):
        self.current_debt -= amount

    # Змінює ліміт витрат на новий
    def change_limit(self, new_limit):
        self.limiting_amount = new_limit


# Клас Operator (Оператор) для розрахунку вартості послуг зв'язку
class Operator:
    def __init__(self, ID, talking_charge, message_cost, network_charge, discount_rate):
        # Встановлюємо параметри оператора: тарифи на дзвінки, повідомлення, інтернет і ставку знижки
        self.ID = ID
        self.talking_charge = talking_charge
        self.message_cost = message_cost
        self.network_charge = network_charge
        self.discount_rate = discount_rate

    # Розраховує вартість дзвінка. Якщо клієнт молодший 18 або старший 65 років, застосовується знижка
    def calculate_talking_cost(self, minutes, customer):
        cost = minutes * self.talking_charge
        if customer.age < 18 or customer.age > 65:
            cost -= cost * (self.discount_rate / 100)  # застосовуємо знижку
        return cost

    # Розраховує вартість повідомлень. Якщо оператори у клієнтів однакові, також надається знижка
    def calculate_message_cost(self, quantity, customer, other_customer):
        cost = quantity * self.message_cost
        if customer.operator == other_customer.operator:
            cost -= cost * (self.discount_rate / 100)  # знижка для однакового оператора
        return cost

    # Розраховує вартість інтернет-трафіку за кількість МБ
    def calculate_network_cost(self, amount):
        return amount * self.network_charge


# Клас Customer (Клієнт), що описує взаємодію клієнта з оператором
class Customer:
    def __init__(self, ID, name, age, operator, bill, limiting_amount):
        # Ініціалізуємо параметри клієнта: ID, ім'я, вік, оператор та рахунок
        self.ID = ID
        self.name = name
        self.age = age
        self.operator = operator
        self.bill = bill
        self.limiting_amount = limiting_amount

    # Метод для здійснення дзвінка іншому клієнту
    def talk(self, minutes, other_customer):
        cost = self.operator.calculate_talking_cost(minutes, self)
        if self.bill.check(cost):  # перевіряємо, чи дозволяє ліміт
            self.bill.add(cost)
            print(f"{self.name} говорив з {other_customer.name} {minutes} хвилин.")
        else:
            print(f"{self.name} не може здійснити дзвінок через ліміт рахунку.")

    # Метод для надсилання повідомлень іншому клієнту
    def message(self, quantity, other_customer):
        cost = self.operator.calculate_message_cost(quantity, self, other_customer)
        if self.bill.check(cost):  # перевіряємо ліміт рахунку
            self.bill.add(cost)
            print(f"{self.name} надіслав {quantity} повідомлень {other_customer.name}.")
        else:
            print(f"{self.name} не може надіслати повідомлення через ліміт рахунку.")

    # Метод для підключення до інтернету
    def connect_to_internet(self, amount):
        cost = self.operator.calculate_network_cost(amount)
        if self.bill.check(cost):  # перевірка, чи вистачає ліміту для інтернету
            self.bill.add(cost)
            print(f"{self.name} використав {amount} МБ даних.")
        else:
            print(f"{self.name} не може підключитися до інтернету через ліміт рахунку.")

    # Оплата рахунку
    def pay_bill(self, amount):
        self.bill.pay(amount)
        print(f"{self.name} оплатив {amount} на свій рахунок.")

    # Зміна оператора на нового
    def change_operator(self, new_operator):
        self.operator = new_operator
        print(f"{self.name} змінив оператора.")

    # Зміна ліміту рахунку на новий
    def change_bill_limit(self, new_limit):
        self.bill.change_limit(new_limit)
        print(f"{self.name} змінив ліміт рахунку на {new_limit}.")


# Основна частина програми
if __name__ == "__main__":
    # Створюємо двох операторів з різними тарифами
    operator1 = Operator(1, 0.5, 0.1, 0.05, 10)
    operator2 = Operator(2, 0.4, 0.2, 0.08, 5)

    # Створюємо два рахунки з різними лімітами
    bill1 = Bill(100)
    bill2 = Bill(150)

    # Створюємо двох клієнтів з різними операторами та рахунками
    customer1 = Customer(1, "Іван", 25, operator1, bill1, 100)
    customer2 = Customer(2, "Аліса", 70, operator2, bill2, 200)

    # Дзвінок від Івана до Аліси
    customer1.talk(20, customer2)

    # Надсилання повідомлень від Івана до Аліси
    customer1.message(5, customer2)

    # Використання інтернету Іваном
    customer1.connect_to_internet(50)

    # Іван оплачує рахунок і змінює оператора
    customer1.pay_bill(50)
    customer1.change_operator(operator2)

    # Іван змінює ліміт рахунку
    customer1.change_bill_limit(200)
