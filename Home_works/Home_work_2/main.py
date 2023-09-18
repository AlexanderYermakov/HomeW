# Домашняя работа к семинару 2

# Task 1
# Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

# basis_number = int(input("Введите число для перевода: "))
# trans_values = {'10':'a', '11':'b', '12':'c', '13':'d', '14':'e', '15':'f'}
# list_values = [10, 11, 12, 13, 14, 15]
# change_index = 16

# def Trans_number(number, change_index):
#     result = ' '
#     while number:
#         current = number % change_index
#         if list_values.count(current) != 0:
#             current = trans_values.get(str(current))
#         result = f'{current}' + result
#         number //= change_index
#     return result
#
# print(f'Число {basis_number} в шестнадцатиричной системе - {Trans_number(basis_number, change_index)}')
# print(f'Проверочный результат - {hex(basis_number)}')




# Task2
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions

numerator1, denominator1 = map(int, input('Введите первую дробь без пробелов используя знак "/" - ').split('/'))
numerator2, denominator2 = map(int, input('Введите вторую дробь без пробелов используя знак "/" - ').split('/'))
# получение числителя и знаменателя дробей

def Frac_multiplication(num1, denom1, num2, denom2):
    return f'{num1 * num2}/{denom1 * denom2}'

def Frac_Summation(num1, denom1, num2, denom2):
    if denom1 == denom2:
        return f'{num1 + num2}/{denom1}'
    else:
        return 'Жесть'

mult = fractions.Fraction(numerator1, denominator1) * fractions.Fraction(numerator2, denominator2)
sum = fractions.Fraction(numerator1, denominator1) + fractions.Fraction(numerator2, denominator2)

print(Frac_multiplication(numerator1, denominator1, numerator2, denominator2))
print(mult)

print(Frac_Summation(numerator1, denominator1, numerator2, denominator2))
print(sum)