def average(*args):
    return sum(args) / len(args)

if __name__ == "__main__":
    print("Среднее значение:", average(5, 10, 15, 20, 25))
