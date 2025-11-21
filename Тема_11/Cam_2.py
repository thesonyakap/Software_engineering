def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = 200

with open("fib.txt", "w", encoding="utf-8") as file:
    for number in fib(n):
        file.write(str(number) + "\n")

print("Файл fib.txt успешно создан.")
