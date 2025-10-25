def add_expense():
    category = input("Введите категорию расхода: ")
    amount = input("Введите сумму: ")
    description = input("Введите описание: ")

    with open("expenses.txt", "a", encoding="utf-8") as file:
        file.write(f"{category};{amount};{description}\n")
    print("Расход добавлен!\n")

def show_expenses():
    print("Текущие расходы:")
    try:
        with open("expenses.txt", "r", encoding="utf-8") as file:
            for line in file:
                cat, amt, desc = line.strip().split(";")
                print(f"{cat:15} | {amt:>8} руб | {desc}")
    except FileNotFoundError:
        print("Файл с расходами пока не создан.")

if __name__ == "__main__":
    while True:
        print("\n1 - Добавить расход\n2 - Показать все расходы\n3 - Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            break
        else:
            print("Неверный выбор!")
