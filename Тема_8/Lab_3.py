from Тема_8.Lab_2 import Car

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

# Создаём новый класс, который наследуется от класса car, со своим атрибутом ёмкости батареи
    def charge(self):
        print(f"Charhing the {self.make} {self.model} with {self.battery_capacity} kWh")

# Создаём новый метод charge

my_electric_car = ElectricCar("Tesla", "Model D", 75)
my_electric_car.drive()
my_electric_car.charge()