# Задание №1

# Пользователь вводит целое число. Выведите его строку-описание вида "отрицательное четное число", "нулевое число", "положительное нечетное число", например, численным описанием числа 190 является строка "положительное четное число". Если число не является четным - выведите сообщение "число не является четным"

num = int(input("Введите целое число: "))
if num == 0:
    print('нулевое число')
elif num > 0:
    if num % 2 == 0:
        print(f"'{num}' - положительное четное число")
    else:
        print(f"'{num}' - положительное нечетное число")
elif num < 0:
    if num % 2 == 0:
        print(f"'{num}' - отрицательное четное число")
    else:
        print(f"'{num}' - отрицательное нечетное число")


# Задание №2

# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».

# Для решения задачи создайте переменную и в неё положите слово с помощью input()

# А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False

word = input("Введите слово маленькими латинскими буквами: ")
flag = False
sumVowelsDigits = 0
sumConsonantsDigits = 0
for i in range(len(word)):
    if (word[i] == 'a') or (word[i] == 'e') or (word[i] == 'i') or (word[i] == 'o') or (word[i] == 'u'):
        flag = True
        sumVowelsDigits += 1
    else:
        sumConsonantsDigits += 1
print(f"Кол-во гласных букв в слове {word} - {sumVowelsDigits}")
print(f"Кол-во согласных букв в слове {word} - {sumConsonantsDigits}")
if flag == False:
    print('False')



# Задание №3

# Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали, что минимальная сумма инвестиций - X долларов, больше инвестировать можно сколько угодно. У Майкла A долларов, у Ивана B долларов. Если оба могут вложиться - выведите 2, если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.

minSumInvest = int(input("Минимальная сумма инвестиций: "))
michelCash = int(input('Сколько долларов у Майкла: '))
ivanCash = int(input('Сколько долларов у Ивана: '))
if (michelCash >= minSumInvest) and (ivanCash >= minSumInvest):
    print(2)
elif (michelCash >= minSumInvest) and (ivanCash < minSumInvest):
    print('Mike')
elif (michelCash < minSumInvest) and (ivanCash >= minSumInvest):
    print('Ivan')
elif ((michelCash+ivanCash) >= minSumInvest):
    print(1)
else:
    print(0)