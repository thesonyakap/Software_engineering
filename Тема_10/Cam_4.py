import time


class CacheDecorator:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1

        cache_key = (args, tuple(kwargs.items()))

        if cache_key in self.cache:
            print(f"Используется кэшированный результат для {self.func.__name__}({args})")
            return self.cache[cache_key]

        print(f"Вычисление нового результата для {self.func.__name__}({args})")
        result = self.func(*args, **kwargs)
        self.cache[cache_key] = result

        return result

    def get_cache_info(self):
        return {
            'function_name': self.func.__name__,
            'call_count': self.call_count,
            'cache_size': len(self.cache),
            'cached_results': list(self.cache.keys())
        }


@CacheDecorator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
        time.sleep(0.1)
    return result


@CacheDecorator
def power(base, exponent=2):
    time.sleep(0.1)
    return base ** exponent


print("=== Демонстрация работы кэширующего декоратора ===\n")

print("1. Тестирование функции factorial:")
print(f"factorial(5) = {factorial(5)}")
print(f"factorial(5) = {factorial(5)}")
print(f"factorial(3) = {factorial(3)}")
print(f"factorial(5) = {factorial(5)}")

print("\n2. Тестирование функции power:")
print(f"power(2, 3) = {power(2, 3)}")
print(f"power(2, 3) = {power(2, 3)}")
print(f"power(4) = {power(4)}")
print(f"power(4, 2) = {power(4, 2)}")

print("\n3. Информация о кэше:")
print("Factorial cache:", factorial.get_cache_info())
print("Power cache:", power.get_cache_info())