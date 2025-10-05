from triangle_area import heron_area

if __name__ == "__main__":
    a = float(input("Введите сторону a: "))
    b = float(input("Введите сторону b: "))
    c = float(input("Введите сторону c: "))
    print("Площадь треугольника:", heron_area(a, b, c))
