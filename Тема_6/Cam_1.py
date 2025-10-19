numbers = input("Введите числа через пробел: ").split()
numbers_list = [int(num) for num in numbers]
numbers_tuple = tuple(numbers_list)

print("Список:", numbers_list)
print("Кортеж:", numbers_tuple)