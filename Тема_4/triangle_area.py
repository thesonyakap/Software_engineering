from math import sqrt

def heron_area(a, b, c):
    s = (a + b + c) / 2  # полупериметр
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area
