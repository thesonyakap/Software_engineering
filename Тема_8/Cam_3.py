from Тема_8.Cam_2 import CoffeeMachine

class SmartCoffeeMachine(CoffeeMachine):
    def __init__(self, model, water_level, wifi_enabled=True):
        super().__init__(model, water_level)
        self.wifi_enabled = wifi_enabled

    def check_connection(self):
        if self.wifi_enabled:
            print("Wi-Fi подключен")
        else:
            print("Wi-Fi выключен")

smart_machine = SmartCoffeeMachine("DeLonghi Smart", 120)
smart_machine.make_coffee("Капучино")
smart_machine.check_connection()
