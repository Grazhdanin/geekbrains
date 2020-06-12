"""Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369."""

number = input("Введите число: ")

var1 = int(number + number)
var2 = int(number + number + number)
number = int(number)

number_sum = number + var1 + var2
print(number_sum)