import time
class TrafficLight:
    _color = None
    _colors = ['красный', 'желтый', 'зеленый']

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        i=0
        while i<5:
            for el in TrafficLight._colors :
                print(el)
                i+=1
                time.sleep(1)

traffic = TrafficLight()
traffic.running()


class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Creat road_to_village object')

    def intake(self):
        self.weigth = 100
        self.tickness = 0.10
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Потребуется {intake} тон для покрытия асфальта')

road_to_village = Road(2000, 3)
road_to_village.intake()


class Worker:
    name = None
    surname = None
    position = None
    profit = None
    bonus = None

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)
    def get_full_name(self):
        return self.name + self.surname
    def get_full_profit(self):
        self.__income = {'доход ': self.profit, 'премия ': self.bonus}
        return self.__income

manager = Position('Иван ', 'Иванов', 'менеджер', 30000, 1000)
print(manager.get_full_name(), manager.get_full_profit())


class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return "Машина поехала "
    def stop(self):
        return "Машина остановилась "
    def turn(self, direction):
        return "Машина повернула " + direction

class TownCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color)
        self.family = family

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

ford = TownCar('БМВ', 120, 'черный')
print(ford.name, ford.color, ford.speed, ford.is_police)
print(ford.go(), ford.turn('Город'), ford.stop())
sport = SportCar('Мерседес', 100, 'черный')
work1 = WorkCar('Форд', 60, 'белый', True)
work2 = WorkCar('БМВ', 90, 'красный', False)
police = PoliceCar('КИА', 70, 'желтый')


class Stationery:
    atr_title = 'Title'
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')
class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')

my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()