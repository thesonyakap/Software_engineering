def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = 200
fibs = list(fib(n))
print(f"200-е число Фибоначчи: {fibs[-1]}")
