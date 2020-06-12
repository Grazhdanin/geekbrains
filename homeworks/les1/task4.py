"""Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

number = input("Введите число: ")
number = int(number)
number_max = 0

while number > 10:
    var = number % 10
    number //= 10
    if var > number_max:
        number_max = var

print(number_max)