from time import sleep

class Tomato:
    states = ("absent", "flowering", "green", "red")

    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]

    def grow(self):
        """Перевести томат на следующую стадию, если это возможно."""
        current_index = Tomato.states.index(self._state)
        if current_index < len(Tomato.states) - 1:
            self._state = Tomato.states[current_index + 1]

    def is_ripe(self):
        """Возвращает True, если томат дозрел (последняя стадия)."""
        return self._state == Tomato.states[-1]

    def info(self):
        """Возвращает информацию о текущем состоянии томата."""
        return (self._index, self._state)


class TomatoBush:
    def __init__(self, count):
        """
        Создаёт список из count объектов Tomato и хранит его в динамическом свойстве tomatoes.
        tomatoes - динамическое свойство (список объектов Tomato).
        """
        self.tomatoes = [Tomato(i + 1) for i in range(count)]

    def grow_all(self):
        """Перевести все томаты на одну стадию вперёд."""
        for t in self.tomatoes:
            t.grow()

    def all_are_ripe(self):
        """Проверить, все ли томаты стали спелыми."""
        return all(t.is_ripe() for t in self.tomatoes)

    def give_away_all(self):
        """Собрать урожай: очистить список томатов (куст остаётся, но без плодов)."""
        self.tomatoes.clear()

    def info(self):
        """Вернуть список кортежей (index, state) для всех томатов."""
        return [t.info() for t in self.tomatoes]


class Gardener:
    @staticmethod
    def knowledge_base():
        """Статический метод: справка по базовым правилам ухода за томатами."""
        print("Справка по садоводству:")
        print("- Регулярно поливайте кусты и следите за стадиями созревания.")
        print("- Для созревания требуется несколько циклов ухода (каждый цикл -> следующая стадия).")
        print("- Собирайте урожай, когда все плоды становятся красными (стадия 'red').")
        print()

    def __init__(self, name, plant):
        """
        Динамические свойства:
        name  - публичное свойство (имя садовника)
        _plant - защищённое свойство, хранит ссылку на объект растения (TomatoBush)
        """
        self.name = name
        self._plant = plant

    def work(self):
        """Садовник ухаживает за растением: вызывает метод grow_all у растения."""
        print(f"{self.name} начинает работу: ухаживает за кустом...")
        self._plant.grow_all()
        print("...работа завершена. Текущее состояние кустa:", self._plant.info())
        print()

    def harvest(self):
        """
        Пытается собрать урожай: проверяет, все ли плоды спелые.
        Если все спелые — собирает (очищает список томатов).
        Если нет — выводит предупреждение.
        """
        print(f"{self.name} пытается собрать урожай...")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Ура! Урожай собран.")
        else:
            print("Внимание: не все плоды созрели. Продолжайте ухаживать.")
        print()


# Тесты 
if __name__ == "__main__":
    # 1) Вызов справки по садоводству
    Gardener.knowledge_base()

    # 2) Создаём куст и садовника
    bush = TomatoBush(4)            # куст с 4 томатами
    gardener = Gardener("Иван", bush)

    # Покажем начальное состояние
    print("Начальное состояние кустa:", bush.info())
    print()

    # 3) Садовник ухаживает за кустом (несколько циклов)
    gardener.work()   # 1-й цикл ухода
    # 4) Попробуем собрать урожай — пока не созрели
    gardener.harvest()

    # Продолжаем ухаживать (ещё 2 цикла — должно хватить, т.к. стадий 4)
    gardener.work()   # 2-й цикл
    gardener.work()   # 3-й цикл

    # 5) Теперь собираем урожай
    gardener.harvest()

    # Состояние куста после сбора
    print("Состояние кустa после сбора:", bush.info())
