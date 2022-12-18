import datetime as dt
from random import uniform
from itertools import permutations


# Волшебник, сидящий справа, что-то пробормотал себе под нос и метнул заклинание вдоль столешницы.
# Оно проделало в лаковом покрытии дымящуюся борозду и примерно на полпути встретилось с серебряными змеями заклинания
# Эффективного Гадосейства, выпущенного волшебником слева. Волшебники обменялись долгими, медленными взглядами –
# такими взглядами можно спокойно жарить каштаны.
#
# Напишите программу, определяющую более сильные заклинания, то есть числа, большие первого в строке и имеющие четную
# сумму последних трех разрядов.

def ProgramOne():
    *array, = iter(input, '')

    result = []
    for i in array:
        temp = []
        a = [int(i) for i in i.split('%%')]
        for number in a[1:]:
            if a[0] < number and len(str(number)[-3:]) == 3 and sum(map(int, str(number)[-3:])) % 2 == 0:
                temp.append(number)
        result.append(temp)

    print('\n'.join(['v'.join(map(str, line)) for line in result]))


# Отдал ракету в ремонт. Прошлый раз слишком близко подошел к Солнцу; весь лак облез.
# Завмастерской убеждает купить электрический мозг. У него один есть, вполне приличный, почти не бывший в употреблении,
# мощностью двенадцать паровых душ.
#
# Напишите программу для определения безопасных дат сближения с Солнцем в зависимости от наличия мозга.
#
# Если мозг есть, то каждое третье сближение безопасное (на двух предыдущих он успевает научиться). Если мозга нет,
# то безопасные только те сближения, что попадают на четверг.

def ProgramTwo():
    d, m, y = map(int, input('Введите дату (DD.MM.YYYY): ').split('.'))
    myDate = dt.date(y, m, d)
    brain = int(input('Введите есть мозг или нет (1-0): '))
    period = int(input('Введите период обращения вокруг Солнца: '))
    deltaTime = dt.timedelta(days=1)
    datesCount = 0
    count = 1
    targetDatesCount = int(input('Введите количество требуемых дат: '))
    while datesCount != targetDatesCount:
        myDate += deltaTime
        if brain == 1:
            if count % 3 == 0 and count % period == 0:
                print(myDate.strftime('%d %B %y'))
                datesCount += 1
        else:
            if myDate.weekday() == 3 and count % period == 0:
                print(myDate.strftime('%d %B %y'))
                datesCount += 1
        count += 1


# Стартовал к Луне ровно в два, сразу после обеда.
# Похоже, простудился в лунной тени – все время чихаю. Принял аспирин. По курсу – три товарные ракеты с
# Плутона; машинист телеграфировал, чтобы я пропустил их. Спросил, что за груз; думал, бог знает что,
# а это обыкновенные брындасы.

# Напишите программу, создающую несколько различных случайных ракет со случайным грузом на случайных траекториях.

# Номер ракеты – прописная буква латинского алфавита из заданного диапазона, две любые цифры,
# номер целиком не повторяется;
# Грузоподъёмность – целое число из заданного диапазона с шагом 50, повторения возможны;
# Дальность – вещественное число из заданного диапазона с точностью до одного знака после запятой, без повторений;
# Груз – случайная строка из заданного набора, без повторений.


def ProgramThree():
    firstLetterOfRange, secondLetterOfRange = input().split()
    startRangeLoadCapacity, endRangeLoadCapacity = map(int, input().split())
    startRangeSpeed, endRangeSpeed = map(float, input().split())
    cargos = input().split(", ")
    countOfRockets = int(input())
    for i, num in enumerate(permutations("AA" + firstLetterOfRange)):
        print(f"Rocket {''.join(num) + str(secondLetterOfRange) * 2} ("
              f"{i * 10 + startRangeLoadCapacity + 10 - startRangeLoadCapacity % 10}, "
              f"{round(uniform(startRangeSpeed, endRangeSpeed), 1)}) follows with cargo of {cargos[i]}.")
        if i == countOfRockets - 1: break
