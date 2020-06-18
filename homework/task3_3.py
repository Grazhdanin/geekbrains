"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func(var1, var2, var3):
    iter_obj = [var1, var2, var3]
    iter_obj.remove(min(iter_obj))
    return print(sum(iter_obj))

my_func(4, 7, 2)