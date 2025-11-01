class CoffeeMachine:
    def __init__(self, model, water_level=100):
        self.model = model
        self.water_level = water_level

    def make_coffee(self, type_of_coffee):
        if self.water_level >= 20:
            self.water_level -= 20
            print(f"{type_of_coffee} готов! Остаток воды: {self.water_level}%")
        else:
            print("Недостаточно воды!")

machine = CoffeeMachine("Philips 3200")
machine.make_coffee("Латте")
machine.make_coffee("Эспрессо")
