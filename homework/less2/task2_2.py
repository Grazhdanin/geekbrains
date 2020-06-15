"""
 Для списка реализовать обмен значений соседних элементов, т.е.
 Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
 При нечетном количестве элементов последний сохранить на своем месте.
  Для заполнения списка элементов необходимо использовать функцию input().
"""
my_list = []

number = input('Количество элементов списка: ')
number = int(number)

while number > 0:
    my = input('Введите элементы: ')
    my_list.append(my)
    number -= 1
print(my_list)

for my in range(int(len(my_list) / 2)):
    my_list[number], my_list[number + 1] = my_list[number + 1], my_list[number]
    number += 2
print(my_list)