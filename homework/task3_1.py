"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def dividing_number ():
    try:
        number1 = input('Введите первое число: ')
        number1 = float(number1)
        number2 = input('Введите второе число: ')
        number2 = float(number2)
        number = number1 / number2
        return round(number, 4)
    except ZeroDivisionError:
        return "division by zero"

print(dividing_number())