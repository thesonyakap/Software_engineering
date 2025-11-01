from Тема_8.Cam_2 import CoffeeMachine

class SmartCoffeeMachine(CoffeeMachine):
    def __init__(self, model, water_level, wifi_enabled=True):
        super().__init__(model, water_level)
        self.__password = "1234"  # приватный атрибут
        self.wifi_enabled = wifi_enabled

    def __check_password(self, password):
        return password == self.__password

    def update_firmware(self, password):
        if self.__check_password(password):
            print("Обновление прошивки начато...")
        else:
            print("Ошибка: неверный пароль!")

machine = SmartCoffeeMachine("Bosch Pro", 100)
machine.update_firmware("0000")
machine.update_firmware("1234")
