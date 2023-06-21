# Задание №1

# Есть родительский класс:

 
print('Задание №1\n')
class Transport:

    def __init__(self, name, max_speed, mileage):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def printTransport(self):
     print(f'Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}')

    

# Создайте объект Autobus, который унаследует все переменные и методы родительского класса Transport и выведете его.
# Ожидаемый результат вывода:

# Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

class Autobus(Transport):
    def printAutobus(self):
        print(f'Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}')

transport = Transport('BMW X6', 220, 15)
transport.printTransport()
bus = Autobus('Renaul Logan', 180, 12)
bus.printTransport()
bus.printAutobus()
print('')

# Задание №2

# Создайте класс Autobus, который наследуется от класса Transport.

# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.

# Используйте переопределение метода.

# Используйте следующий код для родительского класса транспортного средства:

print("Задание №2\n")

class Transport2:

    def __init__(self, name, max_speed, mileage):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
 

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

class Autobus2(Transport2):
    def seating_capacity(self, capacity):
        print(f"Вместимость одного автобуса {self.name}  {capacity} пассажиров")
 

bus2 = Autobus2('Renaul Logan',180,12)
bus2.seating_capacity(50)

# Ожидаемый результат вывода:

# Вместимость одного автобуса Renaul Logan: 50 пассажиров