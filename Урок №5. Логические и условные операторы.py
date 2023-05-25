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
sum = [0, 0, 0, 0, 0]
for i in range(len(word)):
    if(word[i] == 'a'):
        sumVowelsDigits += 1
        sum[0] += 1
    elif(word[i] == 'e'):
        sumVowelsDigits += 1
        sum[1] += 1
    elif(word[i] == 'i'):
        sumVowelsDigits += 1
        sum[2] += 1
    elif(word[i] == 'o'):
        sumVowelsDigits += 1
        sum[3] += 1
    elif(word[i] == 'u'):
        sumVowelsDigits += 1
        sum[4] += 1
    else:
        sumConsonantsDigits += 1

for i in range(len(sum)):
    if (sum[i] == 0):
        sum[i] = 'False'

print(f'Количество гласных: {sumVowelsDigits}, Количество согласных: {sumConsonantsDigits}!')
print(f'Количество "a": {sum[0]}, Количество "e": {sum[1]}, Количество "i": {sum[2]}, Количество "o": {sum[3]}, Количество "u": {sum[4]}')
        



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