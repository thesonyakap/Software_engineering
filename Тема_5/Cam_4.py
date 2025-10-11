def fix_grades(grades):
    return [4 if g == 3 else g for g in grades if g != 2]

grades_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades_3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print("Обновлённый список 1:", fix_grades(grades_1))
print("Обновлённый список 2:", fix_grades(grades_2))
print("Обновлённый список 3:", fix_grades(grades_3))
