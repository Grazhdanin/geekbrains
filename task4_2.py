"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

my_list = [1, 2, 2, 2, 44, 4, 1, 68, 113, 44, 44, 67]
# new_list = [new for num, new in enumerate(my_list)]
# print(num, new)
new_list =[new for num, new in enumerate(my_list) if my_list[num -1] < my_list[num]]
# for num, new in enumerate(my_list):
#
#     if my_list[num - 1] < my_list[num]:
#         new_list.append(new)
#
print(new_list)