class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
# Создаём класс car с помощью конструктора, затем создаем экземпляр класса car

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

# Создаём метод drive для класса car

my_car = Car("Toyota", "Corolla") #создаём экземпляр класса car
my_car.drive()