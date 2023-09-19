# Домашняя работа к семинару 2

# Task 1
# Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def Trans_number_hex(number):

    change_index = 16
    trans_values = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f'}
    list_values = [10, 11, 12, 13, 14, 15]
    result = ' '

    while number:
        current = number % change_index

        if list_values.count(current) != 0:
            current = trans_values.get(str(current))
        result = f'{current}' + result
        number //= change_index

    return result

basis_number = int(input("Введите число для перевода: "))

print(f'Число {basis_number} в шестнадцатиричной системе - {Trans_number_hex(basis_number)}')
print(f'Проверочный результат - {hex(basis_number)}')




# Task2
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions
def Frac_multiplication(num1, denom1, num2, denom2):
    result = f'{num1 * num2}/{denom1 * denom2}'
    return result

def Frac_summation(num1, denom1, num2, denom2):
    if denom1 == denom2:
        result = f'{num1 + num2}/{denom1}'
        return result
    else:
        result = f'{num1 * denom2 + num2 * denom1}/{denom1 * denom2}'
        return result

numerator1, denominator1 = map(int, input('Введите первую дробь без пробелов используя знак "/" - ').split('/'))
numerator2, denominator2 = map(int, input('Введите вторую дробь без пробелов используя знак "/" - ').split('/'))
# получение числителя и знаменателя дробей

multiplication_check = fractions.Fraction(numerator1, denominator1) * fractions.Fraction(numerator2, denominator2)
sum_check = fractions.Fraction(numerator1, denominator1) + fractions.Fraction(numerator2, denominator2)

print(f'Произведение данных дробей: {Frac_multiplication(numerator1, denominator1, numerator2, denominator2)}')
print(f'Проверочный результат произведения: {multiplication_check}')

print(f'Сумма данных дробей: {Frac_summation(numerator1, denominator1, numerator2, denominator2)}')
print(f'Проверочный результат суммы: {sum_check}')
