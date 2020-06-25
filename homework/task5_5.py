"""
Создать (программно) текстовый файл,
записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
"""

with open('task_5_doc.txt', 'w') as text:
    line = input('Введите цифры через пробел: \n')
    text.writelines(line)

sum_list = []

with open('task_5_doc.txt', 'r') as sum_text:
    new_list = sum_text.read().split(' ')
    for number in new_list:
        number = int(number)
        sum_list.append(number)
print(sum(sum_list))