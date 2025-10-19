def top_three_digits(num_string):
    counts = {int(d): num_string.count(d) for d in set(num_string)}
    top3 = dict(sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:3])
    return dict(sorted(top3.items()))

# Пример
s = "1233455667890999555333"
result = top_three_digits(s)
print("3 самых часто встречающихся числа:", result)
