class Drink:
    def make(self):
        print("Готовится напиток...")

class Coffee(Drink):
    def make(self):
        print("Готовится кофе")

class Tea(Drink):
    def make(self):
        print("Заваривается чай")

def prepare(drink):
    drink.make()

prepare(Coffee())
prepare(Tea())
