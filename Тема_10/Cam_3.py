def add_two():
    try:
        user_input = input("Введите число для сложения с 2: ")
        number = float(user_input)
        result = 2 + number
        return f"Результат: 2 + {number} = {result}"
    except ValueError:
        return "Неподходящий тип данных. Ожидалось число."


print("=== Тест 1: Корректный ввод ===")
print(add_two())

print("\n=== Тест 2: Некорректный ввод (строка) ===")
print(add_two())

print("\n=== Тест 3: Корректный ввод (дробное число) ===")
print(add_two())

print("\n=== Тест 4: Некорректный ввод (спецсимволы) ===")
print(add_two())