def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read().strip()

            if not data:
                raise ValueError("Файл пуст!")

            print("Содержимое файла:")
            print(data)
            return data

    except FileNotFoundError:
        print("Ошибка: файл не найден!")
    except ValueError as e:
        print("Ошибка:", e)
    except Exception as e:
        print("Непредвиденная ошибка:", e)

if __name__ == "__main__":
    filename = input("Введите имя файла: ")
    read_file(filename)
