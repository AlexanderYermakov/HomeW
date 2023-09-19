# 1.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

side_a = int(input("Input the length of side A: "))
side_b = int(input("Input the length of side B: "))
side_c = int(input("Input the length of side C: "))

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:    # проверка на треугольник

    if side_a == side_b == side_c:  # равносторонний
        print("this is an equilateral triangle")

    elif side_a == side_b or side_b == side_c or side_a == side_c:  # равнобедренный
        print("this is an isosceles triangle")

    else:
        print("this is a versatile triangle")  # разносторонний

else:
    print("this triangle does not exist")



# 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел
# и чисел больше 100 тысяч.

def Check_num(number):
    if number == 2 or number == 3:
        return "Введенное число является простым"

    elif number % 2 == 0 or number < 2:
        return "Введенное число не является простым"

    for i in range(3, number, 2):
        if number % i == 0:
            return "Введенное число не является простым"
    return "Введенное число является простым"

number = int(input("Введите число от 0 до 100000: "))

if number < 0 or number > 100000:
    print("Ошибка ввода введите число от 0 до 100000 ")
else:
    print(Check_num(number))


# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
def Hidden_number(lower_limit, upper_limit, max_attempts):
    number = randint(lower_limit, upper_limit)

    for attempt in range(max_attempts):
        number_x = int(input(f"Попытка №{attempt + 1}: "))
        if number_x < number:
            print("Загаданное число больше вашего")
        elif number_x > number:
            print("Загаданное число меньше вашего")
        else:
            return print(f"Ура! Вы угадали, задуманное число - {number}")

    return print(f"Вы к сожалению не угадали... Задуманное число - {number}")

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

print("Угадайте число от 0 до 1000. На это у вас 10 попыток!")
Hidden_number(LOWER_LIMIT, UPPER_LIMIT, MAX_ATTEMPTS)





