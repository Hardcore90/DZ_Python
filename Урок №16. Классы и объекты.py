# Задание №1

# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:

# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег
print("Задание №1")
class Cassa(object):
    currentMoney = 0

    def __init__(self, cm):
        self.currentMoney = cm
    
    def top_up(self, X):
        print(f"Операция добавления денег в кассу: Добавляем {X}")
        self.currentMoney = self.currentMoney + X
    
    def count_1000(self):
        print("Операция подсчета тысячных купюр в кассе: ")
        count = 0
        num = self.currentMoney
        while num > 1000:            
            num = num - 1000
            count += 1            
        print(f"Количество целых тысяч в кассе - {count}\n")

    def take_away(self, X):
        print(f"Операция вычета денег из кассы: Вычитаем {X}")
        if self.currentMoney < X:
            print("Ошибка! В кассе не хватает денег!")
        else:
            self.currentMoney -= X

cassa = Cassa(5000)
print(f'Текущее количество денег в кассе: {cassa.currentMoney}\n')
cassa.top_up(500)
print(f'Текущее количество денег в кассе: {cassa.currentMoney}\n')
cassa.count_1000()
cassa.take_away(5600)
print(f'Текущее количество денег в кассе: {cassa.currentMoney}\n')
cassa.take_away(3000)
print(f'Текущее количество денег в кассе: {cassa.currentMoney}\n')
cassa.count_1000()

            


# Задание №2

# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход

# у этого класс есть методы:

# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции

print("Задание №2")
class Turtle(object):
    positionX = 0
    positionY = 0
    step = 1

    def __init__(self, x, y, s):
        self.positionX = x
        self.positionY = y
        self.step = s

    def go_up(self):
        self.positionY += self.step
    
    def go_down(self):
        self.positionY -= self.step
    
    def go_left(self):
        self.positionX -= self.step
    
    def go_right(self):
        self.positionX += self.step
    
    def evolve(self):
        self.step += 1
    
    def degrade(self):
        if self.step <= 0:
            print('Ошибка!')
        else:
         self.step -= 1

    def count_moves(self, x2, y2):
        count = 0
        while self.positionX != x2:
            if self.positionX > x2:
                self.go_left()
                count += 1
            elif self.positionX < x2:
                self.go_right()
                count += 1
        while self.positionY != y2:   
            if self.positionY > y2:
                self.go_down()
                count += 1
            elif self.positionY < y2:
                self.go_up()
                count += 1
        print(f"Минимальное количество действий, за которое черепашка сможет добраться до ({x2} {y2}) от текущей позиции - {count}")

turtle = Turtle(0, 0, 1)
turtle.count_moves(10, 10)
turtle2 = Turtle(0, 0, 1)
turtle2.evolve()
turtle2.count_moves(10, 10)