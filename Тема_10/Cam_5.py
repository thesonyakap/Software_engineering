class NegativeNumberError(Exception):

    def __init__(self, value, operation=""):
        self.value = value
        self.operation = operation
        super().__init__(f"Отрицательное число {value} недопустимо для операции: {operation}")


def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError(number, "извлечение квадратного корня")

    return number ** 0.5


class BankAccount:

    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeNumberError(amount, "снятие денег со счета")

        if amount > self.balance:
            raise ValueError(f"Недостаточно средств. Баланс: {self.balance}")

        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeNumberError(amount, "пополнение счета")

        self.balance += amount
        return self.balance

    def get_balance(self):
        return self.balance


print("=== Демонстрация пользовательского исключения NegativeNumberError ===\n")

print("1. Тестирование функции calculate_square_root:")
try:
    result = calculate_square_root(16)
    print(f"Квадратный корень из 16 = {result}")
except NegativeNumberError as e:
    print(f"Ошибка: {e}")

try:
    result = calculate_square_root(-9)
    print(f"Квадратный корень из -9 = {result}")
except NegativeNumberError as e:
    print(f"Ошибка: {e}")

print("\n2. Тестирование класса BankAccount:")
account = BankAccount(1000)
print(f"Начальный баланс: {account.get_balance()}")

try:
    account.deposit(500)
    print(f"Баланс после пополнения: {account.get_balance()}")
except NegativeNumberError as e:
    print(f"Ошибка при пополнении: {e}")

try:
    account.withdraw(300)
    print(f"Баланс после снятия: {account.get_balance()}")
except NegativeNumberError as e:
    print(f"Ошибка при снятии: {e}")

try:
    account.deposit(-200)
    print(f"Баланс после пополнения: {account.get_balance()}")
except NegativeNumberError as e:
    print(f"Ошибка при пополнении: {e}")

try:
    account.withdraw(-100)  # Попытка отрицательного снятия
    print(f"Баланс после снятия: {account.get_balance()}")
except NegativeNumberError as e:
    print(f"Ошибка при снятии: {e}")

print(f"\nИтоговый баланс: {account.get_balance()}")