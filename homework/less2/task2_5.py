"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
 то новый элемент с тем же значением должен разместиться после них.
"""

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
print("(0 - выход)")
number = int(input("Введите число: "))

while number != 0:
    for my in range(len(my_list)):
        if my_list[my] == number:
            my_list.insert(my + 1, number)
            break
        elif my_list[0] < number:
            my_list.insert(0, number)
        elif my_list[-1] > number:
            my_list.append(number)
        elif my_list[my] > number and my_list[my + 1] < number:
            my_list.insert(my + 1, number)
    print(f"текущий список - {my_list}")
    number = int(input("Введите число "))