def stats(numbers):
    if not numbers:
        return ()
    return (min(numbers), max(numbers), round(sum(numbers) / len(numbers), 2))

# Тесты
print(stats([10, 20, 30, 40, 50]))    
print(stats([5, 5, 5, 5]))
print(stats([2, 8, 15, 3, 9, 10]))