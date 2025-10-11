from math import sqrt

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

mins = [min(one), min(two), min(three)]
maxs = [max(one), max(two), max(three)]

def heron(a, b, c):
    p = (a + b + c) / 2
    return round(sqrt(p * (p - a) * (p - b) * (p - c)), 2)

print("Площадь треугольника с минимальными сторонами:", heron(*mins))
print("Площадь треугольника с максимальными сторонами:", heron(*maxs))
